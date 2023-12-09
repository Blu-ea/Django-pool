from elem import Elem, Text

class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('html', attr, content, 'double')
class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('head', attr, content, 'double')
class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('body', attr, content, 'double')


class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('title', attr, content, 'double')



class Meta(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('meta', attr, content, 'simple')
class Img(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('img', attr, content, 'simple')


class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('table', attr, content, 'double')
class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('th', attr, content, 'double')
class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('tr', attr, content, 'double')
class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('td', attr, content, 'double')


class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('ul', attr, content, 'double')
class Ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('ol', attr, content, 'double')
class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('li', attr, content, 'double')


class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('h1', attr, content, 'double')
class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('h2', attr, content, 'double')


class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('p', attr, content, 'double')


class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('div', attr, content, 'double')


class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('span', attr, content, 'double')


class Hr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('hr', attr, content, 'simple')
class Br(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('br', attr, content, 'double')

if  __name__ == '__main__':
	print (Html([Head(), Body()]))

	print ('======')

	print (\
	Html([
		Head([
			Title('"Hello ground!"')
		]),
		Body([
			H1(['"Ho no, not again!"']),
			Img(attr= {"src":"http://i.imgur.com/pfp3T.jpg"})
					
		])
		])
	)
	html = Elem(tag="html", content=[
			Elem(tag="head", content=Elem(tag="title", content=Text("Hello ground!"))),
			Elem(tag="body", content=[
				Elem(tag="h1", content=Text("Hgit o no, not again!")),
				Elem(tag="img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple'),
			])
	])
	html = Elem(tag="html", content=[
		Elem(tag='head', content=Text("je suis la head")),
		Elem(tag='body', content=Text("je suis le body"))
	])

	html = (
		Html([
			Head([
				Title("Je suis le title :D")
			]),
			Body([
				Div([
					H1("Ho Yeaaahhh Ca fonctionne d'un feu de dieux !!"),
					Img(attr={"src":"https://tenor.com/view/lethal-company-lethal-company-quota-slap-gif-6977915187214085433"}),
				]),
				Div(),
				Div([
					
				])
			])
		])
	)