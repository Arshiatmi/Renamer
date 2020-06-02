import os,sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name',help='The String You Wanted Rename To.')
parser.add_argument('--format',help='The Format You Wanted To Change')
parser.add_argument('--path',help='The Path Of Folder')
parser.add_argument('--delimiter',help='Delimiter Of Name Of File And Suffix.')
parser.add_argument('--mode',help='The Mode. Default Is 1 ( Create Time , Modify Time , Last Access Time )')
dt = parser.parse_args()

if not dt.path:
    dt.path = input("Enter Path : ")

if len(sys.argv) > 1:
    os.chdir(dt.path)

def getExtention(file_name):
    return file_name.split(".")[-1].strip()

def isFile(file_name):
    if len(file_name.split(".")) > 1:
        return True
    return False

paths = ""

if dt.mode:
    if dt.mode == "1":
        paths = sorted(os.listdir(), key=os.path.getctime)
    elif dt.mode == "2":
        paths = sorted(os.listdir(), key=os.path.getmtime)
    elif dt.mode == "3":
        paths = sorted(os.listdir(), key=os.path.getatime)
    else:
        paths = sorted(os.listdir(), key=os.path.getctime)
        x = input("Sorry An Error In Mode ... Default Setted. ( Creation Time )\n Do You Want To Continue ?")
        if x.lower() != "y" or x.lower() != "yes":
            exit(0)
else:
    while True:
        try:
            x = int(input("Enter Mode : ( 1 -> Creation Time / 2 -> Modify Time / 3 -> Last Access Time )"))
            break
        except:
            print("Try Again :(")
    if x == 1:
        paths = sorted(os.listdir(), key=os.path.getctime)
    elif x == 2:
        paths = sorted(os.listdir(), key=os.path.getmtime)
    elif x == 3:
        paths = sorted(os.listdir(), key=os.path.getatime)

exts = set()
all_files = list(paths)
for i in all_files:
    if i == os.path.basename(__file__):
        continue
    if isFile(i):
        exts.add(getExtention(i))
extention = ""
if dt.format:
    extention = dt.format
    if extention not in exts:
        print("Sorry Extention",extention,"Is Incorrect :(")
        exit(1)
else:
    while extention not in exts:
        extention = input(f"Enter A Format {list(exts)} : ")
        if extention not in exts:
            print("Sorry Extention",extention,"Is Incorrect :(")
string = ""
if dt.name:
    string = dt.name
else:
    prompt = False
    while not prompt:
        string = input("Enter String To Change : ")
        prompt_str = input(f"Are You Sure About '{string}' ? (Y/n) ")
        if not prompt_str:
            prompt = True
        else:
            if prompt_str.lower() == "n" or prompt_str.lower().strip() == "no":
                continue
            elif prompt_str.lower().strip() == "y" or prompt_str.lower().strip() == "yes":
                prompt = True
            else:
                print("You Entered An Unknown String, Default Was 'yes' ")
                prompt = True
delimiter = ""
if dt.delimiter:
    delimiter = dt.delimiter
c = 1
for i in all_files:
    if getExtention(i) == extention:
        while os.path.exists(string + delimiter + str(c) + "." + getExtention(i)):
            c += 1
        os.rename(i,string + delimiter + str(c) + "." + getExtention(i))
        c += 1
print("Done :)\n\n")