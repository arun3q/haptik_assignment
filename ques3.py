"""
## Assignment #3
- Arun
"""
# Third (check whether a given string is made from the combinations of a list of strings)
def isCombination(string, lst):
    '''
    checks whether a given string is made from the combinations of the given list of strings
    
    input: str, list
    output: bool
    '''
    tempStr = string
    for i in lst:
        if len(tempStr)>0:
            if i in tempStr:
                tempStr = tempStr.replace(i," ").strip()
    return False if len(tempStr)>0 else True
    


if __name__ == "__main__":
    l1 = ['back','end','front','tree',]
    string1 = 'treetree'   # True
    
    out = isCombination(string1, l1)
    print(out)