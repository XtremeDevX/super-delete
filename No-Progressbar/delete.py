from subprocess import Popen, PIPE
from halo import Halo
import time
import sys

file_path = sys.argv[1]

with Halo(text=rf'Deleting \"{file_path}\" > Null ', color='green', text_color='cyan', spinner='dots') as h:
    if file_path:
        proc = Popen(rf'powershell -c $fso = New-Object -ComObject scripting.filesystemobject;$fso.DeleteFolder("{file_path}", $true);'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        output, err = proc.communicate()
        if proc.returncode == 0:
            h.succeed()            
        else:
            h.fail()
            print(err.decode('utf-8'))
            time.sleep(5)
