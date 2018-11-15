```
# 5.3: Funding a Transaction with CPFP

# create a stuck transaction by setting a low fee and sending coin, the change address will be stuck
rpc_connection.settxfee(0.00000001)
faucet = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
print(rpc_connection.sendtoaddress(faucet, 0.011))

# use bitcoin-cli getrawtransaction 36ff96fd15b3e5b98170a5feb6e4462dadbe9414b7cc56b094f2f6ae47a6a10e 1
# to get the change amount and vout. Reduce amount by a higher fee

utxo_txid = '36ff96fd15b3e5b98170a5feb6e4462dadbe9414b7cc56b094f2f6ae47a6a10e'
utxo_vout = 1
amount = 0.03479973
recipient2 = rpc_connection.getrawchangeaddress()

# build the raw transaction by hand
inputs = [{ "txid" : utxo_txid, "vout" : utxo_vout }]
outputs = { recipient2 : amount }

rawtx = rpc_connection.createrawtransaction(inputs,outputs)
signedtx = rpc_connection.signrawtransactionwithwallet(rawtx)
print(rpc_connection.sendrawtransaction(signedtx['hex']))

# watch the transactions in a blockchain explorer until they confirm

# reset fees
rpc_connection.settxfee(0.0001)
```
