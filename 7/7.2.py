testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
immutable = ["tuple", "int",  "float", "bool", "str", "set"]

for i in range(len(testList)):
    if type(testList[i]) not in immutable:
        print("False")
    break
else:
    print("True")
