from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, FallOutTransition

from models.order import Order
from models.order_status_enum import OrderStatus
from widgets.conversationmessagewidget import ConversationMessageWidget


class OrderDetailScreen(Screen):
    current_order = ObjectProperty(rebind=True)

    def __init__(self, **kwargs):
        super(OrderDetailScreen, self).__init__(**kwargs)

    def on_current_order(self, instance, value):
        self.ids.conversation.clear_widgets()
        for message in value.conversation:
            print(f'adding message for {message.sender}')
            self.ids.conversation.add_widget(ConversationMessageWidget(message))

    def update_order_status(self, status: OrderStatus):
        self.current_order.status = status
        # self.manager.update_order(self.current_order)
        for screen in self.manager.screens:
            if hasattr(screen, 'orders') and len(screen.orders) > 0:
                self.manager.transition = FallOutTransition()
                self.manager.current = screen.name
                break
        # self.manager.remove_widget(self)
