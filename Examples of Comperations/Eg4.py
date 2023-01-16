l = []
for x in [10, 20, 30]:
    for y in [100, 200, 300]:
        l.append(x + y)
print(l)

# Expression(x+y) For Loop( x in (10,20,30) ) For Loop (y in (100,200,300))
l = [x + y for x in (10, 20, 30) for y in (100, 200, 300)]
print(l)
