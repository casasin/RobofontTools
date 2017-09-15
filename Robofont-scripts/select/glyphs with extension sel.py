# glyphs with extension sel.py

from robofab.interface.all.dialogs import AskString

xt = AskString('Type the extension you want glyphs to be selected:')

if xt and '.' not in xt:
    xt = '.' + xt

font = CurrentFont()
glyphsWithExtension = []
for gname in font.keys():
    if xt in gname:
        font[gname].selected = True
        glyphsWithExtension.append(gname)
# print ordered by font.glyphOrder
glyphsWithExtension.sort(key=lambda x : font.glyphOrder.index(x))
print '@{0} = ['.format(xt[1:])
for gname in glyphsWithExtension:
    print gname,
print '];'