import socket
import psutil

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))

while True:
    # Pega as estatísticas do cpu
    cpu = str(psutil.cpu_freq())
    # Calcula a informação da memória
    memory = psutil.virtual_memory()
    # Converte bytes em MB (Bytes -> KB -> MB)
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    mem_info = str(available) + 'MB Livre / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'

    # Calcula informação do disco
    disk = psutil.disk_usage('/')
    # Converte bytes em GB (Bytes -> KB -> MB -> GB)
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    disk_info = str(free) + 'GB Livre / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
  
    x = input('Digite o que quer enviar:\n')
    entrance = x.split(' ')

    # identifica aqui qual é o "tipo" da mensagem
    if entrance[0].lower() == 'post':

      # se é mem, vai mandar informações da memória
      if entrance[1].lower() == 'mem':
        package = x + ' ' + mem_info

        s.sendall(str.encode(package)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

      # se é cpu, vai mandar informações do cpu
      if entrance[1].lower() == 'cpu':
        package = x + ' ' + cpu
        s.sendall(str.encode(package)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

      # se é disk, vai mandar informações do disco rígido
      if entrance[1].lower() == 'disk':
        package = x + ' ' + disk_info
        s.sendall(str.encode(package)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

    # se é um get, vai mandar de qualquer forma e o servidor vai identificar se tem algo errado
    elif entrance[0].lower() == 'get':
        s.sendall(str.encode(x)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()

    # vai mandar alguma coisa se não é nulo
    elif entrance[0].lower() != '':
        s.sendall(str.encode(x)) 
        data = s.recv(4096)
        print()
        print('O servidor respondeu com: ', data.decode())
        print()


    # se é nulo, vai fechar a conexão
    if not str.encode(x):
        s.close()
        break 