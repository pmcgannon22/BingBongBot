from .base import *

GROUPME_AUTH_URL = "https://oauth.groupme.com/oauth/authorize?client_id=XqzF6g769VwqJih5kkHp5S11Qtk3edh3FB2if9As3uwVr0iS"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}