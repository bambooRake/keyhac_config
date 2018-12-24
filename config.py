from keyhac import *
from pprint import pprint
from pyauto import *
import pyauto

def configure(keymap):
	keymap.defineModifier( 29, "User0" )
	keymap_global = keymap.defineWindowKeymap()

	#アプリ終了
	keymap_global["U0-Q"] = "D-Alt", "F4", "U-Alt"

	for any in ("", "Shift-", "Ctrl-", "Ctrl-Shift-", "Alt-", "Alt-Shift-", "Alt-Ctrl-", "Alt-Ctrl-Shift-", "Win-", "Win-Shift-", "Win-Ctrl-", "Win-Ctrl-Shift-", "Win-Alt-", "Win-Alt-Shift-", "Win-Alt-Ctrl-", "Win-Alt-Ctrl-Shift-"):

		#移動系
		keymap_global[any + "U0-H"] = any + "Left"
		keymap_global[any + "U0-J"] = any + "Down"
		keymap_global[any + "U0-K"] = any + "Up"
		keymap_global[any + "U0-L"] = any + "Right"
		keymap_global[any + "U0-A"] = any + "Home"
		keymap_global[any + "U0-E"] = any + "End"

		#編集系
		keymap_global[any + "U0-S"] = any + "Enter"
		keymap_global[any + "U0-D"] = any + "Delete"
		keymap_global[any + "U0-X"] = any + "Back"

	def _mouse_util():
		print("Hello World!")
		pyauto.MouseLeftDown(pyauto.Input.getCursorPos()[0], pyauto.Input.getCursorPos()[1])
		pyauto.MouseLeftUp(pyauto.Input.getCursorPos()[0], pyauto.Input.getCursorPos()[1])

	#マウス系
	keymap_global[ "D-U0-F" ] = keymap.MouseButtonDownCommand('left')
	keymap_global[ "U-U0-F" ] = keymap.MouseButtonUpCommand('left')
	keymap_global[ "D-U0-V" ] = keymap.MouseButtonDownCommand('right')
	keymap_global[ "U-U0-V" ] = keymap.MouseButtonUpCommand('right')
	keymap_global[ "D-U0-G" ] = keymap.MouseButtonDownCommand('middle')
	keymap_global[ "U-U0-G" ] = keymap.MouseButtonUpCommand('middle')
	keymap_global[ "U0-4" ] = keymap.MouseWheelCommand(1.0)
	keymap_global[ "U0-R" ] = keymap.MouseWheelCommand(-1.0)
	keymap_global[ "U0-5" ] = keymap.MouseHorizontalWheelCommand(-1.0)
	keymap_global[ "U0-T" ] = keymap.MouseHorizontalWheelCommand(1.0)
	keymap_global["F1"] = _mouse_util


