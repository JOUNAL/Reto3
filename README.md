# Reto 1
# Programación Orientada a Objetos - UNAL



## Reto 1.1

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

## Reto 1.2

Para el palindromo use una division entera para tener donde esta la mitad, y entera porque si es impar no tomara en cuenta la letra de la mitad, despues tomara esa longitud y la compara con la primera y la ultima, se le suma 1 a la primera y se le resta 1 a la ultima, asi hasta que llegue a la mitad dada por la division entera

```python
def palindromo(var1):
    i:int=0
    j:int=0
    longitud=int(len(var1))
    j=longitud//2
    while i < j:
        if var1[i]==var1[longitud-(1+i)]:
            i+=1
        else:
            return 0
    return 1

palabra= str(input("Digite la palabra a validar:"))
if palindromo(palabra)==0:
    print(palabra + " no es un palindromo")
else:
    print(palabra + " es un palindromo")
```

## Reto 1.3

Para este caso considere que introducia una lista de numeros, tendria que tener al final una lista que solo eran primos y para saber si era primo utilice un contador de 2 hasta el numero-1 y si todas las veces que con la operacion modular da diferente de 0, se añade a la lista prima

```python
lista_total=[]
valor=0
numero=True
while numero==True:
    nuevo_numero= input("Digite numeros para verificar si son primos, o una letra para parar:")
    if nuevo_numero.isnumeric()==True:
        lista_total.append(nuevo_numero)
    else:
        break
def num_primos(lista_x):
    i: int=0
    lista_prima=[]
    while i<len(lista_x):
        j: int=2
        while j < int(lista_x[i]):
            if int(lista_x[i]) % j != 0:
                j +=1
                if j==int(lista_x[i]):
                    lista_prima.append(lista_x[i])
            else:
                break
        i +=1
    i=0
    return lista_prima

print("Los numeros primos de la lista digitada son:")
while valor<len(num_primos(lista_total)):
    print(num_primos(lista_total)[valor])
    valor +=1
```

## Reto 1.4

La idea era ir sumando numero por numero en la lista, y si la suma era mas grande que la de los anteriores numeros, guardaba esa suma y la posicion de los numeros de esa suma, para despues imprimirlos

```python
lista_numeros=[]

numero=True
while numero==True:
    nuevo_numero= input("Digite la lista de numeros; o una letra para parar:")
    if nuevo_numero.isnumeric()==True:
        lista_numeros.append(nuevo_numero)
    else:
        break
def sum_mayor(lista_y):
    i: int=0
    valor=0
    valor_m=0
    posicion=0
    while i<len(lista_y)-1:
        valor=int(lista_y[i])+int(lista_y[i+1])
        if valor>valor_m:
            valor_m=valor
            posicion=i
        i +=1
    print("Los numeros que dan la suma de mayor valor son " + str(lista_y[posicion]) + " y " + str(lista_y[posicion+1]))
    return valor_m
print("La mayor suma consecutiva de la lista es:" + str(sum_mayor(lista_numeros)))


```
## Reto 1.5

La idea era que por cada palabra hiciera una lista de las letras sin que se repitiera, despues esa lista de esa palabra se compararia con cada palabra, y si se verificaba que la cantidad de letras de la palabra a escanear era igual a su longitud comparada con la lista de letras, entonces esa palabra tenia las mismas letras y su posicion se añadia a una lista, y si esa palabra se repetia mas de una vez en la lista, se imprimia

```python
lista_pala=[]
no_vacio=True
while no_vacio==True:
    palabra= str(input("Digite las palabras que quiera evaluar que tengan los mismos caracteres; o deje el cambio vacio para terminar:"))
    if palabra !="":
        lista_pala.append(palabra)
    else:
        break
    
def letras_palabras(lista_palabras):
    palabras_bien=[]
    lista_aux=[]+lista_palabras
    palabra_base: str
    palabra_ahora: str
    letra: str
    i=0
    g=0
    d=0
    while i<len(lista_palabras):
        palabra_base=lista_palabras[i]
        j=0
        palabra_letras=[]
        c=0
        while c<len(palabra_base):
            palabra_letras.append(palabra_base[c])
            c +=1
        c=0
        while c<len(palabra_letras):
            d=0
            h=0
            while h<len(palabra_letras):
                a=palabra_letras[h]
                b=palabra_letras[c]
                if palabra_letras[h]==palabra_letras[c]:
                    
                    d +=1
                if d>1:
                    palabra_letras.pop(h)
                    h -=1
                    d -=1
                h +=1
            c +=1
        
        while j<len(lista_palabras):
            palabra_ahora=lista_palabras[j]
            k=0

            t=0
            while k<len(palabra_letras):
                w=0
                
                while w<len(palabra_ahora):
                    if (palabra_letras[k]==palabra_ahora[w])==True:
                        t +=1
                
                    w +=1
                k +=1
            if t==len(palabra_ahora):
                palabras_bien.append(j)
            j +=1
        i +=1


    c=0

    i=len(palabras_bien)
    while c<i:
        h=0
        d=0
        while h<i:
            if palabras_bien[h]==palabras_bien[c]:
                d+=1
            h +=1
        if d==1:
            palabras_bien.pop(c)
            i=len(palabras_bien)
            c -=1
        c+=1 

    c=0
    i=len(palabras_bien)
    while c<i:
        h=0
        d=0
        while h<i:
            a=palabras_bien[h]
            b=palabras_bien[c]
            if palabras_bien[h]==palabras_bien[c]:
                d+=1
            h +=1
        if d>1:
            palabras_bien.pop(c)
            i=len(palabras_bien)
            c -=1
        c+=1 


    palabras_bien=sorted(palabras_bien)
    c=0
    i=len(palabras_bien)
    while c<i:
        h=int(palabras_bien[c]) - c
        lista_aux.pop(h)
        c+=1


    c=0
    i=len(lista_palabras)
    while c<i:
        h=0
        b=len(lista_aux)
        while h<b:
            if lista_palabras[c]==lista_aux[h]:
                lista_palabras.pop(c)
                i=len(lista_palabras)
                c -=1  
            h +=1
        c+=1 
    return lista_palabras

print(letras_palabras(lista_pala))

```
