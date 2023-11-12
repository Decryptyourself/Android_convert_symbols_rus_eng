from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty
from kivy.clock import Clock

class MainWindowConvert(BoxLayout):
    resultText = StringProperty("")

    def getText(self, instance):
        self.textForUser = self.ids.text_input.text
        self.convertText(self.textForUser)
        Clock.schedule_once(self.changeText, 30) # затирка текста через 30 секунд

    def convertText(self, text): #TODO перевод русских букв в английские
        self.resultText = text
        return self.resultText

    def copy_to_clipboard(self, instance):
        Clipboard.copy(self.resultText)

    def changeText(self, dt):
        self.textForUser = "cleaned"
        self.ids.text_label.text = self.textForUser

class ConvertRusEngApp(App):
    def build(self):
        Builder.load_file('main_window_convert.kv')
        return MainWindowConvert()

if __name__ == '__main__':
    ConvertRusEngApp().run()