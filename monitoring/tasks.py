from celery import shared_task

from .models import MonitoringLog


@shared_task
def clean_old_monitoring_logs():
    MAX_LOGS = 100
    total = MonitoringLog.objects.count()

    if total > MAX_LOGS:
        MonitoringLog.objects.all().delete()
        return f"Deleted all {total} logs"
    return "OK"
