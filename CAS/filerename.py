import os

path = r"E:\python_project\194"

for file in os.listdir(path):
    print(file)
    oldname = os.path.join(path,file)
    print(oldname)
    newname =oldname+".jpg"
    print(newname)
    os.rename(oldname,newname)
