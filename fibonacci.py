#fibonacci
def fibonaci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonaci(2000)
#-===============-=-=--=-=--=-=-=-=-
#fibonacci retorna valor
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) #mesma coisa q 'result += [a]' n sei pq "[]"
        a, b = b, a+b
    return result

f100 = fib(100)
print(f100)