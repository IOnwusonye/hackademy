import math

import datetime

import os

import random


def hello(a_name):
  print("Hello! " + a_name)

def hello2(name_a,name_b):
  print("Hello! " + name_a + " and " + name_b)

def sum_two(x,y):
  z = x + y
  return z


def circle_area(radius):
  y = radius ** 2 * math.pi
  return y
print(circle_area(2))
#wenn man diesen code importiert: z = code.circle_area(2) danach print(z) oder print(code.circle_area(2))

r = float(input("Give me a radius, please: "))
z = circle_area(r) #code. ... weil function von directory code importiert
print(z)
#oder
print("The area is " + str(z))
#ohne das float wäre der radius, den der user eingibt ein string und strings können nicht berechnet werden

def today():
  now = datetime.datetime.now()
  return now.day

  day_number = today()
  print("Today is " + str(day_number) + " in the month")

#function um (in diesem fall) bereiche von bildern zu drehen
def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image

#function um bilder schwarz-weiss zu machen
def to_grayscale(an_image):
  grayscale_im = an_image.convert('L')
  return grayscale_im

#function um die summe aller elemente einer liste zu ermitteln
def my_sum(a_list):
  total = 0
  for n in a_list:
    total = total + n
  return total

#function um das produkt aller elemente einer liste zu ermitteln
def my_product(a_list):
  total = 1
  for n in a_list:
    total = total * n
  return total

#wieviele elemente besitzt eine liste
def my_count(a_list):
  total = 0
  for n in a_list:
    total = total + 1
  return total

#wieviele elemente einer liste sind kleiner als 5
def my_count_less_5(a_list):
  count = 0
  for n in a_list:
    if n > 5:
      count = count + 1
  return count

#wieviele 1 besitzt eine liste
def my_count_ones(a_list):
  count = 0
  for n in a_list:
    if n == 1:
      count = count + 1
  return count

#grösstes element einer liste bestimmen
def my_max(a_list):
  if is_list_empty(a_list):
    return None
  b = 0
  for n in a_list:
    if n > b:
      b = n
  return b
#zum ausführen der function; the_max = code.my_max(a_list) und dann print(the_max)

#wenn eine liste 0 elemente hat wird False angezeigt, sonst True
def is_list_empty(a_list):
  if my_count(a_list) == 0:
    return True
  else:
    return False


def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  print("list of file names:")
  print(list_of_files)
  print("-------------------")
  all_files = []
  for filename in list_of_files:
    full_path = os.path.join(a_dirname,filename)
    if not os.path.isdir(full_path): #damit nicht die ordner genannt werden
      all_files.append(full_path)
  return all_files
#zum ausführen der function; print(code.get_filenames("C:\\Users\\IOnwusonye\\Desktop"))

def print_right(a_list_with_lists):
  for n in a_list_with_lists:
    if isinstance(n,list):
      for i in n:
        print(i,end='')
      print('')
    else:
      print(n)
#a_list = [12,34,[56,67],78]
#print_right(a_list)

#um anzuzeigen was der user eingibt: number = int(input("Give me a number: "))
def single_row_stars(number):
  for n in range(number):
    print("*",end="")

def single_row_of(number,string):
  for n in range(number):
    print(string,end="")

#um anzuzeigen was der user eingibt: number = int(input("Give me a number: "))
def square_of_stars(num):
  for n in range(num):
    for m in range(num):
      print("*",end="")
    print("")

#um anzuzeigen was der user eingibt: number = int(input("Give me a number: "))
def rectangle_of_stars(rows,cols):
  for n in range(rows):
    for m in range(cols):
      print("*",end="")
    print("")

#elemente in einer liste x2 und neue liste daraus machen
def list_by_2(a_list):
  new_list = []
  for n in a_list:
    new_list.append(n * 2)
  return new_list


def create_grid(size):
  new_grid = []
  for row in range(size):
    new_subgrid = []
    for column in range (size):
      new_subgrid.append("-")
    new_grid.append(new_subgrid)
  return new_grid

def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid,max_alive)


def get_empty_grid(size):
  new_grid = []
  for r in range(size):
    new_subgrid = []
    for c in range (size):
      new_subgrid.append("-")
    new_grid.append(new_subgrid)
  return new_grid


def rand_alive():
    number = random.randint(1,3)
    if number == 1:
        return True
    else:
        return False


def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size):
            if (remaining > 0) and (rand_alive() == True):
                a_grid[r_i][c_i] = "x"
                remaining = remaining - 1
            else:
                a_grid[r_i][c_i] = "-"

a_grid = get_empty_grid(3)
fill_grid_random(a_grid,10)
print(fill_grid_random)

def print_grid(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i][c_i],end="")
        print("")



a = ["x","y","z","r"]

l = len(a)

for i in range(l):
    a[i] = "rrr"


#um die elemente zweier funktionen zu vergleichen und anzugeben, ob es gemeinsame elemente hat
def is_duplicate_there(list_a,list_b):
    return (len(set(list_a).intersection(list_b)) == 0)
#oder
def is_duplicate_there2(list_a,list_b):
    for i in list_a:
        if (i in list_b):
            return True
    return False

