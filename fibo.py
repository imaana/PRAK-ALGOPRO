def fib(n):
    """menulis bil fibonacci hingga n"""
    a,b=0,1
    while b<n:
        print(b, end=' ')
        a, b, =b, a+b

def fib2(n):
    """mengembalikan bil fibonacci hingga n"""
    hasil=[]
    a, b=0,1
    while b<n:
        hasil.append(b)
        a,b=b,a+b
    return hasil
