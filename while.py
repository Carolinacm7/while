# i = 0
# while i <= 100:
#     i = i+1
#     if i % 13==0:
#         print(i)
# i= 5
# while i >=1:
#     print(i)
#     i=i-1
# print ("eso es todo")
#cual fruta tiene mas letras

lista_frutas = ("Manzanas", "Peras", "Mango", "Papaya", "Uvas", "Granadilla","Banano")
x = len(lista_frutas)
fruta_mayor = ""
i=0 #variable de control
while(i<x):
    letras= len(lista_frutas[i])
    if (letras>len(fruta_mayor)):
        fruta_mayor= lista_frutas[i]
    i=i+1
print ("la fruta mayor es:"+ fruta_mayor)




