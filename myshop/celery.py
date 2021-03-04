# TODO принимает процессы но не выполняет
# celery -A myshop worker -l info
# celery -A myshop flower

import os
from celery import Celery

# Задаём переменную окружения, содержащую название файла настроек нашего проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
