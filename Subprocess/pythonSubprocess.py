import subprocess

def run_cmd(args_list):
    """
    Description:
        this function execute CLI commands
    """
    print(f'Running systrm command: {args_list}')
    hadoop_process = subprocess.Popen(args_list,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = hadoop_process.communicate()
    s_return = hadoop_process.returncode
    return s_return,s_output, s_err


# version= run_cmd(['hadoop', 'version'])
# print(version)

new_directory= run_cmd(['hadoop', 'fs', '-mkdir', '/HadoopSubprocess'])
print(new_directory)
new_directory= run_cmd(['hadoop', 'fs', '-mkdir', '/HadoopSubprocess1'])


list_all_directory= run_cmd(['hadoop', 'fs', '-ls', '/'])
print(list_all_directory)

put_command= run_cmd(['hadoop', 'fs', '-put', '/home/fatha/Documents/Hadoop/Subprocess/input.txt', '/HadoopSubprocess'])
print(put_command)

copy_from_local= run_cmd(['hadoop', 'fs', '-copyFromLocal', '/home/fatha/Documents/Hadoop/Subprocess/inputHadoop.txt', '/HadoopSubprocess'])
print(copy_from_local)

cat= run_cmd(['hadoop', 'fs', '-cat', '/HadoopSubprocess/inputHadoop.txt'])
print(cat)

get= run_cmd(['hadoop', 'fs', '-get', '/HadoopSubprocess/inputHadoop.txt', '/home/fatha/Documents/Hadoop/WordCount'])
print(get)

copy_to_local= run_cmd(['hadoop', 'fs', '-copyToLocal', '/HadoopSubprocess/input1.txt', '/home/fatha/Documents/Hadoop/WordCount'])
print(copy_to_local)

remove_directory= run_cmd(['hadoop', 'fs', '-rm', '-r', '/HadoopSubprocess1'])
print(remove_directory)