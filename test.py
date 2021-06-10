
2
3
4
5
6
7
8
9
10
11
12
13
14
15
 
def one():
    return "one"
 
def two():
    return "two"
 
def test(x):
    switcher = {
        1: one(),
        2: two()
    }
    return switcher.get(x, "nothing")
 
print(test(2))