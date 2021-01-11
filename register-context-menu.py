import winreg
import os

appdata_dir = os.getenv('APPDATA') + r'\SuperDelete\delete.bat'
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete')
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete\command')

delete_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(delete_key, '', 0, winreg.REG_SZ, 'SuperDelete')
delete_key.Close()


command_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, R'Directory\shell\SuperDelete\command', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, Rf'cmd /c "cd %1 && {appdata_dir}"')
command_key.Close()