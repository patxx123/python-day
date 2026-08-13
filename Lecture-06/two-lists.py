import random
rows = 3
cols = 4

def main():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for i in range(rows):
        for a in range(cols):
            values[i][a] = random.randint(1,100)
            
    print(values)
main()