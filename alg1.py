c = int(input("c: "))
x = int(input("x: "))
n = int(input("n: "))

c_dv = format(c, "b")
expected_res = (x**c) % n
z = 1
c_dv_spisok = list(c_dv)

print("Ожидаемый результат: {}**{} mod {} = {}".format(x, c, n, expected_res))
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
if expected_res == z:
    print("Всё верно!")
else:
    print("Что-то пошло не так...")
        


