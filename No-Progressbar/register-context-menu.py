import winreg
import os

appdata_dir = os.getenv('APPDATA') + r'\Turbo Delete\bin\delete.exe'
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\TurboDelete')
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\TurboDelete\command')

delete_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\TurboDelete', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(delete_key, '', 0, winreg.REG_SZ, 'Turbo Delete')
delete_key.Close()


command_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\TurboDelete\command', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, Rf'"{appdata_dir}" "%1"')
command_key.Close()