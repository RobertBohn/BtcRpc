```
# 4.2: Creating a Raw Transaction

# get starting balance 
startingbalance = rpc_connection.getbalance()

# list unspent transactions
unspent = rpc_connection.listunspent()
for utxo in unspent:
    print(utxo['txid'], ':', utxo['vout'], ' amount:', utxo['amount'])

# pick the first utxo to spend
txid = unspent[0]['txid']
vout = unspent[0]['vout']
amount = unspent[0]['amount']
fee = 0.00001

# important: use the round function when dealing with floats in python
sendamount = round(float(amount) - fee, 8)

# we're going to send this (less the fee) to another address in our wallet
sendto = rpc_connection.getnewaddress('', 'legacy')
inputs = [{ "txid" : txid, "vout" : vout }]
output = { sendto : sendamount }

# build raw transaction
rawtx = rpc_connection.createrawtransaction(inputs,output)
print('raw transaction: ', rawtx)

# validate by decoding the raw transaction
decodedtx = rpc_connection.decoderawtransaction(rawtx)
print(decodedtx)

# sign the transaction
signedtx = rpc_connection.signrawtransactionwithwallet(rawtx)
if (signedtx['complete'] != True):
    print(signedtx['complete'])
    exit(0)

# send it!
rpc_connection.sendrawtransaction(signedtx['hex'])

# get ending balance 
endingbalance = rpc_connection.getbalance()

# the difference should be the fee amount
print(startingbalance)
print(endingbalance)
```
