# glyphs with countours only.py

font = CurrentFont()
for glyph in font:
    if len(glyph.contours) and not len(glyph.components):
        glyph.selected = True
        
print 'selected glyphs with contours'