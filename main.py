from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.animation import AnimationTransition
# from app.notifications import *

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')


class SiteMonster(App):
    BG_COLOR = (1, 1, 1, 1)
    TEXT_COLOR = (0, 0, 0, 1)
    FONT_PATH = 'SegoeUI'
    WELCOME_H_TEXT = 'Welcome to SiteMonster!'
    WELCOME_T_TEXT = 'This app will notify you about any your server state.\n' \
                     'And it can make loud alarm if something went wrong :)'
    WELCOME_TEXT = 'Lets start using it\nand make some noise!'
    START_BTN_TEXT = 'Start'

    animation = Animation(duration=1, transition=AnimationTransition.in_out_cubic, step=1 / 60, x=- 384 / 2)

    def build(self):
        Window.clearcolor = self.BG_COLOR
        root = GridLayout(size=(1280, 720), cols=1, spacing=5)
        welcome_header = Label(text=self.WELCOME_H_TEXT, font_name=self.FONT_PATH, color=self.TEXT_COLOR,
                               font_size='24pt', size_hint=(.1, .1))
        welcome_title = Label(text=self.WELCOME_T_TEXT, font_name=self.FONT_PATH, color=self.TEXT_COLOR,
                              font_size='20pt', size_hint=(.15, .15))
        welcome_text = Label(text=self.WELCOME_TEXT, font_name=self.FONT_PATH, color=self.TEXT_COLOR,
                             font_size='20pt', size_hint=(.15, .15))
        start_btn = Button(text=self.START_BTN_TEXT, font_name=self.FONT_PATH, size_hint=(.5, .2), padding_x=(20, 20))

        root.add_widget(Widget(size_hint=(1, .1)))
        root.add_widget(welcome_header)
        root.add_widget(welcome_title)
        root.add_widget(welcome_text)
        root.add_widget(start_btn)
        root.add_widget(Widget(size_hint=(1, .1)))

        return root


if __name__ == '__main__':
    # send_notification("Ready to work!", "SiteMonster")
    SiteMonster().run()
