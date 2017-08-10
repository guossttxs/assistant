import celery

celery = celery.Celery('celery_module', include=['celery_module.tasks'])
celery.config_from_object('celery_module.config')

if __name__ == '__main__':
    pass