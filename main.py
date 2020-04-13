import celery  
from celery.schedules import crontab
from datetime import datetime
import funcs
import lessons
import os
import time


url = os.environ.get('REDIS_URL')

app = celery.Celery('main', broker=url)
app.conf.timezone = 'Asia/Bishkek'
app.conf.beat_schedule = {
    '08.00': {
        'task': 'main.task',
        'schedule': crontab(hour=8),
        'args': (r'18\30975', '123456')
    },
    '9.30': {
        'task': 'main.task',
        'schedule': crontab(hour=9, minute=30),
        'args': (r'18\30975', '123456')
    },
    '11.00': {
        'task': 'main.task',
        'schedule': crontab(hour=11),
        'args': (r'18\30975', '123456')
    },
    '13.00': {
        'task': 'main.task',
        'schedule': crontab(hour=13, minute=1),
        'args': (r'18\30975', '123456')
    },
    '14.30': {
        'task': 'main.task',
        'schedule': crontab(hour=14, minute=31),
        'args': (r'18\30975', '123456')
    },
    '16.00': {
        'task': 'main.task',
        'schedule': crontab(hour=16, minute=2),
        'args': (r'18\30975', '123456')
    }
}


@app.task
def task(login, password):
    day = int(datetime.today().strftime('%w'))
    if day in range(1, 6):
        print(funcs.enter(login, password))
        time.sleep(600)
        print(funcs.enter(login, password)
