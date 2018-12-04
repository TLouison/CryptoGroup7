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

def hashPicker(clientHashChoice):
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


if __name__ == '__main__':
    port = 12345
    server = server.socket()
    server.bind(('', port))
    server.listen(5)
    while(True):
        client, addr = server.accept()
        print('Got a connection from ', addr)

        #Phase 1

        timestamp = #THIS NEEDS TO BE DONE
        nonce = secrets.randbits(224)

        clientKeyExchanges = client.recv(1)
        keyExchange = keyExchangePicker(clientKeyExchanges)
        client.send(keyExchange)

        clientCipherSuites = client.recv(1)
        cipherSuite =  cipherSuitePicker(clientCipherSuites)
        client.send(cipherSuite)

        clientHashChoices = client.recv(1)
        hashChoice = hashPicker(clientHashChoices)
        client.send(hashChoices)

        #Phase 2
        keyExchange.main(client, keyExchange, 0)


        #Phase 3 (might be uneeded)


        #Phase 4 