import socket, threading
from time import time

HOST = 'localhost'
PORT = 50000
serverKeeper = True

memList  = []
diskList = []
cpuList = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

class Info:
    def __init__(self, username, info):
        self.name = username
        self.info = info

print('Aguardando Conexões!')

def handle_client(conn) :
    print('Um dispositivo conectado')
    x = 0
    while True :
        sent_back = False
        data = conn.recv(4096)
        entrance = str(data.decode()).split(' ')

        if entrance[0].lower()=='help':
            conn.sendall(b'\nTIPOS DE MENSAGEM:\npost {mem/disk/cpu} {your_name}\nget {mem/disk/cpu} {name}')

        try:
           
       

            if entrance[0].lower() == 'post':

                if entrance[1].lower() == 'mem':
                    memInfo =''
                    for x in range(3,len(entrance),+1):
                        memInfo +=' '+ entrance[x]
                    
                    if not entrance[2].lower():
                        sent_back = False
                    else:
                        info = Info(entrance[2],memInfo)

                        memList.append(info)
                        conn.sendall(b'Guardamos informacoes da memoria ram!')
                        sent_back = True
                    

                if entrance[1].lower() == 'disk':
                    name = entrance[2]
                    diskInfo =''
                    x = 3
                    for x in range(3,len(entrance),+1):
                        diskInfo += ' '+entrance[x]
                    if not entrance[2].lower():
                        sent_back = False
                    else: 
                        info = Info(entrance[2],diskInfo)
                        diskList.append(info)

                        conn.sendall(b'Guardamos informacoes do disco!\n')
                        sent_back = True

                if entrance[1].lower() == 'cpu':
                    cpuInfo =''
                    x = 3
                    for x in range(3,len(entrance),+1):
                        cpuInfo += ' '+entrance[x]
                    if not entrance[2].lower():
                        sent_back = False
                    else:
                        info = Info(entrance[2], cpuInfo)
                        cpuList.append(info)
                        conn.sendall(b'Guardamos informacoes da cpu!')
                        sent_back = True

            if entrance[0].lower() == 'get':

                if entrance[1].lower() == 'mem':
                    if not entrance[2]:
                        sent_back = False

                    else:
                        my_bytes = b''
                        my_str = 'Nenhuma informação encontrada com esse nome'
                        for x in range(0, len(memList), +1):
                            if str(memList[x].name).lower() == entrance[2].lower():
                                my_str = memList[x].info

                        result = my_bytes + my_str.encode('utf-8')

                        conn.sendall(result)
                        sent_back = True
            
                if entrance[1].lower() == 'disk':
                    if not entrance[2]:
                        sent_back = False
                    
                    else:
                        my_bytes = b''
                        my_str = 'Nenhuma informação encontrada com esse nome'
                        for x in range(0, len(diskList), +1):
                            if str(diskList[x].name).lower() == entrance[2].lower():
                                my_str = diskList[x].info

                        result = my_bytes + my_str.encode('utf-8')

                        conn.sendall(result)
                        sent_back = True

                if entrance[1].lower() == 'cpu':
                    if not entrance[2]:
                        sent_back = False
                    
                    else:
                        my_bytes = b''
                        my_str = 'Nenhuma informação encontrada com esse nome'
                        for x in range(0, len(cpuList), +1):
                            if str(cpuList[x].name).lower() == entrance[2].lower():
                                my_str = cpuList[x].info

                        result = my_bytes + my_str.encode('utf-8')

                        conn.sendall(result)
                        sent_back = True
            
            if not sent_back :
                conn.sendall(b'Mensagem mal formulada')
        
            if not data:
                print('fechando conexão')
                conn.close()
                break
        except:
            conn.sendall(b'Mensagem mal formulada')



while serverKeeper: 
    conn, addres = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
    
