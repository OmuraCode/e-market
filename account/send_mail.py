from django.core.mail import send_mail


HOST = 'localhost:8000'


def send_confirmation_email(user, code):
    dev_link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    server_link = '/api/v1/accounts/activate/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n{dev_link}'
        f'\nСсылка работает один раз!',
        'akyl.net@gmail.com',
        [user],
        fail_silently=False,
    )
