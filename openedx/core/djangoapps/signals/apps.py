"""

Signal handlers are connected here.
"""

from django.apps import AppConfig


class SignalConfig(AppConfig):
    """
    Application Configuration for Grades.
    """
    name = u'openedx.core.djangoapps.signals'

    def ready(self):
        """
        Connect handlers to recalculate grades.
        """
        # Can't import models at module level in AppConfigs, and models get
        # included from the signal handlers
        from .signals import handlers  # pylint: disable=unused-variable
