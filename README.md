# FileSearch

> Run CLI


```cmd
py main.py <args>
```
optional parameters:
* --list (print path)
* --write (create log file with data in)
* --dir (in actual directory default is base dir C:\)
* --precise (search only the word you enter)
* --file (only file default true)
* --folder (only  folder default false)
* --details (print inforation about files)

Example
```cmd
py main.py --write --details --precise --folder node_modules search_folder other_search_folder
```

> Lib

* LoopPath
  * __base
  * folder
  * file
  * search
  * list=False
  * details=False 
  * write=False
  * precise=False
* FindBase
  * dir
* BackDir
  * dir

```python
import sys
from main import LoopPath
from main import FindBase
import sys
import os

def main(word):
    list=False
    write=False
    details=False
    precise=False
    folder=False
    file=True
    search = word
    __dirname = os.path.dirname(os.path.realpath(__file__))
    __base = FindBase(__dirname)
    pathLoop = LoopPath(__dirname,folder,file,search,list,details,write,precise)
    end=pathLoop.start()
    print("File count: ",end[0])
    print(pathLoop.List)
    return 0

if __name__ == "__main__" and len(sys.argv[1:]) > 1:
    main(sys.argv[1:][0])
```
