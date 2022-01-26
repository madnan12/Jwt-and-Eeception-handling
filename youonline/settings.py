import os
from pathlib import Path
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

YOU_ONLINE='http://127.0.0.1:8000'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#tqrqd&(r=k(mh!9n2t#p(h(=u^7d0#g@731t8=ve0l&hyrc#)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'rest_framework.authtoken',
    'rest_framework_simplejwt',
    # 'social_django',
    'company_info.apps.CompanyInfoConfig',
    'shopping_payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'youonline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ######## social login 
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'youonline.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




# LOGIN_REDIRECT_URL = '/google'
# LOGOUT_REDIRECT_URL = '/google'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JWT_AUTH = {

    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=9000),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',

}

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
    
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY':'error',
    # 'EXCEPTION_HANDLER': 'company_info.custom_handlers.custom_exception_handler',
    'EXCEPTION_HANDLER': 
    'company_info.custom_handlers.custom_exception_handler',

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
    
}



# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.facebook.FacebookOAuth2',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.github.GithubOAuth2',
#     'social_core.backends.google.GoogleOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )

# SOCIAL_AUTH_FACEBOOK_KEY = '666126297753078'  # App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = '94c07d76f32cf4d94a75e90ef1f0590a'  

# SOCIAL_AUTH_GITHUB_KEY = '76612c86a5bdcadfed8e'  # App ID
# SOCIAL_AUTH_GITHUB_SECRET = '6ff046fa943b36c43a984c3cd1c4a424607a019f'  

# SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77k0lawrqf78yd'  # App ID
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'SlIESLLKrMLaxLqY' 

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1008203962550-q1ht8gtrrrlonmb8tjhs5cg4ags8m9au.apps.googleusercontent.com'  # App ID
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' 

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'adnanshab205@gmail.com'
EMAIL_HOST_PASSWORD = 'googleafacebookdinstagramnlinkedina**786**n@#'
EMAIL_PORT = 587

STRIPE_PUBLIC_KEY=""
STRIPE_SECRET_KEY=""
STRIPE_WEBHOOK_KEY=""