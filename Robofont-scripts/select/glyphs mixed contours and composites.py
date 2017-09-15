# glyphs with countours only.py

font = CurrentFont()
font.selection = []
for glyph in font:
    if len(glyph.contours) > 0 and len(glyph.components) > 0:
        glyph.selected = True
        
print 'selected glyphs with contours and composites'