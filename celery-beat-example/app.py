from celery import Celery, chain

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5, scan_for_expired_users, name='expired')


@app.task
def scan_for_expired_users():
    for user in get_expired_users():
        deactivating_process = chain(deactivate_account.s(user), send_expiration_email.s())
        deactivating_process()


@app.task
def deactivate_account(user):
    print("deactivate account: %s" % user)
    return user + '_deactived'


@app.task
def send_expiration_email(user):
    print('sending email to user %s' % user)


def get_expired_users():
    return ('user_%s' % i for i in range(5))
