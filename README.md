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
```
- take a look at example.py

```
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
- liveParser will pick up on games in the log file
```
In [6]: liveParser.games
Out[6]: 
[<hslog.packets.PacketTree at 0x7fd47a343860>,
 <hslog.packets.PacketTree at 0x7fd479991128>,
 <hslog.packets.PacketTree at 0x7fd4797ab6a0>,
 <hslog.packets.PacketTree at 0x7fd479632d30>,
 <hslog.packets.PacketTree at 0x7fd478b4dd30>,
 <hslog.packets.PacketTree at 0x7fd4795e75f8>,
 <hslog.packets.PacketTree at 0x7fd478c51a58>,
 <hslog.packets.PacketTree at 0x7fd478a91198>]

```
- you can select the last/current game and play around
```
In [7]: g = liveParser.games[-1] # select the last/current game

37000
In [8]: ex = g.export()

37100
37200
In [9]: ex
Out[9]: <hslog.export.EntityTreeExporter at 0x7fd47a538fd0>

37300
37400
In [10]: ex.game.entities
Out[10]: 
[Game(id=1, players=[Player(id=2, name='PlayerName#1607'), Player(id=3, name='PlayerName#1849')]),
 Player(id=2, name='PlayerName#1607'),
 Player(id=3, name='PlayerName#1849'),
 Card(id=4, card_id='GIL_526'),
 Card(id=5, card_id=None),
 Card(id=6, card_id=None),
 Card(id=7, card_id=None),
 Card(id=8, card_id='EX1_043'),
 Card(id=9, card_id='GIL_601'),
 Card(id=10, card_id=None),
 Card(id=11, card_id=None),
 Card(id=12, card_id=None),
 Card(id=13, card_id='UNG_029'),
 Card(id=14, card_id=None),
 Card(id=15, card_id='LOOT_528'),
 Card(id=16, card_id='GIL_190'),
 Card(id=17, card_id=None),
 Card(id=18, card_id='GIL_661'),
 Card(id=19, card_id=None),
 Card(id=20, card_id='CS2_234'),
 Card(id=21, card_id=None),
 Card(id=22, card_id=None),
 Card(id=23, card_id=None),
 Card(id=24, card_id=None),
 Card(id=25, card_id=None),
 Card(id=26, card_id='ICC_027'),
 Card(id=27, card_id=None),
 Card(id=28, card_id=None),
 Card(id=29, card_id=None),
 Card(id=30, card_id=None),
 Card(id=31, card_id='EX1_572'),
 Card(id=32, card_id=None),
 Card(id=33, card_id='UNG_029'),
 Card(id=34, card_id=None),
 Card(id=35, card_id='LOOT_218'),
 Card(id=36, card_id=None),
 Card(id=37, card_id='UNG_816'),
 Card(id=38, card_id=None),
 Card(id=39, card_id=None),
 Card(id=40, card_id=None),
 Card(id=41, card_id=None),
 Card(id=42, card_id=None),
 Card(id=43, card_id=None),
 Card(id=44, card_id=None),
 Card(id=45, card_id=None),
 Card(id=46, card_id='GIL_614'),
 Card(id=47, card_id=None),
 Card(id=48, card_id=None),
 Card(id=49, card_id=None),
 Card(id=50, card_id=None),
 Card(id=51, card_id='ICC_083'),
 Card(id=52, card_id=None),
 Card(id=53, card_id='UNG_075'),
 Card(id=54, card_id=None),
 Card(id=55, card_id=None),
 Card(id=56, card_id='UNG_928'),
 Card(id=57, card_id=None),
 Card(id=58, card_id=None),
 Card(id=59, card_id=None),
 Card(id=60, card_id=None),
 Card(id=61, card_id='UNG_809'),
 Card(id=62, card_id='GIL_826'),
 Card(id=63, card_id=None),
 Card(id=64, card_id='HERO_09'),
 Card(id=65, card_id='CS1h_001'),
 Card(id=66, card_id='HERO_08a'),
 Card(id=67, card_id='CS2_034_H1'),
 Card(id=68, card_id='GAME_005'),
 Card(id=69, card_id='GIL_826'),
 Card(id=70, card_id='CS2_034_H1_AT_132'),
 Card(id=71, card_id=None),
 Card(id=72, card_id='UNG_029'),
 Card(id=73, card_id='CS2_004'),
 Card(id=74, card_id='EX1_626'),
 Card(id=75, card_id='GIL_601e'),
 Card(id=76, card_id='EX1_043e'),
 Card(id=77, card_id='CS2_234'),
 Card(id=78, card_id='CS2_004'),
 Card(id=79, card_id='DS1_233'),
 Card(id=80, card_id=None),
 Card(id=81, card_id=None),
 Card(id=82, card_id=None),
 Card(id=83, card_id='GIL_526e'),
 Card(id=84, card_id='GIL_614e2'),
 Card(id=85, card_id='GIL_614e1')]
 ```
- stop liveParser
 ```
 In [11]: liveParser.stop()
```
