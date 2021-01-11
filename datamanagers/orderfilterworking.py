from datamanagers.orderfilterabstract import OrderFilterAbstract
from models.order import Order
from models.order_status_enum import OrderStatus


class OrderFilterWorking(OrderFilterAbstract):
    def Filter(self, orders: Order):
        temp_orders = [r for r in orders if r.status is OrderStatus.WORKING]

        # self.order_total = len(temp_orders)
        # print(f'from get_filtered_order_list in {self.name}')
        # print(self.order_total)
        return temp_orders
