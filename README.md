"# Portafolio-fundamentos-de-programacion-2" 
# ¿Qué es Python? 📖
Python es un lenguaje de programación de propósito general, esto quiere decir que su enfoque no está definido y por lo tanto, se puede crear una enorme cantidad de aplicaciones utilizando este lenguaje. Por ejemplo: aplicaciones web, aplicaciones de escritorio, aplicaciones científicas o también si queremos crear una aplicación de bajo nivel, y mucho más.
# ¿Qué es una variable? 🔎
Una variable es donde se guardan y se recuperan datos que se utilizan en un programa. Cuando escribimos códigos, las variables se utilizan para: guardar (datos y estados), asignar (valores de una variable a otra), representar (valores dentro de una expresión matemáticas) y mostrar (valores por pantalla). 
Todas las variables deben ser de un tipo de datos, ya sea un dato primitivo, como un número o texto, o un dato abstracto, como un objeto que se ha creado.
## Nombrando una variable 📝
La creación de variables se puede realizar asignando un valor x a un nombre sin la necesidad de declararlas.
El operador de asignación que utilizaremos es "=".

```python

x = 2
y = 9
z = 5,6
```

## Asignando valores a una variable 📝
Podemos asignar cualquier nombre que deseamos, siempre y cuando no utilicemos palabras reservadas de python (las cuales son reservadas internamente para su funcionamiento), ni espacios, guiones o números al principio.

Ejemplos de variables:

```python

variable = 39
variable1 = 2
variable2 = 7
```

Sin embargo, hay variables que no son permitidas. Por ejemplo:

```python

3variable = 20
var-iable = 20
var iable = 20
```

También se puede asignar múltiples variables en una misma línea, separados por coma.

```python

x, y = 4, 2
x, y, z = 2, 4, 6
```

## Operadores básicos 🖩
Los operadores básicos son los más comunes que podemos encontrar, los cuales nos permiten realizan operaciones mátematicas, como la suma, resta o exponente. 

Se utilizan los siguientes operadores para python:

```python
+ suma
- resta
* multiplicación
/ división
% módulo
```
 
### Suma ➕
Para realizar una suma en python se utiliza el signo "+" y para poder imprimir por pantalla usamos "print()", a continuación se muestra un ejemplo:

```python
num1 = 5
num2 = 4
suma = num1 + num2
print(suma)
[output] 9
```

También podemos sumar con variables:

```python 

a = 3; b = 7
suma = a + b
print(suma)
[outpout] 10
```

O podemos ingresar valores a los numeros por consola:

```python

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un segundo numero:"))
suma = num1 + num2
print(suma)
```

### Resta ➖ 
Para realizar una resta en python hacemos uso del signo "+", a continuación se presenta un ejemplo:

```python
num = 10
num1 = 2
resta = num - num1
print(resta)
[output] 8
```

Podemos restar utilizando variables:

```python 

x = 30; y = 20
resta = x - y
print(resta)
[outpout] 10
```

O podemos ingresar valores a los numeros por consola:

```python

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un segundo numero:"))
resta = num1 - num2
print(resta)
```


### Multiplicación ✖ 
El operador aritmético * , multiplica los números presentes a la izquierda y derecha del operador.
Por ejemplo:

```python

num1 = 8
num2 = 12
mult = num1 * num2
print(mult)
[output] 96
```

O podemos ingresar valores a los numeros por consola:

```python

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un segundo numero:"))
mult = num1 * num2
print("El resultado es:", mult)
```

### División ➗
Para realizar una división en python se ocupa el operador "/", es de mayor importancia que al momento de realizar una división tener en cuenta que se obtendrá un resultado tipo float, sin importar si la división genera un número con decimales o no, en el siguiente ejemplo se verá como realizar una división:

```python

a = 20
b = 5
division = a / b
print(a, '/', b, '=', division)
[output] 4
```

O podemos ingresar valores a los numeros por consola:

```python

a = int(input("Ingrese un numero:"))
b = int(input("Ingrese un segundo numero:"))
division = a / b
print(a, '/', b, '=', division)
```

### Módulo
El operador "%" realiza la operación módulo entre los números presentes. Tiene como objetivo calcular el resto de una división entera, entre ambos números. Es decir, si dividimos 20 entre 3, el cociente sería 6 y el resto 2. Ese resto es lo que calcula el módulo.

Ejemplo para calcular el módulo en python:

```python

num1 = 12
num2 = 5
modulo = num1 % num2
print(num1,'%',num2,'=',modulo)
[output] 2
```

### Orden de prioridad en operaciones básicas
En los ejercicios anteriores se han aplicado un operador a dos números sin mezclarlos entre ellos. También es posible tener varios operadores en la misma línea de código, y en este caso es muy importante tener en cuenta las prioridades de cada operador y cual se ejecuta primero. Por ende, es importante siempre utilizar paréntesis, porque todo lo que está dentro de un paréntesis se evalua conjuntamente.

El orden de prioridad sería el siguiente, siendo el primero el de mayor prioridad:

```python
() Paréntesis
** Exponente
-x Negación
* / // Multiplicación, División, Cociente, Módulo
+ - Suma, Resta
```

Identificando los siguientes casos:
Con paréntesis se realiza primero la suma

```Python
print(20*(4+6))
[output] 200
```

Sin paréntesis se realiza primero la multiplicación
```Python
print(20*4+6)
[output] 86 
```

# Tipos de datos en Python 📚
En cualquier lenguaje de programación se manejan tipos de datos. Los tipos de datos definen un conjunto de valores que tienen una serie de características y propiedades determinadas. 

Por ejemplo, los distintos conjuntos de números, como los números naturales (1,2,3,4,....), los enteros (..., -2, -1, 0, 1, 2, ...) los reales (.. -1.1, -0,3,...). En python cada uno de estos conjuntos sería lo que llamamos tipos de datos.

## Integer
Los enteros en Python o también conocidos como int, son un tipo de datos que permiten representar números enteros, es decir, positivos y negativos no decimales. Int nos permite almacenar un valor númerico no decimal ya sea + o - de cualquier valor.

Por ejemplo:

```python

i = 5
print(i)
print(type(i))  #Imprime el tipo de dato que es <<class 'int'>
```

Un dato curioso se da cuando intentamos representar un número aún mayor, nos encontramos con lo siguiente en vez de saltar una excepción.

```python
print(2e2000**2)
[output] inf
```

## Float
Nos permite representar un número positivo o negativo con decimales, es decir, números reales. Los valores float son almacenados de una forma muy particular, denominada representación en coma flotante.

Por consiguiente si declaramos y asignamos un valor decimal a una variable, por defecto esta variable será de tipo float.

Ejemplo:

```python
c = 0.33304
print(c)
[output] #0.3304
print(type(c))
[output] <<class 'float'>
```

Una diferencia entre los "float" y los "int" se da en que la primera tienen unos valores mínimo y máximos que pueden representar. Es decir, la mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308.

```python
import sys
print(sys.float_info.min)
[output] 2.2250738585072014e-308

print(sys.float_info.max)
[output] 1.7976931348623157e+308
```

## String
Las cadenas o strings son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.

Por ejemplo:

```python
cadena = "Programa en Python"
print(type(cadena))
[output] <class 'str'>
```

## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.

Existen diferentes tipos de cast o conversión de tipos que se pueden hacer:

Conversión implícita, que es realizada automáticamente por Python y conversión explícita, que es realizada expresamente por nosotros, por ejemplo, convertir de str a int con str().

Ejemplo:

```python
int a str: str(45)
str a int: int ("123")
float a int: int (3.5)
```

## List
Las listas son un tipo de estructuras de datos más versátiles del lenguaje, porque nos permite guardar un conjunto arbitrario de datos. Es decir, se puede almacenar practicamente cualquier cosa en ellas.

Cada elemento o valor que está dentro de una lista se denomina elemento. Así como las cadenas se definen como caracteres entre comillas, las listas se definen con valores entre corchetes [].

Ejemplo:

```python
lista = [4, 5, 6, 7]
print(list)
```

## Tuple
Un tuple o unas tuplas en Python son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables.

Ejemplo:

```python
tupla = (1, 3, 6)
print(tupla)
[output] (1, 3, 6)
```
Se puede declarar sin (), separando por  , todos sus elementos.

```python
tupla = 1, 3, 6
print(type(tupla))
[output] <class 'tuple'>

print(tupla)
[output] (1, 3, 6)
```

## Dictionary
Un diccionario en Python es una colección de elementos, cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.

Ejemplo:

```python
b = {
  "Nombre": "Ruben",
  "Edad": 32,
  "Documento": 1482022
}
print(b)
[output] {'Nombre': 'Ruben', 'Edad': 32, 'Documento': 1482022}
```

# Tomando decisiones ✔✔

## Sentencia if
Es una forma común de controlar el flujo de un programa, lo que te permite ejecutar bloques de código específicos según el valor de algunos datos. Si la condición que sigue a la palabra clave if se evalúa como verdadera, el bloque de código se ejecutará.

Un ejemplo sería si tenemos dos valores a y b que queremos dividir. Antes de entrar en el bloque de código que divide a/b , sería importante verificar que b es distinto de cero, ya que la división por cero no está definida. Es aquí donde entran los condicionales if.

```python
a = 4
b = 2
if b!= 0:
    print(a/b)
```

En el ejemplo de arriba podemos observar cómo se puede usar un if en Python. Con el operador != comprobamos que el número b sea diferente de cero, y si lo es, se ejecuta el código que está identado. Por lo tanto, un if tiene dos partes:

La condición que se tiene que cumplir para que el bloque de código se ejecute, en nuestro caso b != 0.

El bloque de código que se ejecutará si se cumple la condición anterior.

Es muy importante tener en cuenta que la sentencia “if” debe ir terminada por : y el bloque de código a ejecutar debe estar identado. Si usas algún editor de código, seguramente la identación se producirá automáticamente al presionar enter. Nótese que el bloque de código puede también contener más de una línea, es decir puede contener más de una instrucción.

```python
if b!= 0:
    c = a / b
    d = c + 1
    print(d)
```

Todo lo que va después del if y está identado, será parte del bloque de código que se ejecutará si la condición se cumple. Por lo tanto el segundo print() "Fuera if" será ejecutado siempre, ya que está fuera del bloque if.

## Ciclo For
El ciclo for es un tipo de bucle, parecido al while pero en este caso con ciertas diferencias. La principal diferencia es que el número de iteración de un for se encuentra definido de antemano, en cambio el while no esta definido. En while la condición es evaluada en cada interacción para decidir si volver a ejecutar o no el código, en el for no existe tal condición, sino un iterable donde define las ocasiones que se ejecutará el código. 

El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.

Ejemplo:

```python

for i in range(0, 5):
    print(i)
[output]  0
          1
          2
          3
          4
```

Otro ejemplo que podemos analizar es el siguiente:

```python

for i in "Python":
    print(i)
[output]  P
          y
          t
          h
          o
          n
```

Veamos el siguiente ejercicio:

#Calcular la suma y la media aritmetica de Números reales. 
#solicitar el valor de n al usuario y cada uno de los Números reales.

```python

n = int(input("Ingrese los números que desee: "))
suma= 0
for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)
```


## Ciclo While
El bucle while evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Llamaremos iteración a una ejecución completa del bloque de código.

Cabe aclarar que se presentan dos tipos de bucles, el primero tiene un número de iteraciones no definidas, y el segundo los que tienen un número de iteraciones definidas. El while estaría dentro del primer tipo.   

Ejemplo:

```python
x = 5
while x > 0:
    x -=1
    print(x)
[output] 4, 3, 2, 1, 0
```

En el ejemplo anterior se presenta un caso sencillo de while. Donde tenemos una condición x > 0 y un bloque de código a ejecutar mientras dure esa condición x -= 1 y print(x). Por lo tanto mientras que x sea mayor que 0, se ejecutará el código. Una vez se llega al final, vuelve a empezar y si la condición se cumple, se ejecutará otra vez. En este caso entra al bloque de código 5 veces, hasta que la sexta, x vale cero y por lo tanto la condición ya no se cumple. Por eso es que while presenta dos partes.

Otro ejemplo utilizando while:

```python
#10-20

num=11

while num<10 or num >20 or num%2!=0:
    num=int(input("ingrese numero:"))

print("se fue")
```
Otro y ultimo ejemplo:

```python

x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)

[output] ['Dos', 'Tres']
         ['Tres']
         []
```

## Break

La sentencia break nos permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle.Esto significa que una vez se encuentra la palabra break, el bucle se habrá terminado.

Ejemplo:

```python
j=0
for i in range (10):
    j+=2
    print ("i;",i,"j:",j)
    if j==10:
        break
```

Otro ejemplo:

```python
for i in range(5):
    print(i)
    break
[output] 0
```
Un ejemplo un poco más útil, sería el de buscar una letra en una palabra. Se itera toda la palabra y en el momento en el que se encuentra la letra que buscábamos, se rompe el bucle y se sale.

Esto es algo muy útil porque si ya encontramos lo que estábamos buscando, no tendría mucho sentido seguir iterando la lista, ya que desperdiciaríamos recursos.

```python
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)
[output] p
         y
         t
         Se encontro la h
```

## Continue
El uso de continue al igual que el ya visto break, nos permite modificar el comportamiento de de los bucles while y for.

Concretamente, continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.

La diferencia entre el break y continue es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.

Ejemplo:

```python

contador=0
for i in range (10):
    for j in range (10):
        contador +=1
        print ("i:",i,"j:",j)
        if contador >50:
            continue
```

En el siguiente ejemplo vemos como al encontrar la letra P se llama al continue, lo que hace que se salte el print(). Es por ello por lo que no vemos la letra P impresa en pantalla.

```python
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)
[output] y
         t
         h
         o
         n
```
