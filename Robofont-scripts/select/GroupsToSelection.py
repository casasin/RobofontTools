# GroupsToSelection.py
# -*- coding: utf-8 -*-

# Joancarles Casasin
# joanca@casasin.com

# This script was developed for Josep Patau (Tipo Pepel)

"""
Select groups and select them in the main font window.

Double clicking in one group name in the list will print the group items in the Output window
"""

from vanilla import *
from vanilla.dialogs import message
from mojo.events import addObserver, removeObserver

from lib.tools.misc import NSColorToRgba, NSColor


class GroupsToSelection(object):

    def __init__(self):

        self.font = CurrentFont()
        self.mark = 0

        if not self.font:
            message('Open a font first!')
            return
        # window and UI
        self.w = Window((250, 500), "Groups To Selection",
                        minSize=(250, 200),
                        maxSize=(250, 1000))
        # font groups
        self.w.groupsList = List((10, 10, -10, -70),
                                 [],
                                 columnDescriptions=[
                                     {'title': 'sel', 'editable': True, 'cell': CheckBoxListCell(), 'width': 20},
                                     {'title': 'Group Name'}],
                                 doubleClickCallback=self.doubleClickCallback
                                 )
        self.buildGroupsList(self.font)
        # select/unselect all glyphs in font
        self.w.resetButton = Button((10, -60, -120, 20),
                                    '(un)Select All',
                                    sizeStyle='mini',
                                    callback=self.selectAllCallback)
        # mark and color selection
        self.w.markCheckbox = CheckBox((160, -60, -10, 20),
                                       'mark',
                                       value=self.mark,
                                       sizeStyle='small',
                                       callback=self.markCallback)
        self.w.markColor = ColorWell((210, -60, -10, 20))
        self.w.markColor.enable(False)
        self.w.markColor.set(NSColor.redColor())
        # select
        self.w.makeSelection = Button((10, -30, -10, 20),
                                      "Make Selection",
                                      # minSize=(150, 150),
                                      callback=self.makeSelectionCallback)
        # removeObserver if the window closes
        self.w.bind("close", self.windowCloseCallback)
        self.w.open()

        addObserver(self, "updateCurrentFontCallback", "fontBecameCurrent")

    def updateCurrentFontCallback(self, sender):
        self.font = CurrentFont()
        self.buildGroupsList(self.font)

    def buildGroupsList(self, font):
        """
        Creates list of dictionaries with group names and sets the list with it
        """
        self.fontGroups = []
        if font:
            for group in self.font.groups.keys():
                self.fontGroups.append({'Group Name': group, 'sel': False})
        self.w.groupsList.set(self.fontGroups)

    def doubleClickCallback(self, sender):
        """
        Double clicking the list will print in the Output Window the selected group items
        """
        i = sender.getSelection()[0]
        group = sender.get()[i]
        groupName = group['Group Name']
        print
        print '%s : %s' % (groupName, self.font.groups[groupName])

    def selectAllCallback(self, sender):
        """
        Select/Unselect all the checkboxes for quick dealing of many groups or cleaning up
        """
        self.fontGroups = self.w.groupsList.get()
        # how many True?
        n = sum(1 for d in self.fontGroups if d.get('sel') is True)

        sel = False
        if n == 0:
            sel = True

        for group in self.fontGroups:
            group['sel'] = sel

        self.w.groupsList.set(self.fontGroups)

    def markCallback(self, sender):
        """
        enables Colorwell for selecting mark color
        """
        self.w.markColor.enable(self.mark)

    def makeSelectionCallback(self, sender):
        """
        Sets selection of current font window to glyphs in checked groups
        """
        self.fontGroups = self.w.groupsList.get()
        selGroups = [group['Group Name'] for group in self.fontGroups if group['sel'] is True]

        if self.font:
            self.font.selection = []
            glyphsToSelect = []
            for groupName in selGroups:
                glyphsToSelect += self.font.groups.get(groupName)

            self.font.selection = glyphsToSelect

            if self.w.markCheckbox.get():
                markColor = NSColorToRgba(self.w.markColor.get())
                for gname in glyphsToSelect:
                    self.font[gname].mark = markColor
                    # self.font[gname].mark(markColor)

    def windowCloseCallback(self, sender):
        removeObserver(self, "fontBecameCurrent")
        super(Observer, self).windowCloseCallback(sender)


GroupsToSelection()
