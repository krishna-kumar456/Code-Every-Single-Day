""" Note pad like editor.
"""

from appJar import gui

def buttonClick(btnName):
	""" Invoker function that is called whenever a button is clicked.
	"""
	print(btnName + "was clicked!")


if __name__ == '__main__':

	app = gui()
	app.addButton("File", buttonClick)
	app.addScrolledTextArea('text')
	app.go()
