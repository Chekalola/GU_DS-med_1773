def fact(n):
    cur = 1
    for el in range(1, n+1):
        cur *= el
        yield (cur)

n=4
for index, el in enumerate(fact(n)):
    print(index+ 1, el)
