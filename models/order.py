from datetime import datetime

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty

from models.conversationmessage import ConversationMessage
from models.order_status_enum import OrderStatus


class Order(EventDispatcher):
    status = ObjectProperty(OrderStatus.NEW, rebind=True)
    conversation = ListProperty([ConversationMessage], rebind=True)

    def __init__(self, **kwargs):
        self.id: str
        self.time: datetime
        self.customer_name: str = ''
        self.conversation: list[ConversationMessage] = []
        # self.order_message: str = ''

        self.register_event_type('on_updated')
        self.register_event_type('on_conversation_updated')
        super(Order, self).__init__(**kwargs)

    def __repr__(self):
        return "Order Object"

    def on_status(self, instance, value):
        print(f'status changed to {value}')
        self.dispatch('on_updated', value)

    def on_updated(self, *args):
        pass

    def on_conversation(self, value, *args):
        # print(f'triggered on_conversation  model {value}')
        self.dispatch('on_conversation_updated', value.conversation)
        pass

    def on_conversation_updated(self, *args):
        # print('triggered on_conversation from model object')
        pass
