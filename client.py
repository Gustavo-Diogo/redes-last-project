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

class requisition:
  def __init__(self, name, age):
    self.name = name
    self.age = age



s.connect((HOST,PORT))

while True:
    x = input('Digite o que quer enviar:\n')
    entrance = x.split(' ')


    if entrance[0].lower() == 'post':

      if entrance[1].lower() == 'mem':
        package = x + ' ' + mem_info

        s.sendall(str.encode(package)) 
        data = s.recv(1024)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

      if entrance[1].lower() == 'cpu':
        package = x + ' ' + cpu
        s.sendall(str.encode(package)) 
        data = s.recv(1024)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

      if entrance[1].lower() == 'disk':
        package = x + ' ' + disk_info
        s.sendall(str.encode(package)) 
        data = s.recv(1024)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

    elif entrance[0].lower() == 'get':
        s.sendall(str.encode(x)) 
        data = s.recv(1024)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()
      # if not (entrance[1].lower() != 'mem' or entrance[1].lower() != 'gpu' or entrance[1].lower() != 'disk'):
      #   print('first if')
      #   if entrance[2].lower()!= 0:
      #     s.sendall(str.encode(x))
      #   else:
      #     print('está errado')
      # else:
      #     print('está errado')

    elif entrance[0].lower() != '':
        s.sendall(str.encode(x)) 
        data = s.recv(1024)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()


    if not str.encode(x):
        s.close()
        break 

    
    
