from collections import deque
from threading import Thread
import time

from hslog.parser import LogParser


class LiveLogParser(LogParser):
    
    def __init__(self, filepath):
        super(LiveLogParser, self).__init__()
        self.running = False
        self.filepath = filepath
        self.lines_deque = deque([])

    def flask_endpoint(self, line):
        '''
            # used with run-server.sh
            # can be used instead of file_worker
            nohup python server/server.py >/dev/null 2>&1 &
            sleep 1
            echo "running tail > flask server"
            tail /tmp/hearthstone-redirected.log --follow | python server/proxy.py
        '''
        self.lines_deque.append(line)
    
    def file_worker(self):
        lines_read = 0
        file = open(self.filepath, 'r')
        while self.running:    
            line = file.readline()
            if line:
                lines_read += 1
                if not (lines_read % 100): print(lines_read)
                self.lines_deque.append(line)
            else:
                time.sleep(0.2)
        
    def parse_worker(self):
        while self.running:
            if len(self.lines_deque):
                line = self.lines_deque.popleft()
                self.read_line(line)
            else:
                time.sleep(0.2)
    
    def start_file_worker(self):
        file_thread = Thread(target=self.file_worker)
        file_thread.setDaemon(True)
        file_thread.start()
    
    def start_parse_worker(self):
        parse_thread = Thread(target=self.parse_worker)
        parse_thread.setDaemon(True)
        parse_thread.start()
    
    def start(self):
        self.running = True
        self.start_file_worker()
        self.start_parse_worker()
            
    def stop(self):
        self.running = False