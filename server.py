import socket, threading

HOST = 'localhost'
PORT = 50000
serverKeeper = True


# armazenamento dos dados de memória RAM, HD e uso do cpu
memList  = []
diskList = []
cpuList = []

# instancia socket tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa a um endereço e porta
s.bind((HOST, PORT))

# começa a escutar requisições
s.listen()

memList  = []
diskList = []
cpuList = []

#classe criada para armanezar os dados como nome e informações recebidas do cliente como armazenamento interno, memoria e cpu
class Info:
    def __init__(self, username, info):
        self.name = username
        self.info = info

print('Aguardando Conexões!')

#function that identifies connection
def handle_client(conn) :
    print('Um dispositivo conectado')
    x = 0

    # fica conectado ao cliente enquanto for necessário
    while True :
        # variável usilizada para identificar se a resposta referente à requisição atual já foi enviara de volta
        sent_back = False

        # recebe informação
        data = conn.recv(4096)

        # trata a mensagem recebida
        entrance = str(data.decode()).split(' ')

        # enviar informações de volta ao cliente sobre como fazer a requisição
        if entrance[0].lower()=='help':
            conn.sendall(b'\nTIPOS DE MENSAGEM:\npost {mem/disk/cpu} {your_name}\nget {mem/disk/cpu} {name}')

        try:
           
            # faz tratamento para mensagem do tipo post
            if entrance[0].lower() == 'post':

                # faz tratamento para mensagem do tipo post de memória ram
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
                    

                # faz tratamento para mensagem do tipo post de HD
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

                # faz tratamento para mensagem do tipo post de CPU
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

            # faz tratamento para mensagem do tipo get
            if entrance[0].lower() == 'get':

                # get informações de memória ram
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
            
                # get de informações de disco rígido
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

                # get de informações do uso do CPU
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
            
            # se a requisição foi feita de maneira incorreta e as condições anteriores não foram atendidas, ele retorna para
            # o cliente um aviso de mensagem mal formulada
            if not sent_back :
                conn.sendall(b'Mensagem mal formulada')
        
            # se a mensagem estiver vazia, encerra o servidor
            if not data:
                print('fechando conexão')
                conn.close()
                break
        except:
            conn.sendall(b'Mensagem mal formulada')


# fica recebendo novas requisições de conexão de novos clientes.
while serverKeeper: 
    conn, addres = s.accept()
    
    # quando a conecão é aceita, inicia-se a troca de mensagens
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
    
