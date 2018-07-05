#############################################################  
#author:wanglin  
#date:16.03.2014  
#readme: the script used to find which file include the given  
#        string,which in aimStringList,then list the filename  
#  
#############################################################  
#!/usr/bin/evn python  
import os,sys  
  
#give the string list which want to find  
searchPath='D:\\3D_101\\Server\\GameEngine'  
aimStringList = ['malloc(']  
global boolPrintPath  
global fileNo  
boolPrintPath = False  
fileNo = 1  
notIncludeFolders=['man','bak']  
  
##  
# function getIncludeStringFileName(path): find which file include the given  
# string list,then print them  
##  
def getIncludeStringFileName(path):  
    global boolPrintPath,fileNo  
    boolPrintPath = False  
    fileList = os.listdir(path)  
    for item in fileList:  
        if(os.path.isfile(path+'/'+item)):  
            fdFile = open(path+'/'+item) 
            print( fdFile) 
            fileContent = fdFile.read()  
            for strItem in aimStringList:  
                if strItem in fileContent:  
                    print(str(fileNo) + ' ' * (10-len(str(fileNo)))+item )  
                    fileNo = fileNo + 1  
                    boolPrintPath = True  
                    break  
            fdFile.close()  
    if boolPrintPath == True:  
        print(path + '\n'  ) 
  
    for item in fileList:  
        pathNew = path + '/' + item  
        if(os.path.isdir(pathNew)):  
            needRun=True  
            for itm in notIncludeFolders:  
                if itm in pathNew:  
                    needRun=False  
                    break  
            if needRun==True:  
                getIncludeStringFileName(pathNew)  
  
      
##  
# main()  
#  
if __name__ == '__main__':  
    getIncludeStringFileName(searchPath)