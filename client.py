import socket
import psutil

# Get cpu statistics
cpu = str(psutil.cpu_stats()) + '%'

# Calculate memory information
memory = psutil.virtual_memory()
# Convert Bytes to MB (Bytes -> KB -> MB)
available = round(memory.available/1024.0/1024.0,1)
total = round(memory.total/1024.0/1024.0,1)
mem_info = str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'

# Calculate disk information
disk = psutil.disk_usage('/')
# Convert Bytes to GB (Bytes -> KB -> MB -> GB)
free = round(disk.free/1024.0/1024.0/1024.0,1)
total = round(disk.total/1024.0/1024.0/1024.0,1)
disk_info = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'

# print("CPU Info--> ", cpu)
# print("Memory Info-->", mem_info)
# print("Disk Info-->", disk_info)
# 10.2.170.39

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



s.connect((HOST,PORT))

while True:

    # Get cpu statistics
    cpu = str(psutil.cpu_stats()) + '%'

    # Calculate memory information
    memory = psutil.virtual_memory()
    # Convert Bytes to MB (Bytes -> KB -> MB)
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    mem_info = str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'

    # Calculate disk information
    disk = psutil.disk_usage('/')
    # Convert Bytes to GB (Bytes -> KB -> MB -> GB)
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    disk_info = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'

  
    x = input('Digite o que quer enviar:\n')
    entrance = x.split(' ')

    #here identifies what's the "type" of the message
    if entrance[0].lower() == 'post':

      #if it's mem, it's gonna send mem informations
      if entrance[1].lower() == 'mem':
        package = x + ' ' + mem_info

        s.sendall(str.encode(package)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

      #if it's cpu, it's gonna send cpu informations
      if entrance[1].lower() == 'cpu':
        package = x + ' ' + cpu
        s.sendall(str.encode(package)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

      #if it's disk, it's gonna send disk informations
      if entrance[1].lower() == 'disk':
        package = x + ' ' + disk_info
        s.sendall(str.encode(package)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

    #if it's a get, it's gonna send it anyway, the server is going to identifies if anything is wrong
    elif entrance[0].lower() == 'get':
        s.sendall(str.encode(x)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

    #it's gonna send anything if it's not null
    elif entrance[0].lower() != '':
        s.sendall(str.encode(x)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()


    if not str.encode(x):
        s.close()
        break 

    
    
