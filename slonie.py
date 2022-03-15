import math
import fileinput
import numpy as np
import os
from joblib import Parallel, delayed
import tempfile

count_elephants = np.int64(0)

mass_elephants_ = []
initial_elephant_order_ = []
target_elephant_order_ = []

minw = math.inf

#----------- Reading Inputs from File -------------

file_lines = []

for line in fileinput.input():
    file_lines.append(line)

count_elephants = (int(file_lines[0]))

for word in file_lines[1].split():
    mass_elephants_.append(int(word))

for word in file_lines[2].split():
    initial_elephant_order_.append(int(word)-1)

for word in file_lines[3].split():
    target_elephant_order_.append(int(word)-1)
    
mass_elephants = np.array(mass_elephants_, dtype=np.int64)
initial_elephant_order = np.array(initial_elephant_order_, dtype=np.int64)
target_elephant_order = np.array(target_elephant_order_, dtype=np.int64)

# ----------- Algorithm's Initialization -------------

path = tempfile.mkdtemp()
memmap_path = os.path.join(path,'ab3.mmap')

p_x = np.zeros(count_elephants, dtype = np.int64)

def process(i):   
    p_x_memmap[int(initial_elephant_order[i])] = int(initial_elephant_order[int(np.where(target_elephant_order == initial_elephant_order[i])[0][0])])

p_x_memmap = np.memmap(memmap_path, dtype=np.int64, shape=(np.size(p_x)), mode='w+')
Parallel(n_jobs=-2)(delayed(process)(i) for i in range(0,np.size(p_x)))
p_x[:] = p_x_memmap[:]

minw = min(mass_elephants)

is_visited = np.full(count_elephants,False)

#----------------  Main Algorithm Loop ----------------

TWO = np.int64(2)
ONE = np.int64(1)

w = np.int64(0)

for i in range(count_elephants):

    min_cycle_mass = math.inf
    suma = np.int64(0)
    

    if(is_visited[i] == False):
        cycle_length = np.int64(0)
        x = np.int64(i)

        while(True):
            suma += mass_elephants[x]
            min_cycle_mass = min(min_cycle_mass, mass_elephants[x])
            
            is_visited[x] = True
            x = p_x[x]
            cycle_length += ONE
            if(x == i):
                break

        w += min(suma + (cycle_length-TWO)*min_cycle_mass, suma + min_cycle_mass + (cycle_length+ONE) * minw )
    
print(w)