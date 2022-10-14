from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

    def ready(self) -> None:
        import store.signals
        return super().ready()
