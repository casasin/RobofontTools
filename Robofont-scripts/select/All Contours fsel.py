# selectAllContours.py

"""
Selects all the contours from selected glyphs in font window
"""

font = CurrentFont()

for gname in font.selection:
    glyph = font[gname]
    for contour in glyph:
        contour.selected = 1

font.update()

print 'Done!\n\t--Selected all contours in font.selection'
