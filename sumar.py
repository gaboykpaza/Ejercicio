def sumar(a,b):
    return a + b
while True:
    try:
        N = int(input("ingrese valor "))
        N2 = int(input("ingrese valor "))
        break
    except:
        print("ingrese valores enteros")
        
print(sumar(N, N2))