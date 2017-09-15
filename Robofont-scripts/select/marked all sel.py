# selectAllMarks.py

"""
Selects all marked glyphs in CurrentFont
"""

font = CurrentFont()

for glyph in font:
    if glyph.mark:
        glyph.selected = True
    else:
        glyph.selected = False

font.update()
