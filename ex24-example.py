def testvariable(insertnum):
    object1 = insertnum * 5
    object2 = object1 - 100
    return object1, object2

foo = 70

second, first  = testvariable(foo)

print first
print second
