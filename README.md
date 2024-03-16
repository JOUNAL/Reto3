# Reto 3
# Programación Orientada a Objetos - UNAL



## Reto 3.1

En este caso, el codigo contedra la definicion de la clase linea, punto rectangulo y cuadrado (siendo esta una subclase de rectangulo)

### Clase Punto
Veremos como se los metodos de la clase punto, que seria reiniciarlo (ponerlo de nuevo en 0,0), moverlo (cambiarle las coordenadas a un nuevo x,y), y calcular la distancia entre dos puntos propuestos

### Clase Linea 
Veremos como se los metodos de la clase linea, en este caso: calcular la pendiente, calcular la longitud de la linea (utlizando el teorema de pitagoras), si intersecta con el eje x y donde intersecta y si intersecta con el eje y donde intersecta
Para
```python
class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

first_point = Point(x=1, y=1)
second_point = Point(x=2, y=2)
print(first_point.compute_distance(second_point))

class Line:

    def __init__(self,startx,starty,endx,endy):
        self.startx=startx
        self.starty=starty
        self.endx=endx
        self.endy=endy
    def compute_lenght(self):
        self.lenght=(((self.endy-self.starty))**2+((self.endx-self.startx)**2))**0.5
        print("La longitud de la linea es de:" + str(self.lenght))
    def compute_slope(self):
        self.slope=(self.endy-self.starty)/(self.endx-self.startx)
        print("La pendiente de la linea es de:" + str(self.slope))
    def compute_vertical_cross(self):
        self.intersecty=self.starty-(self.slope*self.startx)
        if self.intersecty>self.startx and self.intersecty<self.endx:
            print(self.intersecty)
        else:
            print("No intersecta con el eje y")
    def compute_horizontal_cross(self):
        self.intersectx=(self.starty*0-self.intersecty)/self.slope
        if self.intersectx>self.startx and self.intersectx<self.endx:
            print(self.intersectx)
        else:
            print("No intersecta con el eje x")

Linea0=Line(startx=2,starty=0,endx=5,endy=9)
Linea1=Line(startx=2,starty=2,endx=2,endy=12)
Linea2=Line(startx=2,starty=12,endx=22,endy=12)
Linea3=Line(startx=22,starty=12,endx=22,endy=2)
Linea4=Line(startx=22,starty=2,endx=2,endy=2)
Linea0.compute_lenght()
Linea0.compute_slope()
Linea0.compute_vertical_cross()
Linea0.compute_horizontal_cross()

class Rectangulo:
    def __init__(self,metodo,x=0,y=0,width=0,height=0,x1=0,y1=0,Lineo1=0,Lineo2=0,Lineo3=0,Lineo4=0):
        self.metodo=metodo
        match metodo:
            case 1:
                self.x=x
                self.y=y
                self.width=width
                self.height=height
            case 2:
                self.x=(x-((width)/2))
                self.y=(y-((height)/2))
                self.width=width
                self.height=height
            case 3:
                self.x=x
                self.y=y
                self.width=abs(x-x1)
                self.height=abs(y-y1)
                a=0
                b=0
                if self.x>x1:
                    a=0+self.x
                    self.x=0+x1
                    x1=a
                if self.y>y1:
                    b=0+self.y
                    self.y=0+y1
                    y1=b
            case 4:
                self.x=Lineo1.startx
                self.y=Lineo1.starty


                if self.x>Lineo2.startx:
                    self.x=Lineo2.startx
                    self.y=Lineo2.starty
                elif self.x>Lineo3.startx:
                    self.x=Lineo3.startx
                    self.y=Lineo3.starty
                elif self.x>Lineo4.startx:
                    self.x=Lineo4.startx
                    self.y=Lineo4.starty

                if Lineo1.startx==Lineo1.endx:
                    self.height=abs(Lineo1.starty-Lineo1.endy)
                elif Lineo1.starty==Lineo1.endy:
                    self.width=abs(Lineo1.startx-Lineo1.endx)

                if Lineo2.startx==Lineo2.endx:
                    self.height=abs(Lineo2.starty-Lineo2.endy)
                elif Lineo2.starty==Lineo2.endy:
                    self.width=abs(Lineo2.startx-Lineo2.endx) 

                if Lineo3.startx==Lineo3.endx:
                    self.height=abs(Lineo3.starty-Lineo3.endy)
                elif Lineo3.starty==Lineo3.endy:
                    self.width=abs(Lineo3.startx-Lineo3.endx)   

                if Lineo4.startx==Lineo4.endx:
                    self.height=abs(Lineo4.starty-Lineo4.endy)
                elif Lineo4.starty==Lineo4.endy:
                    self.width=abs(Lineo4.startx-Lineo4.endx)                


                
    def compute_area(self):
        return self.height*self.width
    def compute_perimeter(self):
        return(self.height*2)+(self.width*2) 
    def compute_interference_point(self,pointx,pointy):
        if  self.x<pointx<(self.x+self.width) and self.y<pointy<(self.y+self.height):
            return 1
        else:
            return 0
                
class Cuadrado(Rectangulo):
    def __init__(self,metodo,x=0,y=0,height=0,x1=0,y1=0):
        self.metodo=metodo
        match metodo:
            case 1:
                self.x=x
                self.y=y
                self.height=height
                self.width=height
            case 2:
                self.x=(x-((height)/2))
                self.y=(y-((height)/2))
                self.height=height
                self.width=height
            case 3:
                self.x=x
                self.y=y
                self.width=abs(x-x1)
                self.height=abs(y-y1)
                a=0
                b=0
                if self.x>x1:
                    a=self.x
                    self.x=x1
                    x1=a
                if self.y>y1:
                    b=self.y
                    self.y=y1
                    y1=b


Rectangulo1=Rectangulo(metodo=1,x=2,y=2,height=10,width=20)
Rectangulo2=Rectangulo(metodo=3,x=2,y=2,x1=0,y1=0)
Cuadrado1=Cuadrado(metodo=1,x=2,y=2,height=3)
Cuadrado2=Cuadrado(metodo=3,x=2,y=2,x1=-1,y1=-1)
print("El area del rectangulo es de:" + str(Rectangulo1.compute_area()) + "cm^2")
print("El perimetro del rectangulo es de:" + str(Rectangulo1.compute_perimeter()) + "cm")
print("El area del rectangulo es de:" + str(Rectangulo2.compute_area()) + "cm^2")
print("El perimetro del rectangulo es de:" + str(Rectangulo2.compute_perimeter()) + "cm")
print("El area del perimetro es de:" + str(Cuadrado1.compute_area()) + "cm^2")
print("El perimetro del cuadrado es de:" + str(Cuadrado1.compute_perimeter()) + "cm")
if Cuadrado2.compute_interference_point(pointx=0,pointy=0)==0:
    print("El punto esta fuera del cuadrado")
else:
    print("El punto esta dentro del cuadrado")

Rectangulo3=Rectangulo(metodo=4,Lineo1=Linea1,Lineo2=Linea2,Lineo3=Linea3,Lineo4=Linea4)
print(Rectangulo3.compute_area())
```


# Restaurante

Ahora nos encontramos en una situacion de un restaurante donde debemos calcular la cuenta de la orden de un cliente

### Diagrama de clases

Antes de empezar a programar debemos plantear como seria la estructura de lo que vamos a programar y como se relacionan las clases entre ellas, asi obtenemos el siguiente diagrama de clases

Empezamos con la clase orden, que se compone de items del menu; en esta clase se pueden, añadir items, calcular el total de la cuenta y mostrar la cuenta

La siguiente clase, los items del menu, que se compodria de nombre, precio y cantidad, y que puede calcular el sub_total, que seria la cantidad del item por el precio del item

Y luego estan las subclases qye heredan de items del menu, que serian las categorias que podria a llegar un menu, y que cada una tiene sus caracteristicas propias
![image](https://github.com/JOUNAL/Reto3/blob/main/Reto_3/Diagrama2(1).png)

