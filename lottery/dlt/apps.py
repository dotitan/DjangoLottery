from django.apps import AppConfig


class DltConfig(AppConfig):
    name = 'dlt'

    def ready(self):
        import dlt.signals.handlers
