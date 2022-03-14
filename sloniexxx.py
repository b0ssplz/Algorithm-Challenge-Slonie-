import math
import fileinput
from timeit import Timer
import time


count_elephants = 0
mass_elephants = []
initial_elephant_order = []
target_elephant_order = []

minw = math.inf

#----------- Reading Inputs from File -------------

file_lines = []

start = time.time()


for line in fileinput.input():
    file_lines.append(line)

count_elephants = (int(file_lines[0]))

for word in file_lines[1].split():
    mass_elephants.append(int(word))

for word in file_lines[2].split():
    initial_elephant_order.append(int(word)-1)

for word in file_lines[3].split():
    target_elephant_order.append(int(word)-1)


middle1 = time.time()    


# ----------- Algorithm's Initialization -------------

p_x = [0] * (count_elephants)

for i in range(len(p_x)):
    p_x[initial_elephant_order[i]] = initial_elephant_order[target_elephant_order.index(initial_elephant_order[i])]

middle2 = time.time()


minw = min(mass_elephants)

is_visited = [False] * (count_elephants)

#----------------  Main Algorithm LOOP ----------------

w = 0

for i in range(count_elephants):

    min_cycle_mass = math.inf
    suma = 0

    if(is_visited[i] == False):
        cycle_length = 0
        x = i

        while(True):
            suma += mass_elephants[x]
            min_cycle_mass = min(min_cycle_mass, mass_elephants[x])

            is_visited[x] = True
            x = p_x[x]
            cycle_length += 1
            if(x == i):
                break

        w += min(suma + (cycle_length-2)*min_cycle_mass, suma + min_cycle_mass + (cycle_length+1) * minw )
    
print(w)


end = time.time()

print("TIME start-middle1:" + str(middle1-start))
print("TIME middle1-middle2:" + str(middle2-middle1))

print("TIME middle2-end:" + str(end-middle2))
print("TIME start-end:" + str(end-start))
