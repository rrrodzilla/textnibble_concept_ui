from kivy.uix.screenmanager import Screen

from models.business import Business


class LoginScreen(Screen):
    biz = Business()

    def __call__(self, *args, **kwargs):
        super(LoginScreen, self).__call__()

    def login(self):
        emp_pin = list(self.biz.employees[0].pin)
        print(emp_pin)
        print(self.ids.pin_number.pin)
        if self.ids.pin_number.pin == list(self.biz.employees[0].pin):
            self.manager.current = 'main'
        else:
            self.ids.pin_number.clear()
