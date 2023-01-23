# Expressions (i) for Iterm(i) in Iterable(rang(100) if condition (i%2==0) if Condition (i%10==0) )

a = [i for i in range(100) if i % 2 == 0 if i % 10 == 0]
print(a)

# Expressions (i) for Iterm(i) else condition("not yash") for condition (i) in Condition(name)
name = ["yash", 'Yash', 'yash', 'Yash']
l = [i if i == "yash" else "not yash" for i in name]
print(l)