from os import path
import sys
import os
from datetime import datetime

class LoopPath:
    base=None;
    searchStr=""
    List=[]
    PrintList=False
    PrintDetails=False
    Write=False
    Precise=False
    File=True
    Folder=False

    def __init__(self,__base,folder,file,search,list=False,details=False,write=False,precise=False):
        self.base=__base
        self.searchStr=search
        self.PrintList=list
        self.PrintDetails=details
        self.Write=write
        self.Precise=precise
        self.File=file
        self.Folder=folder

    def start(self):
            i = 0
            for r,d, f in os.walk(self.base):
                if self.Folder:
                    for dir in d:
                        i+=1
                        Find = self.FindStringInDirname(dir,path.join(r,dir))
                        if Find != False:
                            if self.PrintList:
                                if self.PrintDetails:
                                    pos=Find[1]
                                    if not isinstance(Find[1],str):
                                        pos=([char for char in (Find[0]+"".lower())])[Find[1]]
                                    print(Find[0]," find ",self.searchStr," in ",pos," at ",Find[3])
                                else:
                                    print(dir)
                            if self.Write:
                                pos=Find[1]
                                if not isinstance(Find[1],str):
                                    pos=([char for char in (Find[0]+"".lower())])[Find[1]]
                                data = "(folder) {2} = [{0}] => {1} in \"{3}\"".format(Find[0],pos,Find[2],Find[3])
                                with open("./{0}.log".format(datetime.date(datetime.now())), "a+") as f:
                                    f.write(data+"\n")
                            self.List.append(Find)
                else:
                    for file in f:
                        i+=1
                        fp = os.path.join(r, file)
                        Find = False
                    
                        if self.File and not path.isdir(fp):
                            Find = self.FindStringInDirname(file,fp)
                        if Find != False:
                            if self.PrintList:
                                if self.PrintDetails:
                                    pos=Find[1]
                                    if not isinstance(Find[1],str):
                                        pos=([char for char in (Find[0]+"".lower())])[Find[1]]
                                    print(Find[0]," find ",self.searchStr," in ",pos," at ",Find[3])
                                else:
                                    print(fp)
                            if self.Write:
                                pos=Find[1]
                                if not isinstance(Find[1],str):
                                    pos=([char for char in (Find[0]+"".lower())])[Find[1]]
                                data = "(file) {2} = [{0}] => {1} in \"{3}\"".format(Find[0],pos,Find[2],Find[3])
                                with open("./{0}.log".format(datetime.date(datetime.now())), "a+") as f:
                                    f.write(data+"\n")
                            self.List.append(Find)      
            return [i,self.List]

    def FindStringInDirname(self,name,filePath):
        real=name
        name = name.lower()
        if self.Precise:
            if self.searchStr in name:
                return [real,self.searchStr,self.searchStr,filePath]
            else:
                return False
        else:
            if name.find(self.searchStr,0,len(name)) > -1:
                return [real,name.find(self.searchStr,0,len(name)),self.searchStr,filePath]
            else:
                return False

def BackDir(dir):
    return path.dirname(dir)

def FindBase(__dirname):
    dir = BackDir(__dirname)
    last = None
    while True:
        last = dir
        dir = BackDir(dir)
        if last==dir:
            break
    return dir

def main(argv):
    __dirname = os.path.dirname(os.path.realpath(__file__))
    __base = FindBase(__dirname)
    list=False
    write=False
    details=False
    precise=False
    folder=False
    file=True
    args = ["--list","--details","--write","--dir","--precise","--file","--folder"]
    for arg in argv:
        if arg == "--list":
            list=True
        if arg == "--details":
            list=True
            details=True
        if arg == "--write":
            write=True
        if arg == "--dir":
            __base=__dirname
        if arg == "--precise":
            precise=True
        if arg == "--file":
            file=True
            folder=False
        if arg == "--folder":
            folder=True
            file=False
    for arg in argv:
        if not arg in args:
            pathLoop = LoopPath(__base,folder,file,arg,list,details,write,precise)
            end=pathLoop.start()
            print("File count: ",end[0])
            print(pathLoop.List)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])