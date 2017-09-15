# selectChangedGlyphs.py

"""
Selects glyphs that have changed since last .ufo saving
"""

font = CurrentFont()

for glyph in font:
    if glyph.changed:
        glyph.selected = True
    else:
        glyph.selected = False

print "Done!\n\t--Selected changed glyphs"
