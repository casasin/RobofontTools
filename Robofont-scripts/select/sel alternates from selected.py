# sel alternates from selected.py

f = CurrentFont()
xt = '.alt'

fontAlternates = []
for gname in f.selection:
    alternates = [aname for aname in f.keys() if aname.startswith(gname + xt)]
    fontAlternates += alternates
for gname in fontAlternates:
    f[gname].selected = True