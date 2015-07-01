# -*- coding: utf-8 -*-

# test ignore
"""
Opens a new SpaceCenter with a text combo to walk through kerning pairs with up and down arrow keys.

Uses the same values than MetricsMachine, the best kerning tool ever (http://tools.typesupply.com/metricsmachine.html):
left/right arrow:       ± 5
alt-left/right arrow:   ± 1
shift-left/right arrow: ± 10

Useful for checking your kerning in multiline text on screen for minor fixes.
"""
# by joancarles casasin
# joanca@casasin.com

# TODO: use custom strings

from mojo.events import addObserver, removeObserver
from mojo.UI import OpenSpaceCenter

from vanilla.dialogs import message


class SpaceCenterKerning(object):

    """class for SpaceCenterKerning"""

    def __init__(self):

        self.font = CurrentFont()
        self.spaceCenter = None
        if self.font:
            addObserver(self, 'SpaceCenterObserver', 'spaceCenterDidOpen')
            self.spaceCenter = OpenSpaceCenter(self.font, newWindow=True)

            # addObserver(self, None, 'spaceCenterDraw')
            addObserver(self, 'pressedKey', 'spaceCenterKeyDown')
            addObserver(self, 'closeSpaceCenter', 'spaceCenterWillClose')

            # get kerning from CurrentFont and build text list
            self.pairsTextCheck = []
            self.kKeys = self.getKerningPairsRef(self.font)
            # get reference pairs for flipping
            self.refPairs = [pair[0] for pair in self.kKeys]

            for key, gkey in self.kKeys:
                self.pairsTextCheck.append(self.returnPattern(key))

            # index of text
            self.i = 0
            self.maxi = len(self.kKeys)

            self.spaceCenter.set(self.pairsTextCheck[self.i])

        else:
            message('You need to open a font first!')

    def SpaceCenterObserver(self, info):
        if self.spaceCenter:
            self.spaceCenter.set(self.pairsTextCheck[self.i])
            self.updateSpaceCenter()

    def pressedKey(self, info):
        event = info['event']
        pair = self.kKeys[self.i][1]
        keyCode = event.keyCode()

        # modifier key? alt, shift, None
        if event.modifierFlags() == 11010336:
            kIncrement = 1
        elif event.modifierFlags() == 10617090:
            kIncrement = 5
        else:
            kIncrement = 10

        # down, up, left, right keyCodes
        if keyCode == 125:
            self.i += 1
        elif keyCode == 126:
            self.i -= 1
        elif keyCode == 123:
            self.font.kerning[pair] -= kIncrement
        elif keyCode == 124:
            self.font.kerning[pair] += kIncrement
        # flip pair: command-shift-f
        elif event.modifierFlags() == 1179914 and keyCode == 3:
            # print 'command-shift-f hit!'
            refPair = self.kKeys[self.i][0]
            flippedPair = refPair[1], refPair[0]
            if flippedPair in self.refPairs:
                self.i = self.refPairs.index(flippedPair)
            else:
                print 'Flipped pair (%s, %s) has no kern value' % refPair

        # reset if self.i is out of range
        if self.i == self.maxi or self.i == -self.maxi:
            self.i = 0

        self.spaceCenter.set(self.pairsTextCheck[self.i])

    def getKerningPairsRef(self, font):
        """use only the main glyph from kerning group and keep the reference"""
        kerningRef = font.kerning.keys()[:]

        for k in kerningRef:
            left, right = k

            if left in font.groups:
                groupGlyphs = font.groups[left]
                groupGlyphs.sort()
                # get first glyphname in the group
                leftRef = groupGlyphs[0]
            else:
                leftRef = left

            if right in font.groups:
                groupGlyphs = font.groups[right]
                groupGlyphs.sort()
                # get first glyphname in the group
                rightRef = groupGlyphs[0]
            else:
                rightRef = right

            i = kerningRef.index(k)
            kerningRef[i] = (leftRef, rightRef), (left, right)

        kerningRef.sort()
        return kerningRef

    def returnPattern(self, pair):
        """returns the pattern for each kerning pair for its use in the SpaceCenter"""
        left, right = pair
        pattern = 'H/O/H/%s/%s/H/O/H/\\n/H/H/H/%s/%s/H/H/H/\\n/O/O/O/%s/%s/o/o/o/\\n/X/H/X/%s/%s/x/o/x' % (
            left, right, left, right, left, right, left, right,)
        return pattern

    def closeSpaceCenter(self, info):
        """remove Observers when closing the custom SpaceCenter"""
        removeObserver(self, 'spaceCenterDidOpen')
        # removeObserver(self, 'spaceCenterDraw')
        removeObserver(self, 'spaceCenterWillClose')
        removeObserver(self, 'spaceCenterKeyDown')

if __name__ == '__main__':
    SpaceCenterKerning()
