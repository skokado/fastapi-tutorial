from celery import Celery

from app.core.config import settings

REDIS_URL = 'redis://{host}:{port}/{db}'.format(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)
celery = Celery("worker", broker=REDIS_URL)
celery.conf.result_backend = REDIS_URL

celery.conf.task_routes = {
    "app.tasks.task1.*": {'queue': 'primary'},
    # "app.tasks.other_task.*": {'queue': 'secondary'},
}
