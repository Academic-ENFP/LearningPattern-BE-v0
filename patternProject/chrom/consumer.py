# from email import message
# from msilib import text
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import json

# room_name -> subject
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # return self.accept()
        self.subject = self.scope['url_route']['kwargs']['subject']
        self.room_group_name = 'chrom_%s' % self.subject
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from WebSocket
    def receive(self, text_data):
        # json으로 채팅 메시지 받기
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # # json객체를 인코딩해서 보냄
        # self.send(text_data=json.dumps({
        #     'message' : message
        # }))
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))