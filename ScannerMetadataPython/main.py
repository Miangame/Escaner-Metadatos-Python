# -*- coding:utf-8 -*-
from funciones import *

def limpiarPantalla():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")

limpiarPantalla()

print '\n>>>Pulse INTRO para abrir un documento...'
raw_input()
entrada = 's'
while entrada == "s":
	root = Tk()
	root.withdraw()
	ruta = askopenfilename()
	scanMetadataFile(ruta)
	entrada = raw_input("\n¿Desea abrir otro documento? s/n: ")
	while entrada != 's' and entrada != 'n':
		entrada = raw_input("\n¿Desea abrir otro documento? s/n: ")
	limpiarPantalla()
