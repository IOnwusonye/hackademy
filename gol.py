import random


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

