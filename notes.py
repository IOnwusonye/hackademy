def hello(a_name):
  print("Hello! " + a_name)

def hello2(name_a,name_b):
  print("Hello! " + name_a + " and " + name_b)

def sum_two(x,y):
  z = x + y
  return z




import code

a_name = input("What is your name?")
code.hello(a_name)

name_a = input("What is your name?")
name_b = input("What about your mates name?")
code.hello2(name_a,name_b)




import math

def circle_area(radius):
  y = radius ** 2 * math.pi
  return y
print(circle_area(2))
#wenn man diesen code importiert: z = code.circle_area(2) danach print(z) oder print(code.circle_area(2))

r = float(input("Give me a radius, please: "))
z = code.circle_area(r)
print(z)
#oder
print("The area is " + str(z))
#ohne das float wäre der radius, den der user eingibt ein string und strings können nicht berechnet werden



 

def today():
  now = datetime.datetime.now()
  return now.day

  day_number = code.today()
  print("Today is " + str(day_number) + " in the month")



#bevor man dies tun kann, muss man zuerst die pillow-library runterladen
from PIL import Image
im = Image.open("C:\\Users\\IOnwusonye\\Desktop\\pictures\\picture1.jpeg")
print(im.format, im.size, im.mode)
im.show()
#mit diesem code kann man format, grösse, mode des bildes und das bild selber anzeigen

box = (100,100,400,400)
region = im.crop(box)
transposed = region.transpose(Image.ROTATE_180)
im.paste(transposed,box)
im.show()
#mit diesem code kann man einen bereich des bildes auswählen und in diesem fall um 180° drehen und wieder ins bild einfügen


#function um (in diesem fall) bereiche von bildern zu drehen
def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image

#gehört noch zur function und beschreibt den ort wo sich die bilder befinden und welche bilder bearbeitet werden sollen
im = Image.open("C:\\Users\\IOnwusonye\\Desktop\\pictures\\picture1.jpeg")
print(im.format, im.size, im.mode)

im = rotate_box(im)

im2 = Image.open("C:\\Users\\IOnwusonye\\Desktop\\pictures\\picture2.jpg")
im2 = rotate_box(im2)

im.show()
im2.show()





a = [1,2,3]

b = ["harry","ron","hermione"]

c = [1,"harry",3.4,"blue"]

print(b[0]) #die position b0 anzeigen (0 = erste stelle der liste)

print(len(b)) #um die anzahl elemente einer liste anzuzeigen, hier der liste b

for item in b: #um alle elemente der lsite anzuzeigen
    print(item)


#bsp:
numbers = [1,2,3]

for n in numbers: #hier wird das programm nach jedem element der liste ein "ciao" anzeigen, da das "print("ciao")" noch in der function ist
    print(n)      #print(n * 2), um jedes element der liste mit 2 zu multiplizieren (funktioniert auch mit jeder anderen zahl)
    print("ciao")

print("bye")


#aufgabe: es soll die summe aller elemente der liste angegeben werden
number = [2,4,6,8,10]

total = 0

for m in number: 
    total = m + total

print(total)


#aufgabe: produkt aller elemente der liste
x = [4,5,10]

total = 1

for y in x:
    total = y * total

print(total)

# normalerweise kommen die "imports" immer am Anfang des Dokuments




import code

a = 23
b = 23

if a < b:
    print("You know what? It was true!")
else:
    print("It was acutally false!")

print("done")




import code
import os
from PIL import Image

pics = code.get_filenames(("C:\\Users\\IOnwusonye\\Desktop\\pictures"))
num = 1
for picname in pics:
    im = Image.open(picname)
    im = code.to_grayscale(im)

    newfilename = "pic_gray_" + str(num) + ".jpg"
    num = num + 1
    newfullpath = os.path.join("C:\\Users\\IOnwusonye\\Desktop\\pictures\\grayscale",newfilename)
    im.save(newfullpath)



#damit kann man (in diesem fall 10, kann aber auch eine beliebige andere zahl sein) 10x * auf derselben zeile anzeigen lassen
for n in range(10):
  print("*",end="")



#um alle elemente einer liste in einer neuen liste anzuzeigen; bsp l = ["abd","ORI","oo","PP"] --> ["abd","ORI","oo","PP"]
def list_of_strings(a_list):
    new_list = []
    for n in a_list:
        new_list.append(n.lower())
    return new_list
print(list_of_strings(l))
#oder
result = [x.lower() for x in a_list]
print(result)





#um irgendein element einer liste anzuzeigen
import random
l = [x,y,z]
def random_item(a_list):
    a = random.choice(a_list)
    return a
random_item(a_list)
#oder
def random_item2(a_list):
  a = random.sample(a_list,l)
  return a
#oder
def random_item3(a_list):
  a = random.randint(0,len(a_list)-l)
  return a_list(a)




#um das zweitgrösste element einer liste anzuzeigen
def second_max(a_list):
  new_list = []
  for n in a_list:
    if n != max(a_list):
      new_list.append(n)
  return max(new_list)

