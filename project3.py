
from web3 import Web3
from lxml import html
import requests
import random
import sys
from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL


z = 100000000000000000
while True:
    magic = "0000000000000000000000000000000000000000000000000000000000000000"
    while len(magic) < 64:
        magic = "0" + magic
    magic = magic[:64-len(str(hex(z)[2:]))] + str(hex(z)[2:])
    PRIVATE_KEY = str(magic)
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    privatekey=hdwallet.private_key()
    addr = hdwallet.p2wsh_in_p2sh_address()
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{addr}/balance"

    response = requests.get(url)

    if response.status_code == 200:
        balance = response.json()["balance"]
        print(f"The balance of address {addr} is {balance} satoshis")
    else:
        print(f"Failed to retrieve balance for address {addr}")
    f = open('btc.txt', "r")
    z +=1
    while line := f.readline():
            print(f"The balance of address {addr} is {balance} satoshis")
            print(line , addr , privatekey)
            if addr == line :
              print('Write Information Wallet On File Winner (MMDRZA.Com)')
              print('==========================[Mmdrza.Com]================================')
              print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
              fileone = open("winner.txt","a")
              fileone.write('\nADDRESS ETH      : ' + addr)
              fileone.write('\nPrivate Key ETH   : ' + privatekey)
              fileone.write('\nValue TX   ETH   : ' )
              fileone.write('\n=====================[ MMDRZA.CoM ]===========================\n')
              fileone.close()
              print('Saved and Write All Details For WiN Wallet')
              continue
            if balance > 0:
                print(balance, "winner")
                fileone = open("winner.txt","a")
                fileone.write('\nADDRESS ETH      : ' + addr)
                fileone.write('\nPrivate Key ETH   : ' + privatekey)
                fileone.write('\nValue TX   ETH   : ' )
                fileone.write('\n=====================[ MMDRZA.CoM ]===========================\n')
                fileone.close()
                continue

        #tx = web3.tx(rawTransaction)
        #tx.sign( privatekey )
        #serializedTx = tx.serialize()
        #err = KeyError
        #web3.eth.send_raw_transaction('0x' + serializedTx.to_string('hex'), function(err, hash))
        #Print("Transaction Done")
    f.close()
    print(z)
    continue
        
