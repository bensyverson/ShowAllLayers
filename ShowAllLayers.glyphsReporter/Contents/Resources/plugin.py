# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class ShowAllLayers(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({'en': u'All Layers', 'de': u'Alle Schichten anzeigen'})
		self.keyboardShortcut = '`'
		self.keyboardShortcutModifier = NSCommandKeyMask
		
	def foreground(self, layer):
		NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.5, 0.5, 0.5, 0.2 ).set()
		for aLayer in layer.parent.layers:
			aLayer.completeBezierPath.fill()
