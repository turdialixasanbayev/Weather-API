from django.db import models

### MonitoringLog modeli


class MonitoringLog(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    status = models.IntegerField()

    duration_ms = models.FloatField()
    sql_count = models.IntegerField()
    sql_data = models.JSONField()

    ip = models.GenericIPAddressField(null=True)
    user_agent = models.TextField(null=True)
    user_id = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return f"{self.method} {self.path} - {self.status} ({self.created_at})"

    class Meta:
        verbose_name = "Monitoring Log"
        verbose_name_plural = "Monitoring Logs"
        ordering = ["-created_at"]
