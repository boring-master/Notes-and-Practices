def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos]) * (pos + 1)
    return sum % tablesize