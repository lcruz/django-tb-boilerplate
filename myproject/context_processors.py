from django.conf import settings
from django.contrib.sites.models import Site

def basic_info(request):    
    print Site.objects.get_current()
    return {'media_url': settings.MEDIA_URL}