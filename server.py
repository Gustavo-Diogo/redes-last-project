import socket, threading

HOST = 'localhost'
PORT = 50000

memList  = []
diskList = []
cpuList = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

def handle_client(conn) :
    x = 0
    while True :
        sent_back = False
        data = conn.recv(1024)
        entrance = str(data.decode()).split(' ')
        print('enviou algo!')

        if entrance[0].lower()=='help':
            conn.sendall(b'\npost {mem/disk/cpu} {your_name}\nget {mem/disk/cpu} {name}')

        if entrance[0].lower() == 'post':

            if entrance[1].lower() == 'mem':
                name = entrance[2]
                memInfo =''
                x = 3
                for x in range(x,entrance.__len__(),x+1):
                    memInfo += entrance[x]
                memList.append(memInfo)
                print(memList)
            
                conn.sendall(b'Guardamos informacoes da memoria ram!')
                sent_back = True

            if entrance[1].lower() == 'disk':
                name = entrance[2]
                diskInfo =''
                x = 3
                for x in range(x,entrance.__len__(),x+1):
                    diskInfo += entrance[x]
                diskList.append(diskInfo)
                print(diskList)
            
                conn.sendall(b'Guardamos informacoes do disco!')
                sent_back = True

            if entrance[1].lower() == 'cpu':
                name = entrance[2]
                cpuInfo =''
                x = 3
                for x in range(x,entrance.__len__(),x+1):
                    cpuInfo += entrance[x]
                cpuList.append(cpuInfo)
                print(cpuList)
            
                conn.sendall(b'Guardamos informacoes da cpu!')
                sent_back = True

        if entrance[0].lower() == 'get':

            if entrance[1].lower() == 'mem':
                my_bytes = b''
                my_str = memList[0]
                result = my_bytes + my_str.encode('utf-8')
                print(result)
                conn.sendall(result)
                sent_back = True
        
            if entrance[1].lower() == 'disk':
                my_bytes = b''
                my_str = diskList[0]
                result = my_bytes + my_str.encode('utf-8')
                print(result)
                conn.sendall(result)
                sent_back = True

            if entrance[1].lower() == 'cpu':
                my_bytes = b''
                my_str = cpuList[0]
                result = my_bytes + my_str.encode('utf-8')
                print(result)
                conn.sendall(result)
                sent_back = True
        
        if not sent_back :
            conn.sendall(b'Requisicao mal feita')
    
        if not data:
            print('fechando conexão')
            conn.close()
            break

while True : 
    conn, addres = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()