import random

#This function will take for example [1,1,3,2,3] and print __^-^
def print_chart(N,TheList):
    print(N+1)
    output = ""    
    for elementInTheList in TheList:
        
        if elementInTheList == 1:
            output += "_"
        elif elementInTheList == 2:
            output += "-"
        else:
            output += "^"

    print(output)

def adjacent_min(noise):
    output = []
    for i in range(len(noise) - 1):
        output.append(min(noise[i], noise[i+1]))
    return output

def noise1(mapSize = 60,N = 5,): 
    for Map in range(5):
        noise = []
        for element in range(mapSize+1):            
            noise.append(random.randint(1, 3))
            
        print_chart(Map,adjacent_min(noise))

def noise2(mapSize = 60,N = 5): 
    for Map in range(5):
        noise = []
        for element in range(mapSize+2):            
            noise.append(random.randint(1, 3))
            
        print_chart(Map,adjacent_min(adjacent_min((noise))))
        
