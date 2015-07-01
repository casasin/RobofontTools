# unselectGlyphsWithExtension.py

f = CurrentFont()

for gname in f.selection:
    if '.' in gname:
        f[gname].selected = 0
