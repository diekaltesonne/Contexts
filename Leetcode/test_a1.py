def fib(i):
    while True:
        i+=1
        yield i
    
for i in (fib(0)):
    if i == 10:
        break
    print(i) 
