import os,sys

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

def getExtention(file_name):
    return file_name.split(".")[-1].strip()

def isFile(file_name):
    if len(file_name.split(".")) > 1:
        return True
    return False

paths = sorted(os.listdir(), key=os.path.getctime)

exts = set()
all_files = list(paths)
for i in all_files:
    if i == os.path.basename(__file__):
        continue
    if isFile(i):
        exts.add(getExtention(i))
extention = ""
while extention not in exts:
    extention = input(f"Enter A Format {list(exts)} : ")
    if extention not in exts:
        print("Sorry Extention",extention," Is Incorrect :(")
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
c = 1
for i in all_files:
    if getExtention(i) == extention:
        while os.path.exists(string + str(c) + "." + getExtention(i)):
            c += 1
        os.rename(i,string + str(c) + "." + getExtention(i))
        c += 1
print("Done :)\n\n")
input("Press Any Key To Continue...")