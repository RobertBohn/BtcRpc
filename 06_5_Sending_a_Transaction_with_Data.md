```
# 6.5: Sending a Transaction with Data

utxo_txid = '5d49b596fd537c4b62716ecab58b11b83e7fbe3599a7dc6fbe6eaff617fde266'
utxo_vout = 0
changeaddress = rpc_connection.getrawchangeaddress()
amount = 0.01989
op_return_data="000013131313130000"

inputs = [ { 'txid' : utxo_txid, 'vout' : utxo_vout } ]
outputs = { 'data' : op_return_data, changeaddress : amount }

rawtx = rpc_connection.createrawtransaction(inputs,outputs)
signedtx = rpc_connection.signrawtransactionwithwallet(rawtx)
print(rpc_connection.sendrawtransaction(signedtx['hex']))
```
