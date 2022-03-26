from itertools import count
from mimetypes import init
import sys

count_elephants = 0
mass_elephants = []
initial_elephant_order = []
target_elephant_order = []


INF = 1000000000
MAXN = 1000000
minw = INF

def getInputs():
    filename = "zadanie_B/slo7.in"
    #filename = sys.argv[1]
    with open(filename) as file:        
        for line in file:
            lines = []
            for word in line.split():
                lines.append(int(word))
            yield lines

g = getInputs()

count_elephants = next(g)
mass_elephants = next(g)
initial_elephant_order = [x - 1 for x in next(g)]
_target_elephant_order = [x - 1 for x in next(g)]

target_elephant_order = [0] * count_elephants[0]

for i in range(count_elephants[0]):
    target_elephant_order[_target_elephant_order[i]] = initial_elephant_order[i]

print(initial_elephant_order)
print(_target_elephant_order)
print(target_elephant_order)

print("VVVVVVVVVVVVVVVVVVVV")



minw = min(mass_elephants)

print(count_elephants)
print(mass_elephants)
print(initial_elephant_order)
print(target_elephant_order)

is_visited = [False] * (count_elephants[0] + 1)

print("-------------------------")

p_x = [0] * (count_elephants[0] + 1)
print(p_x)

print("DEBUG: " + str(initial_elephant_order[1]))
print("DEBUG: " + str(target_elephant_order.index(initial_elephant_order[1])))
print("DEBUG: " + str(initial_elephant_order[target_elephant_order.index(initial_elephant_order[1])]))
print("DEBUG: " )

wynik = 0

for i in range(count_elephants[0]):
    if(is_visited[i] == False):
        min_cycle_mass = INF
        suma = 0
        cur = i
        cycle_length = 0

        while(True):
            min_cycle_mass = min(min_cycle_mass, mass_elephants[cur])
            suma += mass_elephants[cur]
            cur = target_elephant_order[cur]
            print(i)
            print("cur: " + str(cur))
            is_visited[cur] = True
            cycle_length += 1
            if(cur == i):
                break
        
        print("METODA 1: " + str(suma + (cycle_length-2)*min_cycle_mass)) 
        print("METODA 2: " + str(suma + min_cycle_mass + (cycle_length+1) * minw)) 
        print("-------------------")
        wynik += min(suma + (cycle_length-2)*min_cycle_mass, suma + min_cycle_mass + (cycle_length+1) * minw )
    
print(wynik)

p_x = [0] * (count_elephants[0] )
#print(p_x)

#print("DEBUG: " + str(initial_elephant_order[1]))
#print("DEBUG: " + str(target_elephant_order.index(initial_elephant_order[1])))
#print("DEBUG: " + str(initial_elephant_order[target_elephant_order.index(initial_elephant_order[1])]))
#print("DEBUG: " )

for i in range(len(p_x) - 1):
    p_x[initial_elephant_order[i]] = initial_elephant_order[target_elephant_order.index(initial_elephant_order[i])]

#p_x[initial_elephant_order[1]] = initial_elephant_order[target_elephant_order.index(initial_elephant_order[1])]

#print(p_x)
