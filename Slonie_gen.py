import sys

count_elephants = 0
mass_elephants = []
initial_elephant_order = []
target_elephant_order = []


INF = 1000000000
MAXN = 1000000
minw = INF

def getInputs():
    filename = "zadanie_B/slo3.in"
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
target_elephant_order = [x - 1 for x in next(g)]

p_x = [0] * (count_elephants[0] )

for i in range(len(p_x)):
    p_x[initial_elephant_order[i]] = initial_elephant_order[target_elephant_order.index(initial_elephant_order[i])]

minw = min(mass_elephants)

is_visited = [False] * (count_elephants[0] + 1)

def is_visited_gen():
    for i in is_visited:
        yield is_visited[i]


#----------------  Main Algorithm ----------------

wynik = 0
wynik_list = []

def algorith_gen():
    for i in range(count_elephants[0]):

        min_cycle_mass = INF
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

            wynik_list = min(suma + (cycle_length-2)*min_cycle_mass, suma + min_cycle_mass + (cycle_length+1) * minw )
    yield wynik_list

_w = algorith_gen()



wynik = wynik + next(_w)
    
print(wynik)

