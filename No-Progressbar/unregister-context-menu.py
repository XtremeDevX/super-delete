import winreg

winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Directory\shell\TurboDelete\command')
winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Directory\shell\TurboDelete')