from django.conf.urls import patterns, url 
from django.views.decorators.csrf import csrf_exempt 
import videos
from views import *

urlpatterns = patterns('video.views',
    url(r'^v1/get_videos/',csrf_exempt(VideosView.as_view())),
)

