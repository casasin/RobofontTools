# toggleSelectedGlyphs.py

"""
Toggles selected glyphs in font window
"""

font = CurrentFont()

for glyph in font:
    if glyph.selected:
        glyph.selected = False
    else:
        glyph.selected = True

font.update()

print 'Done!\n\tToggled font.selection'
