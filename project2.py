
from web3 import Web3
from lxml import html
import requests
import random
import sys
from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL


z = 1
while True:
    magic = "0000000000000000000000000000000000000000000000000000000000000000"
    while len(magic) < 64:
        magic = "0" + magic
    magic = magic[:64-len(str(hex(z)[2:]))] + str(hex(z)[2:])
    PRIVATE_KEY = str(magic)
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    privatekey = hdwallet.private_key()
    ethaddr = hdwallet.p2pkh_address()
    f = open('eth.txt', "r")
    z +=1
    mumbai_rpc_url = "https://ethereum.atomicwallet.io/"
    web3 = Web3(Web3.HTTPProvider(mumbai_rpc_url))
    balance = web3.eth.get_balance(ethaddr)
    BAL = balance
    print("balance = " + str(BAL))
    while line := f.readline():
            print(line[:42] , ethaddr , privatekey)
            if ethaddr == line[:42] :
              print('Write Information Wallet On File Winner (MMDRZA.Com)')
              print('==========================[Mmdrza.Com]================================')
              print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
              fileone = open("ethATOMICWINEEEEEEERRRRRRRRRRRRRRRRRRRRRRR.txt","a")
              fileone.write('\nADDRESS ETH      : ' + ethaddr)
              fileone.write('\nPrivate Key ETH   : ' + privatekey)
              fileone.write('\nValue TX   ETH   : ' )
              fileone.write('\n=====================[ MMDRZA.CoM ]===========================\n')
              fileone.close()
              print('Saved and Write All Details For WiN Wallet')
              continue
    if int(BAL) > 0:
        print('Write Information Wallet On File Winner (MMDRZA.Com)')
        print('==========================[Mmdrza.Com]================================')
        print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
        f1 = open("ethATOMICWINEEEEEEERRRRRRRRRRRRRRRRRRRRRRR.txt","a")
        f1.write('\nADDRESS ETH      : ' + ethaddr)
        f1.write('\nPrivate Key ETH   : ' + privatekey)
        f1.write('\nValue TX   ETH   : ' + str(BAL))
        f1.write('\n=====================[ MMDRZA.CoM ]===========================\n')
        f1.close()
        print('Saved and Write All Details For WiN Wallet')
        #tx = web3.tx(rawTransaction)
        #tx.sign( privatekey )
        #serializedTx = tx.serialize()
        #err = KeyError
        #web3.eth.send_raw_transaction('0x' + serializedTx.to_string('hex'), function(err, hash))
        #Print("Transaction Done")
        continue
    f.close()
    print(z)
    
        
