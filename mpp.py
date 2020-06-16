"""
@author: 
    Tania lizbeth Oria trejo 14590555
    Efrain Garcia Garcia     15590287

# Programación  Lógica

# Modus ponendo ponens

"el modo que, al afirmar, afirma"

P → Q. P ∴ Q


Se puede encadenar usando algunas variables

P → Q. 
Q → S. 
S → T. P ∴ T

Ejercicio 
Defina una funcion que resuelva con verdadero o falso segun corresponada

Laura esta en Queretaro
Alena esta en Paris
Claudia esta en San Francisco
Queretaro esta en Mexico
Paris esta en Francia
San Francisco esta en EUA
Mexico esta en America
Francia esta en Europa
EUA esta en America

def esta(E1,E2):
	pass


print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false

"""
#def esta(e1,e2):
#   esta==Base

def esta1(base,b):
	if not base:
		return []
	if len(base):
		if b == base[0][0]:
			return base[0][1]
		else:
			return esta1(base[1:], b)
Base = [
	["Laura","Queretaro"],
    ["Alena","Paris"],
    ["Claudia","San Francisco"],
    ["Queretaro","Mexico"],
    ["Paris","Francia"],
    ["San Francisco","EUA"],
	["Mexico","America"],
    ["Francia","Europa"],
    ["EUA","America"]
]

#def esta(E1,E2):
#	pass

def esta(E1,E2):
	B = esta1(Base,E1)
	X = esta1(Base, B)
	if X == E2 or B == E2:
		return True
	Z = esta1(Base, X)
	if Z == E2:
		return True
	else:
		return False



print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false
