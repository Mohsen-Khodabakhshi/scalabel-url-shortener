from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


@scheduler.scheduled_job("interval", seconds=60)
def scheduled_task() -> None:
    pass
