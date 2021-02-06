from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import cidades
from cidades import *
import main2
import imp

Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '600')

root = Builder.load_file('interface2.kv')

gsolucao = ''
gcusto = ''


class BLayout(GridLayout):
    pass


class ButtonComecar(Button):
	def __init__(self, **kwargs):
		super(ButtonComecar, self).__init__(**kwargs)
		self.text = 'Começar'

	def on_press(self):
		global gsolucao, gcusto

		imp.reload(main2)

		solucao, custo = main2.main(cidades.cidade_atual)
		gsolucao = solucao
		gcusto = custo


class LbScore(Label):
	def __init__(self, **kwargs):
		super(LbScore, self).__init__(**kwargs)
		Clock.schedule_interval(self.change_label, 0.1)

	def change_label(self, dt):
		global gsolucao, gcusto

		strtemp = '\n'
		for i in gsolucao:
			strtemp += str(i) + '\n'


		self.text = 'Solução: {s} \nCusto: {c}'.format(s=strtemp, c=gcusto)


class Line_AB(Widget):
	pass


class Buscas(App):
    def build(self):
        self.title = 'Buscas'
        return BLayout()


if __name__ == '__main__':
    Buscas().run()
