# como poder hacer una funcion correcta
# para que se pueda
# usar en donde se 
# necesite 

print ('hola mundo')
print ("hola mundo ")
#Python requiere que no haya más de una instrucción por línea
print("Vino la lluvia y se la llevó.")
print("La Witsi Witsi Araña subió a su telaraña.")
# aqui agregamos una linea de por medio de separacion
print("La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

# igual manera se puede usar caracteres de linea /n para 
#mostrar codigo en si
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\nay se la llevó.")


# tambien se tiene el uso para poder 
# mostrar varios argumentos en la misma linea 
# de lo que estemos mostrando con print
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")


#comando end en la funcio print donde se hara un espacio de linea segun lo que se quiera mostrar
print("Mi nombre es", "Python.", end="\n")
print("Monty Python.")

# el parámetro end especifica que imprimir al final de la declaración de impresión.
print("mi nombre es", end="")
print(" monty python")


#poner guion o otro signo al espacio que pueda haber entre caracteres con el comando sep=
print("mi","nombre","es","monty","python",sep="--")

# Modifica la primera línea de código en el editor, usando las palabras claves reservadas sep y end, para que se obtenga la salida esperada. Emplea dos funciones print() en el editor.

# No cambies nada en la segunda invocación del print().

'''
respuesta
'''
print("Programming","Essentials","in", sep="***", end="...")
print("Python")


#multiplicando la salida de caracteres para que salga las veces indicadas siend el "*2" 
print("va ver o no va ver"*2)


#dibujando una flecha y duplicarla
print("    *"*2)
print("   * *"*2)
print("  *   *"*2)
print(" *     *"*2)
print("***   ***"*2)
print("  *   *"*2)
print("  *   *"*2)
print("  *****"*2)

print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)