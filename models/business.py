from faker import Faker
from faker.providers import phone_number
from kivy.event import EventDispatcher

from models.employee import Employee

fake = Faker()
fake.add_provider(phone_number)


class Business(EventDispatcher):

    def __init__(self, **kwargs):
        emp = Employee()
        emp.name = fake.name()
        emp.id = '1111'
        emp.pin = '1111'

        self.id: str
        self.name: str = 'Jibe Espresso Bar'
        self.textnibble_phone: str = fake.phone_number()
        self.employees: [] = [emp]
        super(Business, self).__init__(**kwargs)

    def __repr__(self):
        return "Business Object"
