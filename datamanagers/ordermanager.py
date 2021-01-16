import random
from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta
from faker import Faker
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from datamanagers.orderfilterabstract import OrderFilterAbstract
from datamanagers.orderfilteractive import OrderFilterActive
from datamanagers.orderfilterawaitingpickup import OrderFilterAwaitingPickup
from datamanagers.orderfilterfullfilled import OrderFilterFulfilled
from datamanagers.orderfilteridle import OrderFilterIdle
from datamanagers.orderfilterworking import OrderFilterWorking
from descriptors.lazyproperty import LazyProperty
from models.conversationmessage import ConversationMessage
from models.order import Order as orderObj
from models.order_status_enum import OrderStatus
from singleton import Singleton

fake = Faker()


class OrderManager(Widget):
    __metaclass__ = Singleton
    all_orders = ListProperty(rebind=True)
    urgent_orders = ListProperty(rebind=True)
    working_orders = ListProperty(rebind=True)
    idle_orders = ListProperty(rebind=True)
    awaiting_pickup_orders = ListProperty(rebind=True)
    fulfilled = ListProperty(rebind=True)
    current_order = ObjectProperty(orderObj(), rebind=True)
    food_word_list = [
        'latte', 'muffin', 'cappuccino',
        'breakfast sandwich', 'iced tea', 'chocolate chip cookie',
        'salad', 'artichoke panini', 'iced latte',
        'chia pudding', 'avocado toast', 'drip coffee', 'bowl of oatmeal']

    def __init__(self, **kwargs):
        super(OrderManager, self).__init__(**kwargs)
        self.register_event_type('on_loaded')
        self.register_event_type('on_updated')
        self.register_event_type('on_current_order_changed')
        self.register_event_type('on_clear')
        # self.load_dummy_orders()

    def on_updated(self, *args):
        pass

    def on_current_order_changed(self, value, *args):
        pass

    def on_current_order(self, value, *args):
        self.dispatch('on_current_order_changed', *args)

    def clear(self):
        self.all_orders.clear()
        self.dispatch('on_clear')

    def on_clear(self):
        pass

    def on_loaded(self, *args):
        pass

    # def update_order(self, order):
    #     update_index = next(i for i, x in enumerate(self.all_orders) if x.id == order.id)
    #     print(f'found index {update_index} for id: {order.id} with customer {order.customer_name}')
    #     print(f'attempting to update order {order.id} for {order.customer_name} with status {order.status.name} from '
    #           f'status {self.all_orders[next(i for i, x in enumerate(self.all_orders) if x.id == order.id)].status.name}')
    #     self.all_orders[next(i for i, x in enumerate(self.all_orders) if x.id == order.id)] = order

    def on_all_orders(self, instance, value):
        self.all_orders = value
        self.urgent_orders = OrderFilterActive().Filter(value)
        self.working_orders = OrderFilterWorking().Filter(value)
        self.idle_orders = OrderFilterIdle().Filter(value)
        self.awaiting_pickup_orders = OrderFilterAwaitingPickup().Filter(value)
        self.fulfilled = OrderFilterFulfilled().Filter(value)

    def refresh_orders(self, instance, value):
        # TODO get rid of debug statment
        # print('refreshing orders')
        prop = self.property('all_orders')
        prop.dispatch(self)

    def add_dummy_order(self):
        # print('adding order')
        new_order = orderObj()
        new_order.id = str(len(self.all_orders))
        new_order.customer_name = fake.name()
        # new_order.status = OrderStatus(random.randint(OrderStatus.NEW.value, OrderStatus.FULFILLED.value))
        if new_order.status is OrderStatus.NEW:
            new_order.time = datetime.now(tz=timezone.utc) + relativedelta(minutes=-random.randint(2, 4))
        else:
            new_order.time = datetime.now(tz=timezone.utc) + relativedelta(minutes=-random.randint(2, 15))
        msg = ConversationMessage()
        msg.id = msg.uid
        msg.send_time = new_order.time
        msg.sender = new_order.customer_name
        msg.message = f'{random.randint(1, 2)} {fake.word(ext_word_list=self.food_word_list)} and ' \
                                  f'{random.randint(1, 2)} {fake.word(ext_word_list=self.food_word_list)}'

        new_order.conversation.append(msg)

        biz_response = ConversationMessage()
        biz_response.send_time = msg.send_time + relativedelta(seconds=+45)
        biz_response.id = biz_response.uid
        biz_response.sender = 'Jibe Espresso Bar - Roland'
        biz_response.message = 'Hi! What size would you like?'
        biz_response.is_business_response = True

        new_order.conversation.append(biz_response)

        reply = ConversationMessage()
        reply.id = reply.uid
        reply.send_time = biz_response.send_time + relativedelta(seconds=+45)
        reply.sender = new_order.customer_name
        reply.message = "large thx"

        new_order.conversation.append(reply)
        # new_order.order_message = new_order.conversation[0].message
        new_order.bind(on_updated=self.refresh_orders)

        self.all_orders.append(new_order)

    def load_dummy_orders(self):
        count = 0
        self.clear()

        while count < random.randint(10, 30):
            self.add_dummy_order()
            count = count + 1
        self.dispatch('on_loaded')

