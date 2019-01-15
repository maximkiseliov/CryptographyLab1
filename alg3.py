from math import sqrt

def algo_one(c, x, n):
#c aka m - stepeni pervogo cisla(stepeni bazi)
#x aka alp aka result1 - pervoe cislo(baza)
#n aka p - moduli
    c_dv = format(c, "b")
    expected_res = (x**c) % n
    z = 1
    c_dv_spisok = list(c_dv)

    print("{}**{} mod {} = {}".format(x, c, n, expected_res))
    print("({})10 = ({})2". format(c, c_dv))
    print("\ni\tci\tz")

    for i in range(len(c_dv_spisok)):
        ii = (len(c_dv_spisok)-1) - i
        c_i = int(c_dv_spisok[i])
        
        
        if c_dv_spisok[i] == '1':
            print("{}\t{}\tz = {}**2 mod{} = {} mod{} = {};".format(ii, c_i, z, n, z**2, n, (z**2) % n))
            z = (z**2) % n
            print(" \t \tz = {} * {} mod{} = {};".format(z, x, n, (z * x) % n))            
            z = (z * x) % n        
        else:
            print("{}\t{}\tz = {}**2 mod{} = {} mod{} = {};".format(ii, c_i, z, n, z**2, n, (z**2) % n))
            z = (z**2) % n

    print("\nНаш результат = ", z)
    print("-*"*10)
    print("")
    return z

def beaty_print(mainarray):
#print table that we get as a result of work of func algo_two
    print("")
    print("step\tn0\tb0\tq\tr\tt0\tt\ttemp")
    for i in range(len(mainarray)):
       intostring = map(str, mainarray[i])
       print('\t'.join(intostring))
       
def algo_two(b, n):
#b aka alp**i - bazis
#n aka p - moduli
    if b == 1:
        return 1
    
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
    print("-*"*10)
    print("")
    return temp

def algo_three_result(alp, bet, m, num_sublist_L1, num_sublist_L2, p):
    print("")
    print("-*"*10, "ФИНАЛЬНЫЙ РЕЗУЛЬТАТ","-*"*10)
    final_result = m * num_sublist_L1 + num_sublist_L2 %(p-1)
    print("LOGalpha BETA = m * j + i (mod(p-1)) -> log%i %i = %i * %i + %i (mod(%i - 1)) = %i" % (alp, bet, m, num_sublist_L1, num_sublist_L2, p, final_result))
        
#----------------------------------------------------MAIN----------------------------------------------------
p = int(input("p: "))
alp = int(input("alpha: "))
bet = int(input("beta: "))
m = int(sqrt(p - 1))
list_L1 = []
list_L2 = []

print("Нам нужно найти log%i %i\n" % (alp, bet))
result_one = algo_one(m, alp, p)

print("Вычисление списка пар L1:")

for i in range(m):
    temp_list = list()
    temp_res = int()
    temp_res = algo_one(i, result_one, p)
    temp_list.insert(0, i)
    temp_list.insert(1, temp_res)
    list_L1.append(temp_list)
    
print("\nСписок пар L1 (j, alpha**mj(modp) | 0 <= j <= m-1) -> (j, %i**j(mod%i) | 0 <= j <= %i):" % (result_one, p, m-1))
print(list_L1)

print("Вычисление списка пар L2:")

for i in range(m):
    temp_list = list()
    temp_res = int()
    b = alp**i
    temp_res = algo_two(b, p)
    result_algo_two = bet * temp_res % p
    temp_list.insert(0, i)
    temp_list.insert(1, result_algo_two)
    list_L2.append(temp_list)
    
print("\nСписок пар L2 ")#(j, alpha**mj(modp) | 0 <= j <= m-1) -> (j, %i**j(mod%i) | 0 <= j <= %i):" % (result_one, p, m-1))
print(list_L2)

print("\nПроверка схожих пар")
pair_index = 0

while pair_index < len(list_L1):
   potential_pair = list_L1[pair_index]
   
   for i in range(len(list_L2)):
      if potential_pair[1] == list_L2[i][1]:
         match_pair_L1 = list_L1[pair_index]        
         match_pair_L2 = list_L2[i]
         
         print("\tПара из списка L1:", match_pair_L1)         
         print("\tПара из списка L2:", match_pair_L2)

   pair_index += 1

algo_three_result(alp, bet, m, match_pair_L1[0], match_pair_L2[0], p)
