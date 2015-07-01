# deselectAllContours.py

"""
Deselects all contours from selected glyphs in font window
"""

font = CurrentFont()

for gname in font.selection:
    glyph = font[gname]
    for contour in glyph:
        contour.selected = 0

font.update()

print 'Done!\n\t--Deselected all contours in font.selection'
