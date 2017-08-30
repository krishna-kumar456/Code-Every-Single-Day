""" Note pad like editor.
"""

from appJar import gui

def openButtonClick(btnName):
	""" Invoker function that is called whenever a button is clicked.
	"""
	print(btnName)
	app.openBox(title=None, dirName=None, fileTypes=None, asFile=False)

def saveButtonClick(btnName):
	""" Invoker function that is called whenever a button is clicked.
	"""

	print(btnName)



if __name__ == '__main__':

	menu = ['Open', 'Save']

	menuClickFunctions = [openButtonClick, saveButtonClick]
	app = gui()
	app.addToolbar(menu, menuClickFunctions)
	app.addScrolledTextArea('text')
	app.go()
