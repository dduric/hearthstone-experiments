import sys
import requests

if __name__ == "__main__":
    for line in sys.stdin:
        requests.post('http://localhost:8000/api/live/', json={'line': line})
