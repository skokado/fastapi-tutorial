from app.core.celery_app import celery


@celery.task(acks_late=True)
def greet(name: str) -> str:
    print('## called')
    return f"Hi {name} san!"
