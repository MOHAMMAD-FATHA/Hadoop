import sys

for line in sys.stdin:

    # Removing white spaces
    line=line.strip()

    # Splitting the lines.
    entry=line.split(',')

    key=entry[0]
    value=line[1:]

    if key=='a':
        print(f"{key}\t{value}")

    elif key == 'b':
        print(f'{key}\t{value}')
