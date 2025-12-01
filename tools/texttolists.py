# Reads a text input and returns separated values
# Returns a list of lists

###########################

def to2dLists(text, group="\n", item=","):

    # Split text into groups, split groups into items
    list = [group.split(str(item)) for group in text.split(str(group))]
        
    # return list of lists
    return list

def toList(text, group="\n"):
    
    return text.split(str(group))
        
########### EOF ############