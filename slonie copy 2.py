from itertools import count
import math
import fileinput
import time
import sys
print(sys.path)
import numpy as np


count_elephants = 0
# mass_elephants = np.array([])
# initial_elephant_order = np.array([])
# target_elephant_order = np.array([])

mass_elephants_ = []
initial_elephant_order_ = []
target_elephant_order_ = []

minw = math.inf

#----------- Reading Inputs from File -------------

file_lines = []

start = time.time()


for line in fileinput.input():
    file_lines.append(line)

count_elephants = (int(file_lines[0]))

for word in file_lines[1].split():
    mass_elephants_.append(int(word))
    #mass_elephants = np.append(mass_elephants,int(word))

for word in file_lines[2].split():
    initial_elephant_order_.append(int(word)-1)
    #initial_elephant_order = np.append(initial_elephant_order,int(word)-1)

for word in file_lines[3].split():
    target_elephant_order_.append(int(word)-1)
    #target_elephant_order = np.append(target_elephant_order,int(word)-1)
    
    
middle1 = time.time()    

mass_elephants = np.array(mass_elephants_)
initial_elephant_order = np.array(initial_elephant_order_)
target_elephant_order = np.array(target_elephant_order_)


middle12 = time.time()

# ----------- Algorithm's Initialization -------------

#p_x = [0] * (count_elephants)
p_x = np.zeros(count_elephants, dtype = int)


for i in range(len(p_x)):
    # [initial_elephant_order[k] if k == ]
    #index = np.where(target_elephant_order == initial_elephant_order[i])
    #print("halo" + str(int(initial_elephant_order[index[0][0]])))
    #test = int(index[0][0])
    # print("test: " + str(test))
    # print("i: " + str(initial_elephant_order[i]))
    # print(initial_elephant_order[test])
    
    p_x[int(initial_elephant_order[i])] = int(initial_elephant_order[int(np.where(target_elephant_order == initial_elephant_order[i])[0][0])])
    #p_x[initial_elephant_order[i]] = initial_elephant_order[target_elephant_order.index(initial_elephant_order[i])]
    

middle2 = time.time()

minw = min(mass_elephants)

#is_visited = [False] * (count_elephants)
is_visited = np.full(count_elephants,False)

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
#print("TIME middle1-middle2:" + str(middle2-middle1))
print("TIME middle1-middle12:" + str(middle12-middle1))
print("TIME middle12-middle2:" + str(middle2-middle12))
print("TIME middle2-end:" + str(end-middle2))
print("TIME start-end:" + str(end-start))
