import keyEncryption
import keyExchange
import socket
import secrets

def keyExchangePicker():
    keyExchangeList = ['staticdiffiehellman', 'ephemeraldiffiehellman', 'rsakeygeneration']
    choices = ['0', '0', '0']
    while(True):
        keyExchangeChoice = input("Pick a keyExchange method (staticdiffiehellman, ephemeraldiffiehellman, rsakeygeneration)[quit to exit]: ")
        if keyExchangeChoice == 'quit':
            tmp = ''
            for i in choices:
                tmp += i
            return tmp
        elif keyExchangeChoice == 'staticdiffiehellman':
            choices[0] = '1'
        elif keyExchangeChoice == 'ephemeraldiffiehellman':
            choices[1] = '1'
        elif keyExchangeChoice == 'rsakeygeneration':
            choices[2] = '1'
        else:
            print("Invalid Key Exchange Algorithm")


def cipherSuitePicker():
    cipherSuiteList = ['des3', 'des', 'textbookrsa']
    choices = ['0','0','0']
    while(True):
        cipherSuite = input("Pick a cipher suite (des3, des, textbookrsa)[quit to exit]: ")
        if cipherSuite == 'quit':
            tmp = ''
            for i in choices:
                tmp += i
            return tmp
        elif cipherSuite == 'des3':
            choices[0] = '1'
        elif cipherSuite == 'des':
            choices[1] = '1'
        elif cipherSuite == 'textbookrsa':
            choices[2] = '1'
        else:
            print("Invalid Cipher Suite Algorithm")

def hashPicker():
    hashList = ['sha1']
    choices = ['0']
    while(True):
        hashChoice = input("Pick a hash (sha1): ")
        if hashChoice == 'quit':
            tmp = ''
            for i in choices:
                tmp += i
            return tmp
        elif hashChoice == 'sha1':
            choices[0] = '1'
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

    port = int(input('port: '))

    client = socket.socket()
    client.connect((host,port))
    while(True):
        #Phase 1
        #client.send(1024)

        #timestamp #THIS NEEDS TO BE DONE
        nonce = secrets.randbits(224)

        keyExchanges = keyExchangePicker()
        client.send(keyExchanges.encode())

        cipherSuites =  cipherSuitePicker()
        client.send(cipherSuites.encode())

        hashChoices = hashPicker()
        client.send(hashChoices.encode())

        keyExchanges = client.recv(3).decode()
        cipherSuites = client.recv(3).decode()
        hashChoices = client.recv(3).decode()

        while(True):
            if(keyExchanges[0] == '1'):
                currentkey = 'staticdiffiehellman'
            elif(keyExchanges[1] == '1'):
                currentkey = 'ephemeraldiffiehellman'
            elif(keyExchanges[2] == '1'):
                currentkey = 'rsakeygeneration'
            break
        
        while(True):
            if(cipherSuites[0] == '1'):
                currentSuite = '3des'
            elif(cipherSuites[1] == '1'):
                currentSuite = 'des'
            elif(cipherSuites[2] == '1'):
                currentSuite = 'textbookrsa'
            break

        while(True):
            if(hashChoices[0] == '1'):
                currentHash = 'sha1'        
            break
            
        #Phase 3 
        sessionInfo = keyExchange.main(client, currentkey, 0)

        #Phase 4
        print("You're in... talk how you like")
        while(True):
            m = input('>>> ')
            c = keyEncryption.main(client, currentSuite, sessionInfo, m, True)
            client.send(str(c).encode())
            c = str(client.recv(1024).decode())
            m = keyEncryption.main(client, currentSuite, sessionInfo, c, False)
            print("%s: %s" %(host, m))