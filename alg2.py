def beaty_print(mainarray):
    print("")
    print("step\tn0\tb0\tq\tr\tt0\tt\ttemp")
    for i in range(len(mainarray)):
       intostring = map(str, mainarray[i])
       print('\t'.join(intostring))

b = int(input("b: "))
n = int(input("n: "))
mainlist = []
sublist = []

#START 1st step
i = 1
n0 = n
print("%i.\tn0 = n = %i;"%(i, n))

b0 = b
print("\tb0 = b = %i;"%(b))

t0 = 0
print("\tt0 = %i;"%(t0))

t = 1
print("\tt = %i;"%(t))

q = n0 // b0
print("\tq = n0 // b0 = %i // %i = %i;"%(n0, b0, q))

r = n0 - (q * b0)
print("\tr = n0 - q * b0 = %i - %i * %i = %i;"%(n0, q, b0, r))

temp = t0 - (q * t)
print("\ttemp = t0 - q * t = %i - %i * %i = %i;"%(t0, q, t, temp))

if temp >= 0:
    temp = temp % n
    print("\ttemp = temp mod%i = %i;"%(n, temp))
else:
    print("\ttemp = n - ((-temp) mod n) = %i - (%i mod%i) = %i;"%(n, 0-temp, n, n - ((-temp) % n)))
    temp = n - ((-temp) % n)
    
sublist = [i, n0, b0, q, r, t0, t, temp]
mainlist.append(sublist)
#END 1st step

#START other steps
while True:
    print("")
    sublist = []
    i += 1
    n0 = b0
    print("%i.\tn0 = b0 = %i;"%(i, b0))
    
    b0 = r
    print("\tb0 = r = %i;"%(r))
    
    t0 = t
    print("\tt0 = %i;"%(t0))
    
    t = temp
    print("\tt = temp = %i;"%(temp))
    
    q = n0 // b0
    print("\tq = n0 // b0 = %i // %i = %i;"%(n0, b0, q))
    
    r = n0 - (q * b0)
    print("\tr = n0 - q * b0 = %i - %i * %i = %i;"%(n0, q, b0, r))
    if r == 0:
        sublist = [i, n0, b0, q, r, t0, t, " "]
        mainlist.append(sublist)
        break

    temp = t0 - (q * t)
    print("\ttemp = t0 - q * t = %i - %i * %i = %i;"%(t0, q, t, temp))
    
    if temp >= 0:
        temp = temp % n
        print("\ttemp = temp mod%i = %i;"%(n, temp))
    else:
        print("\ttemp = n - ((-temp) mod n) = %i - (%i mod%i) = %i;"%(n, 0-temp, n, n - ((-temp) % n)))
        temp = n - ((-temp) % n)
        
    sublist = [i, n0, b0, q, r, t0, t, temp]
    mainlist.append(sublist)
#END other steps    
        
beaty_print(mainlist)

print("Результат:", temp)


        
