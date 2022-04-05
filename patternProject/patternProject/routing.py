from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chrom.routing

# 클라이언트와 channels 개발 서버가 연결 될 때, 어느 protocol타입의 연결인지 
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # websoket protocol이라면 AuthMiddlewareStack
    'websocket': AuthMiddlewareStack(
        # URLRouter로 연결, 소비자의 라우트 연결 HTTP path를 조사
        URLRouter(  
            chrom.routing.websocket_urlpatterns
        )
    ),
})