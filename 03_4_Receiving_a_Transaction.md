```
# 3.4: Receiving a Transaction

# get unconfirmed balance
print('unconfirmed balance: ', rpc_connection.getunconfirmedbalance())

# get your balance
balance = rpc_connection.getbalance()
print('confirmed balance: ', balance)

# get your balance with x confirmations - I can't get this to work - any suggestions?
confirmations = 9
balance = rpc_connection.getbalance("*", 9)
print('balance with %d confirmations: %d' % (confirmations, balance))

# get wallet information
# variables: walletname, walletversion, balance, unconfirmed_balance, immature_balance, txcount, keypoololdest, 
#     keypoolsize, keypoolsize_hd_internal, paytxfee, hdseedid, hdmasterkeyid, private_keys_enabled
walletinfo = rpc_connection.getwalletinfo()
print('balance: ', walletinfo['balance'])
print('wallet version: ', walletinfo['walletversion'])
print('transaction count: ', walletinfo['txcount'])
print('paytxfee: ', walletinfo['paytxfee'])
print('keypoololdest: ', datetime.date.fromtimestamp( walletinfo['keypoololdest'] ))

# get transactions
# transaction variables: address, category, amount, label, vout, confirmations, blockhash, blockindex, blocktime, 
#     txid, walletconflicts[], time, timereceived, bip125-replaceable
transactions = rpc_connection.listtransactions()
print('transactions: ', len(transactions))
print('amount: ', transactions[0]['amount'])
print('confirmations: ', transactions[0]['confirmations'])
print('txid: ', transactions[0]['txid'])
print('vout: ', transactions[0]['vout'])
print('time: ', transactions[0]['time'])
print('category: ', transactions[0]['category'])

# list unspent
# unspent variables: txid, vout, address, label, scriptPubKey, amount, confirmations, spendable, solvable, safe
unspent = rpc_connection.listunspent()
print('unspent: ', len(unspent))
print('address: ', transactions[0]['address'])

# examine a transaction - getrawtransaction - verbose
# variables: txid, hash, version, size, vsize, weight, locktime, vin[], vout[], hex, blockhash, confirmations, 
#     time, blocktime
rawtransaction = rpc_connection.getrawtransaction(transactions[0]['txid'], 1)
print('inputs: ', len(rawtransaction['vin']))
print('outputs: ', len(rawtransaction['vout']))
```
