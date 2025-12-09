import time

from django.db import connection
from django.utils.deprecation import MiddlewareMixin

from .models import MonitoringLog


class FullMonitoringMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()
        request._initial_queries = len(connection.queries)
        return None

    def process_response(self, request, response):
        try:
            duration_ms = (time.time() - request._start_time) * 1000
        except:
            duration_ms = 0

        initial = getattr(request, "_initial_queries", 0)
        queries = connection.queries[initial:]

        MonitoringLog.objects.create(
            method=request.method,
            path=request.path,
            status=response.status_code,
            duration_ms=round(duration_ms, 2),
            sql_count=len(queries),
            sql_data=[{"sql": q["sql"], "time": q.get("time")} for q in queries],
            ip=self._get_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", "-"),
            user_id=request.user.id if request.user.is_authenticated else None,
        )

        return response

    def _get_ip(self, request):
        x = request.META.get("HTTP_X_FORWARDED_FOR")
        return x.split(",")[0] if x else request.META.get("REMOTE_ADDR")
