# sel points smooth False.py

"""
Select not smooth points in font selected glyphs.
Later you can make them smooth with another complementary script
"""

f = CurrentFont()

for gname in f.selection:
    print "%s : selected all not smooth points" % gname
    g = f[gname]
    for con in g:
        for p in con:
            if p.smooth is False:
                p.selected = True