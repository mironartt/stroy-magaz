import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stroy_magaz.settings')

app = Celery('stroy_magaz')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()