from subprocess import Popen, PIPE
from progress.bar import Bar
from pathlib import Path
import time
import sys
import os

file_path = sys.argv[1]

def rmdir(directory, bar: Bar):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item, b)
        else:
            bar.next()
            try:
                item.unlink()
            except:
                pass
    try:
        directory.rmdir()
    except:
        pass

len = sum([len(files) for r, d, files in os.walk(file_path)])
with Bar(f'Deleting {file_path}', max=len) as b:
    rmdir(sys.argv[1], b)
    if os.path.isdir(file_path):
        proc = Popen(rf'powershell -c $fso = New-Object -ComObject scripting.filesystemobject;$fso.DeleteFolder("{file_path}", $true);'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        output, err = proc.communicate()
        if proc.returncode != 0:
            print(err.decode())
            time.sleep(5)
