import string

pairs = ["aA", "Aa", "bB", "Bb", "cC", "Cc", "dD", "Dd", "eE",
         "Ee", "fF", "Ff", "gG", "Gg", "hH", "Hh", "iI", "Ii",
         "jJ", "Jj", "kK", "Kk", "lL", "Ll", "mM", "Mm", "nN",
         "Nn", "oO", "Oo", "pP", "Pp", "qQ", "Qq", "rR", "Rr",
         "sS", "Ss", "tT", "Tt", "uU", "Uu", "vV", "Vv", "wW",
         "Ww", "xX", "Xx", "yY", "Yy", "zZ", "Zz"]

def eliminate_pairs(string):
    eliminated = True
    while eliminated == True:
        eliminated = False
        for pair in pairs:
            if pair in string:
                eliminated = True
                string = string.replace(pair, "")

    return string


with open("input.txt", "r") as file:
    print len(eliminate_pairs(file.read()))


with open("input.txt", "r") as file:
    inpt = file.read()
    min = 9202
    min_char = ""
    for char in list(string.ascii_lowercase):
        temp_inpt = inpt.replace(char, "")
        temp_inpt = temp_inpt.replace(char.upper(), "")
        size = len(eliminate_pairs(temp_inpt)) - 1
        if size < min:
            min = size
            min_char = char


    print min_char
    print min
