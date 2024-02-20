from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class hospital_appConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital_app'


class AdminConfig(DjangoSuitConfig):
    layout='vertical'