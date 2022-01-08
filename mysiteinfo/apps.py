from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MysiteinfoConfig(AppConfig):
    name = 'mysiteinfo'

    def ready(self):
        from .models import create_default_site_detail
        post_migrate.connect(create_default_site_detail, sender=self)
