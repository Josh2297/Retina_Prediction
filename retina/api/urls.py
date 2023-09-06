from django.urls import path
from .retina_views import VideoAdd

app_name = 'api'

urlpatterns = [
    path('video/', VideoAdd.as_view(), name='upload-video'),
]