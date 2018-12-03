import socket

client = socket.socket()

def keyExchangePicker():
    keyExchangeList = ['staticdiffiehellman', 'ephemeraldiffiehellman']
    while(True):
        keyExchange = input("Pick a keyExchange method (): ")
        if keyExchange in keyExchangeList:
            return keyExchange
        else:
            print("Invalid Key Exchange Algorithm")



def cipherSuitePicker():
    cipherSuiteList = ['des3', 'des', 'toydes']
    while(True):
        cipherSuite = input("Pick a cipher suite (): ")
        if cipherSuite in cipherSuiteList:
            return cipherSuite
        else:
            print("Invalid Cipher Suite Algorithm")

def hashPicker():
    hashList = ['sha1']
    while(True):
        hashChoice = input("Pick a hash (): ")
        if hashChoice in hashList:
            return hashChoice
        else:
            print("Invalid hash Algorithm")

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

    keyExchange = keyExchangePicker()
    cipherSuite =  cipherSuitePicker()
    hashChoice = hashPicker()

    while(True):
        client.send()
        client.recv(1024)

        if(serverKeyExchange != keyExchange):
            while(True):
                res = input("Friend picked " + serverKeyExchange + " do you want to continue with this? (y/n): ")
                if(res == 'y'):
                    keyExchange = serverKeyExchange
                    break
                elif(res == 'n'):
                    while(True):
                        res = input("Do you want to try and renegotiate? (y/n): ")
                        if(res == 'y'):
                            keyExchange = keyExchangePicker()
                            break
                        elif(res == 'n'):
                            client.send('ABORT')
                            client.close()
                            return
                        else:
                            print('Invalid option')
                else:
                    print('Invalid option')
        else:
            break    

    while(True):
        client.send()
        client.recv(1024)

        if(serverCipherSuite != cipherSuite):
            while(True):
                res = input("Friend picked " + cipherSuite + " do you want to continue with this? (y/n): ")
                if(res == 'y'):
                    cipherSuite = serverCipherSuite
                    break
                elif(res == 'n'):
                    while(True):
                        res = input("Do you want to try and renegotiate? (y/n): ")
                        if(res == 'y'):
                            cipherSuite = cipherSuitePicker()
                            break
                        elif(res == 'n'):
                            client.send('ABORT')
                            client.close()
                            return
                        else:
                            print('Invalid option')
                else:
                    print('Invalid option')
        else:
            break     

    while(True):
        client.send()
        client.recv(1024)

        if(serverCipherSuite != cipherSuite):
            while(True):
                res = input("Friend picked " + cipherSuite + " do you want to continue with this? (y/n): ")
                if(res == 'y'):
                    cipherSuite = serverCipherSuite
                    break
                elif(res == 'n'):
                    while(True):
                        res = input("Do you want to try and renegotiate? (y/n): ")
                        if(res == 'y'):
                            cipherSuite = cipherSuitePicker()
                            break
                        elif(res == 'n'):
                            client.send('ABORT')
                            client.close()
                            return
                        else:
                            print('Invalid option')
                else:
                    print('Invalid option')
        else:
            break 
    #Phase 2
    