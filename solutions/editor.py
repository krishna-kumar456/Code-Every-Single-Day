""" Note pad like editor.
"""

from appJar import gui

def openButtonClick(btnName):
	""" Invoker function that is called whenever a button is clicked.
	"""
	print(btnName)
	fileName = app.openBox(title=None, dirName=None, fileTypes=None,
							asFile=False)
	print(fileName)
	with open(fileName, 'r') as f:
		title = 'text'
		app.setTextArea(title, f.readlines(), callFunction=True)


def saveButtonClick(btnName):
	""" Invoker function that is called whenever a button is clicked.
	"""

	print(btnName)
	saveFile = app.saveBox(title=None, fileName=None, dirName=None, fileExt=".txt", fileTypes=None, asFile=None)
	with open(saveFile, 'w') as f:
		title = 'text'
		f.write(app.getTextArea(title))


if __name__ == '__main__':

	menu = ['Open', 'Save']

	menuClickFunctions = [openButtonClick, saveButtonClick]
	app = gui()
	app.addToolbar(menu, menuClickFunctions)
	app.addScrolledTextArea('text')
	app.go()
