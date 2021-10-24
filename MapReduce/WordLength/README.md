Hadoop Version 3.3.1 Python Version 3.9.5

Create a directory to save all the files related to word length program.

mkdir WordLength

Create a text file inside the created directory to store data in it.

nano input.txt. To edit the txt file

Create a mapper.py file to write the map function code.

nano mapper.py

Execute the mapper.py file

cat input.txt| python3 mapper.py

Create a reducer.py file to write the reduce function code.

nano reducer.py

Execute the mapper.py and reducer.py file

cat input.txt| python3 mapper.py | sort | python3 reducer.py

Start all apache hadoop daemons

start-all.sh Hadoop version 3.3.1 Python version 3.9.5

Create a directory in hadoop

hadoop fs -mkdir /WordLength

Copy the data file from local system to hadoop system

hadoop fs -put /home/fatha/Documents/Hadoop/MapReduce/WordLength/input.txt /WordLength

Use the jar file, mapper and reducer file to execute the program

To find the hadoop-streaming-3.3.1.jar path execute find /home -name 'hadoop-stream*.jar'

hadoop jar /home/fatha/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar
-file /home/fatha/Documents/Hadoop/MapReduce/WordLength/mapper.py -mapper "python3 mapper.py" \ 
-file /home/fatha/Documents/Hadoop/MapReduce/WordLength/reducer.py -reducer "python3 reducer.py"
-input /Matrix/input.txt
-output /Matrix/Output

Use cat command to check the output file

hadoop fs -cat /Matrix/output/part-00000
