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
