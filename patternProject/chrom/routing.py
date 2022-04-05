from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/chrom/(?P<subject>\w+)/$', consumer.ChatConsumer.as_asgi()),
]