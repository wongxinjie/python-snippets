from urllib.request import urlopen

from celery import Celery


app = Celery('tasks')

app.conf.update(
    broker_url="amqp://guest:guest@localhost:5672",
    result_backend="redis://localhost:6379/2",
    timezone='Asia/Shanghai',
    enable_utc=True,
    TCELERY_RESULT_NOWAIT=False
)


@app.task
def fetch_content(url):
    with urlopen(url) as page:
        content = page.read().decode("utf-8")
    return content


if __name__ == "__main__":
    app.start()
