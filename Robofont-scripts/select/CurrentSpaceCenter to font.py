"""
    select all glyphs from the current space center in the font window
"""

from mojo.UI import CurrentSpaceCenter


font = CurrentFont()
sc = CurrentSpaceCenter()
font.selection = sc.get()
