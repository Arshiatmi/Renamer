import os

path = input("Please Enter Path Of The Program : ( Default Is Here -> Rename.exe )").encode('utf-8')
if not path:
    path = os.getcwd().encode('utf-8')
    path += "\\Renamer.exe".encode('utf-8')

if not str(path).endswith("Renamer.exe'"):
    print("Please Enter A Path With 'Renamer.exe' At The End.")

path = path + r" \"--path\" \"%V".encode('utf-8')
path = r"\"".encode('utf-8') + path + r"\"".encode('utf-8')
path = "\"".encode('utf-8') + path + "\"".encode('utf-8')
path = str(path)[2:][:-1]

lines = ["Windows Registry Editor Version 5.00\n"]
lines.append("\n[HKEY_CLASSES_ROOT\Directory\Background\shell\Renamer]\n")
lines.append("\"MUIVerb\"=\"Renamer\"\n")
lines.append("\n[HKEY_CLASSES_ROOT\Directory\Background\shell\Renamer\command]\n")
lines.append(f"@={path}\n")
f = open("file.reg","w")
f.writelines(lines)
f.close()

os.system(r".\file.reg")
os.remove(r".\file.reg")