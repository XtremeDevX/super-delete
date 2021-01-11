import winreg

winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Directory\shell\SuperDelete\command')
winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Directory\shell\SuperDelete')