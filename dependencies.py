import pip
import json
try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
     from pip.operations import freeze





import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
    return






# Example
if __name__ == '__main__':
    with open('document.json') as f:
        data = json.load(f)
    a= data['Dependencies']
    print(a)
    for i in a:
        install(i)
        x = freeze.freeze()
        if i not in x:
            print(i)




    #install('argh')
