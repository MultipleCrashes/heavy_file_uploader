from django.conf.urls import patterns, url 
from django.views.decorators.csrf import csrf_exempt 
import videos
urlpatterns = patterns('video.views',
    url(r'^v1/get_videos/',csrf_exempt('Videos.as_view()')),
)

