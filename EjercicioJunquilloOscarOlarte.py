# Realizado por Óscar Duván Olarte
#               20162020450

def evaluarFuncion(i, j):
    result = ((0.25*pow(int (i),2))/(0.02*int(j))) - (0.0001*int (j))/0.02
    return round(result, 1)

matriz = []
print("Input")
flag = True
while flag:
    cadena = input()
    nums = cadena.split()
    if nums[0]== '0' and nums[1]== '0':
        flag = False
    else:
        matriz.append(nums)

print("Output:")
for expresion in matriz:
    print(evaluarFuncion(expresion[0],expresion[1]))



