# Reto 3
# Programación Orientada a Objetos - UNAL



## Reto 3

Para este caso use un case segun la operacion aritmetica introducida por el usuario, y despues de eso en cada case correspondiente se hacia la accion correspondiente.
```python
num1= int(input("Digite los numeros a operar:"))
num2= int(input())
operacion= str(input("Digite la operacion a realizar:"))
def Operaciones(numero1,numero2,opera):
    match opera:
        case "+":
            return (numero1 + numero2)
        case "-":
            return(numero1 - numero2)
        case "*":
            return(numero1 * numero2)
        case "/":
            return (numero1 / numero2)
print("El resultado de la operacion es:" + str(Operaciones(num1,num2,operacion)))

```


### Componentes del Ciclo `while`
- Condición de parada: Evalúa si el bloque de instrucciones debe ejecutarse.
- Bloque de instrucciones: Conjunto de instrucciones que se ejecutan mientras la condición sea verdadera.
- Actualización: Modificación de variables para que eventualmente la condición de parada sea falsa y termine el ciclo.

