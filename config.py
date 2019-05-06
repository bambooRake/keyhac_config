from keyhac import *
from pprint import pprint
from pyauto import *

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
	
	keymap.ShellExecuteCommand( None, r"C:\\Users\dazs.DESKTOP-PAUGMTC\\.config\\AutoHotKey\\AutoHotkey.exe", "", "" )()