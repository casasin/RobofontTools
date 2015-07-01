# scriptRunner.py

"""

Run a script in Robofont with a button given its path

Useful if you want to run a script several times and you don't want to navigate the Menu every time.

"""

import os.path

from vanilla import *
from vanilla.dialogs import getFile, message

from lib.scripting.scriptTools import ScriptRunner


class ScriptRunner(object):

    """Script Runner Window"""

    def __init__(self, pathToScript=None):
        # super(ScriptRunner, self).__init__()
        self.pathToScript = pathToScript

        if pathToScript:
            self.scriptName = os.path.basename(self.pathToScript)
        else:
            self.scriptName = 'None'

        # window
        self.w = FloatingWindow((200, 120), 'Script Runner')
        self.w.info = TextBox((10, 10, -10, 19),
                              'Run script: %s' % self.scriptName,
                              sizeStyle='mini')
        self.w.changeScript = Button((10, 30, 110, 19),
                                     'Select',
                                     sizeStyle='small',
                                     callback=self.selectScriptCallback)
        self.w.sepLine = HorizontalLine((10, 65, -10, 1))
        self.w.runnerButton = Button((10, -38, -10, 20),
                                     'Run',
                                     callback=self.runCallback)
        # 'r' shortcut for running the script (should work if it's not a FloatingWindow)
        # self.w.runnerButton.bind('r', ['option'])
        # self.w.setDefaultButton(self.w.runnerButton)
        self.w.open()

    def runCallback(self, sender):
        """Run the script button callback"""
        if self.pathToScript:
            ScriptRunner(path=self.pathToScript,
                         text=None,
                         stdout=None,
                         stderr=None,
                         namespace=None,
                         threaded=False)
        else:
            message('Sorry, you need to select a script to run first')

    def selectScriptCallback(self, sender):
        """Select the script to run callback"""
        getFilePath = getFile('Select new script:')
        if getFilePath is not None:
            newScriptPath = getFilePath[0]
            self.pathToScript = newScriptPath
            self.scriptName = os.path.basename(self.pathToScript)
            self.w.info.set('Run script: %s' % self.scriptName)


if __name__ == '__main__':
    ScriptRunner()
