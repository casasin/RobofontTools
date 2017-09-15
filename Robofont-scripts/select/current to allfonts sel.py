# selectionToAllFonts.py

f = CurrentFont()
for afont in AllFonts()[1:]:
    selectedInFont = [gname for gname in f.selection if gname in afont.keys()]
    afont.selection = selectedInFont
    if selectedInFont != f.selection:
        print '{0} misses some glyph from CurrentFont selection'.format(afont)