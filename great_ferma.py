#https://www.quora.com/Fermats-Last-Theorem-How-did-the-writing-staff-of-The-Simpsons-find-3987-12-+4365-12-approx-4472-12-How-does-it-manage-to-fool-a-calculator
def get_relative_error(x,n):
    y = int( pow(x,1./n) )
    return min( x/pow(y,n), pow(y+1,n)/x ) - 1

n = 8
print (f'power is {n}')
best = float('+inf')
for a in range(1000,10**6):
    for b in range(a//2,a+1):
        err = get_relative_error( a**n + b**n, n )
        if err < best:
            best = err
            c = int(( a**n + b**n ) ** (1./n))
            print('{} {} {} {:.42f}'.format(a,b,c,err))

