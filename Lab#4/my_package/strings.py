def integer(string):
    if string.isdigit()==True:
        return list(map(lambda x: int(x), string))
    return "Error"

