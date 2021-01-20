from functools import partial

from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, FallOutTransition

from models.conversationmessage import ConversationMessage
from models.order import Order
from models.order_status_enum import OrderStatus
from widgets.conversationmessagewidget import ConversationMessageWidget


class OrderDetailScreen(Screen):
    current_order: ObjectProperty(rebind=True)

    def __init__(self, **kwargs):
        # self.current_order = Order()
        super(OrderDetailScreen, self).__init__(**kwargs)

    def current_order_changed(self, *args):
        print("current order changed")

    def on_pre_enter(self, *args):
        print(self)
        print(
            f"on_pre_enter - screen current order: {self.current_order.customer_name}\n"
            f"on_pre_enter - current order: {self.manager.order_manager.current_order.customer_name}"
        )
        self.manager.order_manager.bind(
            on_current_order_changed=self.current_order_changed
        )
        self.current_order = self.manager.order_manager.current_order
        self.current_order.bind(on_conversation_updated=self.on_conversation_updated)
        prop = self.property("current_order")
        prop.dispatch(self)
        self.ids.conversation.clear_widgets()
        self.ids.numpad.bind(on_key_pressed=self.set_price_subtotal)

        for message in self.current_order.conversation:
            widget = ConversationMessageWidget(message)
            self.ids.conversation.add_widget(widget)

    def set_price_subtotal(self, value, *args):
        if args[0] is "Done":
            self.ids.price_subtotal.clear()
        else:
            self.ids.price_subtotal.append(args[0])
            print(f"new subtotal: {self.ids.price_subtotal.total}")
            print(f"appending to subtotal: {args[0]}")
        self.ids.total_label.text = "${:,.2f}".format(self.ids.price_subtotal.total)

    def on_conversation_updated(self, value, *args):
        convo = args[0]
        print(f"conversation updated with {args[0]}")

    def send_order_message(self):
        msg = ConversationMessage()
        msg.id = msg.uid
        msg.sender = "Jibe Espresso Bar - Roland"
        msg.message = self.ids.msg_input.text
        msg.is_business_response = True
        # TODO get rid of debug statement
        self.current_order.conversation.append(msg)
        new_message_widget = ConversationMessageWidget(msg)
        self.ids.conversation.add_widget(new_message_widget)

        # self.ids.scroll_view.scroll_to(new_message_widget)
        self.ids.msg_input.text = ""
        # wait a moment before switching screens
        # Clock.schedule_once(partial(self.update_order_status, OrderStatus.AWAITING_REPLY), 2)

    def on_current_order(self):
        # clear message box
        print("current order updated")
        self.ids.conversation.clear_widgets()
        for message in value.conversation:
            self.ids.conversation.add_widget(ConversationMessageWidget(message))

    def update_order_status(self, status: OrderStatus, *args):
        self.current_order.status = status
        # go to the first screen with orders
        for screen in self.manager.screens:
            if hasattr(screen, "orders") and len(screen.orders) > 0:
                self.manager.transition = FallOutTransition()
                self.manager.current = screen.name
                break
