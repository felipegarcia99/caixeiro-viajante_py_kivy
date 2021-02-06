from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock

cidade_atual = 'A'


class CidadeA(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeA, self).__init__(**kwargs)
		self.let = 'A'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicadoA')
		self.source = 'bolas/bolavermelhaA.png'
		cidade_atual = 'A'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaA.png'


class CidadeB(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeB, self).__init__(**kwargs)
		self.let = 'B'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaB.png'
		cidade_atual = 'B'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaB.png'


class CidadeC(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeC, self).__init__(**kwargs)
		self.let = 'C'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaC.png'
		cidade_atual = 'C'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaC.png'


class CidadeD(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeD, self).__init__(**kwargs)
		self.let = 'D'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaD.png'
		cidade_atual = 'D'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaD.png'


class CidadeE(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeE, self).__init__(**kwargs)
		self.let = 'E'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaE.png'
		cidade_atual = 'E'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaE.png'


class CidadeF(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeF, self).__init__(**kwargs)
		self.let = 'F'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaF.png'
		cidade_atual = 'F'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaF.png'


class CidadeG(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeG, self).__init__(**kwargs)
		self.let = 'G'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaG.png'
		cidade_atual = 'G'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaG.png'


class CidadeH(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeH, self).__init__(**kwargs)
		self.let = 'H'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaH.png'
		cidade_atual = 'H'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaH.png'


class CidadeI(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeI, self).__init__(**kwargs)
		self.let = 'I'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaI.png'
		cidade_atual = 'I'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaI.png'


class CidadeJ(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeJ, self).__init__(**kwargs)
		self.let = 'J'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaJ.png'
		cidade_atual = 'J'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaJ.png'


class CidadeK(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeK, self).__init__(**kwargs)
		self.let = 'K'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaK.png'
		cidade_atual = 'K'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaK.png'


class CidadeL(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeL, self).__init__(**kwargs)
		self.let = 'L'
		Clock.schedule_interval(self.change_state, 0.1)

	def on_press(self):
		global cidade_atual

		print('clicado')
		self.source = 'bolas/bolavermelhaL.png'
		cidade_atual = 'L'

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaL.png'


class CidadeM(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(CidadeM, self).__init__(**kwargs)
		self.let = 'M'

	def on_press(self):
		global cidade_atual

		print('clicado')

	def change_state(self, dt):
		if cidade_atual != self.let:
			self.source = 'bolas/bolapretaM.png'
