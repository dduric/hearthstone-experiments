import sys
import requests

if __name__ == "__main__":
    for line in sys.stdin:
        requests.post('http://localhost:5000', json={'line': line})
