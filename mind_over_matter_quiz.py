from itertools import product

for p in product(('+', '-'), repeat=5):
    j = ''.join
    a = j(map(j, zip(p, 'AEMIQ')))
    b = j(map(j, zip(p, 'UQIME')))
    c = j(map(j, zip(p, 'HLTPX')))
    a = a.replace('Q', '17').replace('A', '1').replace('M', '13').replace('E', '5').replace('I', '9')
    b = b.replace('Q', '17').replace('A', '1').replace('M', '13').replace('E', '5').replace('I', '9').replace('U','21')
    c=c.replace('H','8').replace('L','12').replace('X','24').replace('P','16').replace('T','20')
    if eval(a) == eval(b) or eval(b) == eval(c) or eval(a) == eval(c):
        print('{a} {a2} {b2} {c2}'.format(a=a, a1=a, a2=eval(a), b1=b, b2=eval(b), c2=eval(c)))
