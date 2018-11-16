```
# 6.4: Sending a Transaction with a Locktime

utxo_txid = '5bedc0b46500989e0395400e2505e240a2be573c1448e14dedf926162c8db9af'
utxo_vout = 1
recipient = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
changeaddress = rpc_connection.getrawchangeaddress()
amount = 0.01478

inputs = [ { 'txid': utxo_txid, 'vout': utxo_vout } ]
outputs = { recipient: amount }
locktime = rpc_connection.getblockcount() + 2

rawtx = rpc_connection.createrawtransaction(inputs,outputs,locktime)
signedtx = rpc_connection.signrawtransactionwithwallet(rawtx)

print('locktime', locktime)
while True:
    try:
        balance = rpc_connection.getbalance()
        blocks = rpc_connection.getblockcount()
        tx = rpc_connection.sendrawtransaction(signedtx['hex'])
        print('balance', balance, 'blocks', blocks, 'date', datetime.now())    
        print('tx', tx)
        break
    except JSONRPCException:    
        print('balance', balance, 'blocks', blocks, 'date', datetime.now())    
        sleep(10)
        
print('Done!')
```
