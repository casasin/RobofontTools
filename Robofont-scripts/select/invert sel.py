# invertFontSelection.py

"""
Inverts selection in the current font
"""

for glyph in CurrentFont():
    if glyph.selected:
        glyph.selected = False
    else:
        glyph.selected = True
