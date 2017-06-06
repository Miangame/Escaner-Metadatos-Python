import os
from Tkinter import *
from tkFileDialog import askopenfilename

def scanMetadataFile(ruta):
    try:
    	if ruta != "":
    		print "\n-----METADATA------\n"
        	os.system("exiftool "+ ruta)
       	else:
       		print "Ruta incorrecta."       
    except:
        print "Fichero no valido."
