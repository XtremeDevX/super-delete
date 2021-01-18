import winreg
import os

appdata_dir = os.getenv('APPDATA') + r'\Super Delete\bin\delete.exe'
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete')
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete\command')

delete_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(delete_key, '', 0, winreg.REG_SZ, 'Super Delete')
delete_key.Close()


command_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete\command', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, Rf'"{appdata_dir}" "%1"')
command_key.Close()