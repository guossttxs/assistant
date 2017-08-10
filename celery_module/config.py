#!/usr/bin/env python
# -*- coding:utf8 -*-

from __future__ import absolute_import
from celery.schedules import crontab

CELERY_RESULT_BACKEND='redis://127.0.0.1:6379/5'
BROKER_URL='redis://127.0.0.1:6379/6'
CELERY_ACCEPT_CONTENT=['pickle', 'json', 'msgpack', 'yaml']
CELERY_RESULT_SERIALIZER='json'
CELERY_TASK_SERIALIZER='json'
CELERY_TASK_RESULT_EXPIRES=3600
CELERY_TIMEZONE='Asia/Shanghai'

CELERYBEAT_SCHEDULE={
    'inspection-every-5-min': {
        'task': 'celery_module.tasks.inspection_service',
        'schedule': crontab(minute='*/3'),
    }
}