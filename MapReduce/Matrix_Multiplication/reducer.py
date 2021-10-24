import sys

a={}
b={}

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')
    v = value.split(',')

    if key=='a':
        a[ (int (v[1]), int (v[2]))] = int (v[3]) 
    elif key== 'b':
        b[ (int (v[1]), int (v[2]))] = int (v[3])

result=0
for i in range(0,2):
    for j in range(0,2):
        for k in range (0,2):

            result=result+a[(i,k)]*b[(k,j)]

        print(f'({i},{j})\t{result}') 
        result=0
