Just a repo full of experiments related to Hearthstone

# Install Python3.6
Ubuntu 16.04 https://askubuntu.com/a/865569

# Create your virutalenv
```
sudo -H pip install virtualenv
virtualenv -p python3.6 venv-python3.6
source venv-python3.6/bin/activate
```

# Install pip requirements
```
pip install -r pip-requirements.txt
```

# Clone repo
```
git clone https://github.com/dduric/hearthstone-experiments.git
cd hearthstone-experiments
```

# Start liveParser with iPython
```
~/hearthstone-experiments$ ipython
Python 3.6.5 (default, Mar 29 2018, 03:28:50) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: cat example.py
from time import sleep
import traceback

from hslog.liveparser import LiveLogParser


def main():
    try:
        file = '/tmp/hearthstone-redirected.log'
        liveParser = LiveLogParser(file)
        liveParser.start()
        
        while True:
            sleep(1)
            
    except:
        print(traceback.format_exc())
        liveParser.stop()
    
    
if __name__ == "__main__":
    main()

In [2]: from hslog.liveparser import LiveLogParser

In [3]: file = '/tmp/hearthstone-redirected.log'
   ...: liveParser = LiveLogParser(file)
   ...: liveParser.start()
   ...: 
   ...: 

```
