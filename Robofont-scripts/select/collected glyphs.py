# collected glyphs.py

font = CurrentFont()

gnames = """A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ampersand period comma colon semicolon ellipsis hyphen uni00AD hyphen.case uni00AD.case exclam exclamdown question questiondown quoteleft quoteright quotedblleft quotedblright quotesinglbase quotedblbase guilsinglleft guilsinglright guillemotleft guillemotright guilsinglleft.case guilsinglright.case guillemotleft.case guillemotright.case slash backslash bar doublebar brokenbar endash emdash endash.case emdash.case bullet periodcentered parenleft parenright bracketleft bracketright braceleft braceright parenleft.case parenright.case bracketleft.case bracketright.case braceleft.case braceright.case asterisk dagger daggerdbl section paragraph asciicircum underscore quotesingle quotedbl at copyright registered uni2117 trademark currency Euro dollar cent sterling florin yen ordfeminine ordmasculine numbersign zero one two three four five six seven eight nine"""

glyphNames = gnames.split()

font.selection = []
for gname in glyphNames:
    font[gname].selected = True