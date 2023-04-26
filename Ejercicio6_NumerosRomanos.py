#!/usr/bin/env python
# coding: utf-8

# In[20]:


##Escribe una clase de python denomida "Conversion" que permita la conversion de un numero romano a un numero entero 
##a traves de un metodo llamado "romano_entero"


## Consideraciones a tomar en cuenta: 
## sumar los valores si en la izquierda hay un dígito mayor que a la derecha, como VI.
## restar si el valor de la izquierda es menor que el de la derecha, como el número romano IX.

class Conversion:
    def __init__(self, numero_romano):
         # Crear un diccionario para almacenar los valores de cada símbolo romano
        self.numero_romano = numero_romano.upper()
        self.valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
    def romano_entero(self):
        total = 0
        anterior = 0
        # Recorrer el número romano de derecha a izquierda
        for letra in self.numero_romano[::-1]:
            valor = self.valores_romanos[letra]
            # Restar el valor del símbolo anterior si es menor que el actual
            if valor < anterior:
                total -= valor
             # Sumar el valor del símbolo actual si es mayor o igual que el anterior
            else:
                total += valor
            anterior = valor
        
        return total
    
# Crear un objeto de la clase Conversion
numero = Conversion('MMMCMLXXXXVI')
print(numero.romano_entero())

