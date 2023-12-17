translate = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "th3ree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "ei8ght",
        "nine": "n9ine"}

def convert(s):
    s = s.strip()
    for k, v in translate.items():
        s = s.replace(k, str(v))
    return s

f = open("input.txt")
lines = [[c for c in convert(line) if c.isdigit()] for line in f.readlines()]
print(sum(10*int(line[0])+int(line[-1]) for line in lines))
