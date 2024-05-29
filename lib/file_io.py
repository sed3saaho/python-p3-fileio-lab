def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode = 'w') as f:
        f.write(file_content)
    

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode = 'a') as f:
        f.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', mode = 'r') as f:
        return f.read()

# Example usage
write_file('logfile', 'Log 1: 5 bananas added')

append_file('logfile', 'Log 2: 3 bananas added')

read_file('logfile')

print(read_file('logfile'))
    
