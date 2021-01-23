from functools import partial

from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.event import EventDispatcher
from kivy.uix.screenmanager import Screen, FallOutTransition

from models.conversationmessage import ConversationMessage
from models.order import Order
from models.order_status_enum import OrderStatus
from widgets.conversationmessagewidget import ConversationMessageWidget


class OrderDetailScreen(Screen):
    current_order = ObjectProperty(rebind=True)

    def __init__(self, **kwargs):
        # self.current_order = Order()
        super(OrderDetailScreen, self).__init__(**kwargs)

    def on_current_order(self, instance, value):
        self.ids.price_subtotal.subtotal.clear()
        self.ids.total.subtotal.clear()
        self.ids.conversation.clear_widgets()
        self.ids.fee.set_value("75")
        for message in value.conversation:
            self.ids.conversation.add_widget(ConversationMessageWidget(message))

        print("current order changed")

    #   def on_pre_enter(self, *args):
    #       # bindings for subtotal changes
    #       self.ids.price_subtotal.subtotal.bind(on_changed=self.update_total)
    #       self.ids.numpad.bind(on_key_pressed=self.set_price_subtotal)
    #
    def set_price_subtotal(self, value, *args):
        if args[0] == "Clear":
            self.ids.price_subtotal.subtotal.clear()
        else:
            self.ids.price_subtotal.subtotal.append(args[0])

    def update_total(self, value, *args):
        self.ids.total.subtotal.clear()
        self.ids.total.set_value(
            str(
                (
                    self.ids.price_subtotal.subtotal.total
                    + self.ids.tax.subtotal.total
                    + self.ids.fee.subtotal.total
                )
            )
        )

    def on_conversation_updated(self, value, *args):
        convo = args[0]

    def send_order_message(self):
        msg = ConversationMessage()
        msg.id = msg.uid
        msg.sender = "Jibe Espresso Bar - Roland"
        msg.message = self.ids.msg_input.text
        msg.is_business_response = True
        self.current_order.conversation.append(msg)
        new_message_widget = ConversationMessageWidget(msg)
        self.ids.conversation.add_widget(new_message_widget)

        self.ids.msg_input.text = ""
        # wait a moment before switching screens
        Clock.schedule_once(
            partial(self.update_order_status, OrderStatus.AWAITING_REPLY), 2
        )

    def update_order_status(self, status: OrderStatus, *args):
        self.current_order.status = status
        # go to the first screen with orders
        for screen in self.manager.screens:
            if hasattr(screen, "orders") and len(screen.orders) > 0:
                self.manager.transition = FallOutTransition()
                self.manager.current = screen.name
                break
