import socket
import secrets

server = socket.socket()

def keyExchangePicker(clientKeyExchange):
    keyExchangeList = ['staticdiffiehellman', 'ephemeraldiffiehellman']
    choice = ''
    for i in range(0,len(clientKeyExchange)):
        if clientKeyExchange[i] == 1:
            while(True):
                res = input('Do you want to use' + keyExchangeList[i] + '? (y/n): ')
                if res == 'y':
                    choice += '1'
                    while(len(choice)<4):
                        choice += '0'
                    return choice
                elif res == 'n':
                    choice += '0'
                    break
                else:
                    print('invalid choice')
    return choice


def cipherSuitePicker(clientCipherSuite):
    cipherSuiteList = ['des3', 'des', 'toydes']
    choice = ''
    for i in range(0,len(clientCipherSuite)):
        if clientCipherSuite[i] == 1:
            while(True):
                res = input('Do you want to use' + cipherSuiteList[i] + '? (y/n): ')
                if res == 'y':
                    choice += '1'
                    while(len(choice)<4):
                        choice += '0'
                    return choice
                elif res == 'n':
                    choice += '0'
                    break
                else:
                    print('invalid choice')
    return choice

def hashPicker(clientHashChoice)
    hashList = ['sha1']
    choice = ''
    for i in range(0,len(clientHashChoice)):
        if clientHashChoice[i] == 1:
            while(True):
                res = input('Do you want to use' + clientHashChoice[i] + '? (y/n): ')
                if res == 'y':
                    choice += '1'
                    while(len(choice)<4):
                        choice += '0'
                    return choice
                elif res == 'n':
                    choice += '0'
                    break
                else:
                    print('invalid choice')
    return choice

while(True):
    host = input("Friend's IP (127.0.0.1 if local): ")
    try:
        socket.inet_aton(host)
        break
    except socket.error:
        print("Invalid IP address")

while(True):
    try:
        port = int(input("Friend's port (12345 if they choose default or greater if custom): "))
    except:
        print("Invalid port provided")
    
    if(port<12345):
        print("Invalid port provided")
    else:
        break

client.connect((host,port))
while(True):
    #Phase 1
    client.send(1024)

    timestamp = #THIS NEEDS TO BE DONE
    nonce = secrets.randbits(224)

    clientKeyExchanges = server.recv(1)
    keyExchange = keyExchangePicker(clientKeyExchanges)
    server.send(keyExchange)

    clientCipherSuites = server.recv(1)
    cipherSuite =  cipherSuitePicker(clientCipherSuites)
    server.send(cipherSuite)

    clientHashChoices = server.recv(1)
    hashChoice = hashPicker(clientHashChoices)
    server.send(hashChoices)

    #Phase 2
    keyExchange(client, keyExchange, 0)


    #Phase 3



    #Phase 4