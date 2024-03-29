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
    """""          WIP
    def compute_interference_line(self,Punto1,Punto2):
        if Punto1.x != Punto2.x and Punto1.y != Punto2.y:
            if Punto1.x>Punto2.x:
                a=Punto1
                Punto1=Punto2
                Punto2=a
            pendi =(Punto2.y-Punto1.y)/(Punto2.x-Punto1.x)
            puntope=(Punto1.y)-(pendi*Punto1.x)
            cruce_y=pendi*self.x+puntope
            cruce_y2=pendi*(self.x+self.width)+puntope
            cruce_x=(self.y-puntope)/pendi
            cruce_x2=((self.y+self.height)-puntope)/pendi
            print(cruce_x,cruce_y,cruce_x2,cruce_y2,self.x,self.y,pendi,puntope)
            print(Punto1.x,Punto1.y,Punto2.x,Punto2.y)
            if (self.x<=((cruce_y-puntope)/pendi)<=(self.x+self.width)) and (self.y<=cruce_y<=(self.y+self.height)):
                print(1)
                if ((Punto1.x<=cruce_x<=Punto2.x) and (Punto1.y<=cruce_x<=Punto2.y)) or ((Punto1.x<=cruce_y<=Punto2.x) and (Punto1.y<=cruce_y<=Punto2.y)):
                    return 1
            
            elif (self.x<=cruce_x<=(self.x+self.width)) and (self.y<=((cruce_x*pendi)+puntope)<=(self.y+self.height)):
                print(2)
                if ((Punto1.x<=cruce_x<=Punto2.x) and (Punto1.y<=cruce_x<=Punto2.y)) or ((Punto1.x<=cruce_y<=Punto2.x) and (Punto1.y<=cruce_y<=Punto2.y)):
                    return 1
            elif (self.x<=((cruce_y2-puntope)/pendi)<=(self.x+self.width)) and (self.y<=cruce_y2<=(self.y+self.height)):
                print(3)
                if ((Punto1.x<=cruce_x2<=Punto2.x) and (Punto1.y<=cruce_x2<=Punto2.y)) or ((Punto1.x<=cruce_y2<=Punto2.x) and (Punto1.y<=cruce_y2<=Punto2.y)):
                    return 1
            
            elif (self.x<=cruce_x2<=(self.x+self.width)) and (self.y<=((cruce_x2*pendi)+puntope)<=(self.y+self.height)):
                print(4)
                if ((Punto1.x<=cruce_x2<=Punto2.x) and (Punto1.y<=cruce_x2<=Punto2.y)) or ((Punto1.x<=cruce_y2<=Punto2.x) and (Punto1.y<=cruce_y2<=Punto2.y)):
                    return 1
            else:
                return 0
        """
                
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