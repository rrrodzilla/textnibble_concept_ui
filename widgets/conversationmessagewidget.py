from arrow import arrow
from kivy.animation import Animation
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from models.conversationmessage import ConversationMessage


class ConversationMessageWidget(BoxLayout):
    conversation = ObjectProperty(ConversationMessage, rebind=True)
    humanized_time = StringProperty(rebind=True)

    def __init__(self, conversation: ConversationMessage, **kwargs):
        self.conversation = conversation
        self.height = 0
        self.humanized_time = arrow.Arrow.fromdatetime(conversation.send_time).humanize()
        super(ConversationMessageWidget, self).__init__(**kwargs)
        prop = self.property('conversation')
        prop.dispatch(self)

    def on_conversation(self, instance, value):
        # print('on_conversation')
        if not self.height == 96:
            anim = Animation(height=96, t='in_out_quart', duration=.750)
            anim.start(self)
