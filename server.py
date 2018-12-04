import socket
import secrets
import keyEncryption
import keyExchange

def keyExchangePicker(clientKeyExchange):
    keyExchangeList = ['staticdiffiehellman', 'ephemeraldiffiehellman', 'rsakeygeneration']
    choice = ''
    for i in range(0,len(clientKeyExchange)):
        if clientKeyExchange[i] == '1':
            while(True):
                res = input('Do you want to use ' + keyExchangeList[i] + '? (y/n): ')
                if res == 'y':
                    choice += '1'
                    while(len(choice)<3):
                        choice += '0'
                    return keyExchangeList[i], choice
                elif res == 'n':
                    choice += '0'
                    break
                else:
                    print('invalid choice')
        choice += '0'
    return choice


def cipherSuitePicker(clientCipherSuite):
    cipherSuiteList = ['des3', 'des', 'textbookrsa']
    choice = ''
    for i in range(0,len(clientCipherSuite)):
        if clientCipherSuite[i] == '1':
            while(True):
                res = input('Do you want to use ' + cipherSuiteList[i] + '? (y/n): ')
                if res == 'y':
                    choice += '1'
                    while(len(choice)<3):
                        choice += '0'
                    return cipherSuiteList[i], choice
                elif res == 'n':
                    choice += '0'
                    break
                else:
                    print('invalid choice')
        choice += '0'
    return choice

def hashPicker(clientHashChoice):
    hashList = ['sha1']
    choice = ''
    for i in range(0,len(clientHashChoice)):
        if clientHashChoice[i] == '1':
            while(True):
                res = input('Do you want to use ' + hashList[i] + '? (y/n): ')
                if res == 'y':
                    choice += '1'
                    while(len(choice)<3):
                        choice += '0'
                    return hashList[i], choice
                elif res == 'n':
                    choice += '0'
                    break
                else:
                    print('invalid choice')
        choice += '0'
    return choice


if __name__ == '__main__':
    port = int(input('port: '))
    server = socket.socket()
    server.bind(('', port))
    server.listen(5)
    while(True):
        client, addr = server.accept()
        print('Got a connection from ', addr)

        #Phase 1

        #timestamp #THIS NEEDS TO BE DONE
        nonce = secrets.randbits(224)

        clientKeyExchanges = client.recv(3).decode()
        keyExchanges, binary = keyExchangePicker(clientKeyExchanges)
        client.send(binary.encode())

        clientCipherSuites = client.recv(3).decode()
        cipherSuite, binary =  cipherSuitePicker(clientCipherSuites)
        client.send(binary.encode())

        clientHashChoices = client.recv(3).decode()
        hashChoice, binary = hashPicker(clientHashChoices)
        client.send(binary.encode())

        #Phase 2
        sessionInfo = keyExchange.main(client, keyExchanges, 0)

        #Phase 4 
        print("You're in... waiting on buddies message")
        while(True):
            c = client.recv(1024).decode()
            m = keyEncryption.main(client, cipherSuite, sessionInfo, c, False)
            print("%s: %s" %(addr, m))
            m = input('>>> ')
            c = keyEncryption.main(client, cipherSuite, sessionInfo, m, True)
            client.send(c.encode())