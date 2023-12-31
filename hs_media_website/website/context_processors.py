# myapp/context_processors.py
from django.utils.functional import LazyObject
from django.apps import apps

class LazyLogo(LazyObject):
    def _setup(self):
        # This function is called when the LazyLogo object is first accessed
        from .models import Logo
        self._wrapped = Logo.objects.first()

def logo(request):
    return {'logo': LazyLogo()}
