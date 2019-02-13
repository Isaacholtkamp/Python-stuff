def num_char (name):
    numb = len(name)
    numb = numb % 2
    if numb == 1:
        return "odd"
    else:
        return "even"
    

print "The name has a", num_char("Steve"), "amount of characters"
