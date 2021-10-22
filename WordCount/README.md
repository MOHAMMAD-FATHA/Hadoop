Steps to execute word count program.

dir WordCount

Create a text file inside the created directory to store data in it.

touch input.txt nano input.txt. To edit the txt file

Create a mapper.py file to write the map function code.

nano mapper.py

Execute the mapper.py file

cat input.txt| python3 mapper.py

Create a reducer.py file to write the reduce function code. nano reducer.py

Execute the reducer.py file

cat input.txt| python3 mapper.py | sort | python3 reducer.py
