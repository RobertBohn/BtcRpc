```
# 4.4: Sending Coins with Raw Transactions

# get starting balance 
print('starting balance ', rpc_connection.getbalance())

# get a change address
changeaddress = rpc_connection.getrawchangeaddress()
print('change address ', changeaddress)

# for this example we're going to collect all our utxo's
totalamount = 0.0
inputs = []

unspent = rpc_connection.listunspent()
for utxo in unspent:
    inputs.append({ "txid" : utxo['txid'], "vout" : utxo['vout'] })
    totalamount = totalamount + float(utxo['amount'])
   
print(round(totalamount, 8))
print(inputs)

# send 0.2 back to the faucet, set fee to 0.0001
faucet = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
tofaucet = 0.2
fee = 0.0001
change = totalamount - tofaucet - fee

outputs={ faucet : round(tofaucet,8), changeaddress: round(change,8) }
print(outputs)

# create raw transaction
rawtx = rpc_connection.createrawtransaction(inputs,outputs)

# validate by decoding the raw transaction
print(rpc_connection.decoderawtransaction(rawtx))

# sign it
signedtx = rpc_connection.signrawtransactionwithwallet(rawtx)
if (signedtx['complete'] != True):
    print('Error: ', signedtx['complete'])
    exit(0)

# send it
print(rpc_connection.sendrawtransaction(signedtx['hex']))

# ending balance should be our change amount
print('ending balance ', rpc_connection.getbalance())
```
