# programa para verificar si un numero es positivo oo negativo

# input
X=int(input("digite un numero: "))

#Processing
if X>0:
    RTA= "positivo"
elif X==0:
    RTA= "su numero es neutro "
else:
    RTA= "negativo"

# output
print("el numero",X,"es",RTA)