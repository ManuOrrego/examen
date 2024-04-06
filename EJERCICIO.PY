 

nume=[]
for i in range(10):
    nums = float(input("Ingrese el numero {}: ".format(i + 1)))
    nume.append(nums)
    suma= sum(nume)

    promedio = suma/len(nume)
print("el total de la suma es: ",suma)
print("el promedio es: ",promedio)