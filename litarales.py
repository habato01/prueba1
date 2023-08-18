# literal siendo un dato cuyo Valor 
# esta determinado por el mismo por ejemplo 
print("2")
print(2)

# en cambio si se usa la letra C
# este ya no seria una literlal

#para numeros enteros largos se usa el guion bajo
#o pegarlos todos juntos para mostrarlos en pantalla
c=1_600_999
c1=1600999
print(c)
print(c1)

# Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.

# 0o123 es un número octal con un valor (decimal) igual a 83.

# La función print() realiza la conversión automáticamente. Intenta esto:
print(0o123)


# La segunda convención nos permite utilizar números en hexadecimal. Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x).

# 0x123 es un número hexadecimal con un valor (decimal) igual a 291. La función print() puede manejar estos valores también. Intenta esto:
print(0x123)

#variable flotantes
x=2.5
print(x)

#NUMEROS con notacion cientifica
x1=3E8
print(x1)
#python tiende a mostrar resultados muy extenso ya con su definicion de notacion cientifica
print(0.0000000000000000000001)
# lo mostrar como 1e-22



#ahora para mostrar un valor largo en notacion cientifica seria asi 
print(6.62607E-34) #python lo presentara de la misma forma ya que siempre elige la forma
# mas corta de presentar los numeros extensos


# Supongamos que se desea mostrar un muy sencillo mensaje:

# Me gusta "Monty Python"
# ¿Cómo se puede hacer esto sin generar un error? Existen dos posibles soluciones.

# La primera se basa en el concepto ya conocido del carácter de escape, el cual recordarás se utiliza empleando la diagonal invertida. La diagonal invertida puede también escapar de la comilla. Una comilla precedida por una diagonal invertida cambia su significado - no es un limitador, simplemente es una comilla. Lo siguiente funcionará como se desea:


print("Me gusta \"Monty Python\"")
# La segunda solución puede ser un poco sorprendente. Python puede utilizar una apóstrofe en lugar de una comilla. Cualquiera de estos dos caracteres puede delimitar una cadena, pero para ello se debe ser consistente.

# Si se delimita una cadena con una comilla, se debe cerrar con una comilla.

# Si se inicia una cadena con un apóstrofe, se debe terminar con un apóstrofe.

# Este ejemplo funcionará también:
print('Me gusta "Monty Python"')


# ahora bien con apostrofe es lo mismo pero al 
# reves para mostrarlo en una cadena
print('I\'m Monty Python.')#opcion uno
print("I'm Monty Python.")#opcion dos

