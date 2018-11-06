"""
## Assignments #1
- Arun
"""
import re
from collections import Counter

# First (most active user in Chat)
def mostActiveUser(cFile):
    '''
    returns list of top 3 active users in the chat
    
    input: file
    output: list
    '''
    with open(cFile) as fh:
        rl = re.findall("<(.+?)>:", fh.read())
        top3 = ([i for i,_ in Counter(rl).most_common(3)])
        return top3
        

if __name__ == "__main__":
    
    top3 = mostActiveUser("chats.txt")
    print(top3)        