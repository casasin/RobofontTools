def selectMark(font):
    """
    Selects all glyphs in f with the same mark than current selected glyph
    if no marked glyph is selected then it will select ALL marked
    """

    selectedglyph = font.selection[0]
    sourcemark = font[selectedglyph].mark

    if sourcemark:
        for glyph in font:
            if glyph.mark == sourcemark:
                glyph.selected = True
    else:
        print "The source glyph (selected) is not marked.\nIf you want to select all marked use selecteAllMarks(font)"
    font.update()


selectMark(CurrentFont())
