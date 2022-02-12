#@Sergitooo

#CREAR VARIABLES
#INPUT DEL PROGRAMA
primer_dígito = float(input("Introduce un número: "))
segundo_dígito = float(input("Introduce otro número: "))
suma = primer_dígito+segundo_dígito
resta = primer_dígito-segundo_dígito
multiplicacion = primer_dígito*segundo_dígito
division = primer_dígito/segundo_dígito

#ELECCIÓN DE LA OPERACIÓN
entrada = int(input("\n¿Qué quieres hacer?"+"""\n
[1] SUMA
[2] RESTA
[3] MULTIPLICACIÓN
[4] DIVISIÓN
\n"""))

#RESOLVER OPERACIÓN
if entrada == 1:
  print("\nSuma: "+int(suma))
if entrada == 2:
  print("\nResta: "+str(resta))
if entrada == 3:
  print("\nMultiplicación: "+str(multiplicacion))
if entrada == 4:
  print("\nDivisión: "+str(division))
