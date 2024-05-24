def countX(text):
    
    if len(text) == 0:
        return 0
    
    elif text[0] == 'x':
        return 1 + countX(text[1:])
    
    else:
        return countX(text[1:])