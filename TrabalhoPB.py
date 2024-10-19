n = int(input("Defina o número de obeservações: "))
x = int(input("Defina o número de sucessos: "))
p = float(input("Defina a probabilidade de sucesso em forma decimal: "))

q = 1 - p
nx = n-x
pa = 0


de1=1
count=nx

while count >= 1:
    de1 *= count
    count -= 1

de2=1
count=x

while count >= 1:
    de2 *= count
    count -= 1

if nx > x:
    nu=1
    count=n

    while count > nx:
        nu *= count
        count -= 1
    c = nu/de2
else:
    nu=1
    count=n

    while count > x:
        nu *= count
        count -= 1
    c = nu/de1


pf = p**x
qf = q**nx
final1 = c*pf*qf*100

stoper = x
pac = 0
while pac <= stoper:
    x=pac
    pac += 1
    nx = n-x

    de1=1
    count=nx

    while count >= 1:
        de1 *= count
        count -= 1

    de2=1
    count=x

    while count >= 1:
        de2 *= count
        count -= 1

    if nx > x:
        nu=1
        count=n

        while count > nx:
            nu *= count
            count -= 1
        c = nu/de2
    else:
        nu=1
        count=n

        while count > x:
            nu *= count
            count -= 1
        c = nu/de1


    pf = p**x
    qf = q**nx
    pav = c*pf*qf
    pa += pav

final2 = pa*100


print("Probabilidade Binomial Individual: %.2f" % final1)
print("Probabilidade Binomial Acumulada: %.2f" % final2)
