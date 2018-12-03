import socket
import secrets
import keyEncryption
import keyExchange


client = socket.socket()

def keyExchangePicker():
    keyExchangeList = ['staticdiffiehellman', 'ephemeraldiffiehellman']
    choices = []
    while(True):
        keyExchange = input("Pick a keyExchange method ()[quit to exit]: ")
        if keyExchange == 'quit':
            return choices
        if keyExchange in keyExchangeList:
            choices.append(keyExchange)
        else:
            print("Invalid Key Exchange Algorithm")



def cipherSuitePicker():
    cipherSuiteList = ['des3', 'des', 'toydes']
    choices = []
    while(True):
        cipherSuite = input("Pick a cipher suite ()[quit to exit]: ")
        if cipherSuite == 'quit':
            return choices
        if cipherSuite in cipherSuiteList:
            choices.append(cipherSuite)
        else:
            print("Invalid Cipher Suite Algorithm")

def hashPicker():
    hashList = ['sha1']
    choices = []
    while(True):
        hashChoice = input("Pick a hash (): ")
        if hashChoice == 'quit':
            return choices
        if hashChoice in hashList:
            choices.append(hashChoice)
        else:
            print("Invalid hash Algorithm")


if __name__ == '__main__':
    while(True):
        host = input("Friend's IP (127.0.0.1 if local): ")
        try:
            socket.inet_aton(host)
            break
        except socket.error:
            print("Invalid IP address")

    port = 12345
    '''
    while(True):
        try:
            port = int(input("Friend's port (12345 if they choose default or greater if custom): "))
        except:
            print("Invalid port provided")
        
        if(port<12345):
            print("Invalid port provided")
        else:
            break
    '''

    client.connect((host,port))
    while(True):
        #Phase 1
        client.send(1024)

        timestamp = #THIS NEEDS TO BE DONE
        nonce = secrets.randbits(224)

        keyExchanges = keyExchangePicker()
        client.send(keyExchange)

        cipherSuites =  cipherSuitePicker()
        client.send(cipherSuite)

        hashChoices = hashPicker()
        client.send(hashChoices)

        keyExchange = client.recv(1)
        cipherSuite = client.recv(1)
        hashChoice = client.recv(1)
        
        #Phase 2
        keyExchange.main(client, keyExchange, 0)


        #Phase 3 (might be uneeded?)
        keyEncryption.main()


        #Phase 4