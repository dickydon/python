import os
import chardet
#test11111
def dirlist(path, allfile):  
    filelist =  os.listdir(path)  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile
allfile = []
dirlist("D:\\3D_105\\Server\\GameEngine\\",allfile)
for file in allfile:
    f = open(file,'rb')
    data = f.read()
    print(file, chardet.detect(data)["encoding"])
    f.close()
