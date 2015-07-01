# nextmarked to GlyphWindow

from mojo.UI import *


f = CurrentFont()

cgname = CurrentGlyph().name


gnames = []

for gname in f:
    if gname.mark:
        gnames.append(gname.name)

# gnames.sort()

nexti = gnames.index(cgname) + 1
nextg = gnames[nexti]

if CurrentGlyphWindow():
    SetCurrentGlyphByName(nextg)
else:
    OpenGlyphWindow(f[nextg])
