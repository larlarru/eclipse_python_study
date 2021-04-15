# settings.py

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    # django-rest-auth
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    # django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',

    # my app
    'accounts',

    # provider
    'allauth.socialaccount.providers.kakao',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id': b9cfa5b35e3ae75acd84aeb36feb4e2a,
            'secret': kgy9466,
            'key': ''
        }
    }
}


