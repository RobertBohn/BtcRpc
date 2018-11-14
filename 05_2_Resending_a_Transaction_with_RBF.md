```
# 5.2 Resending a Transaction with RBF

# NOTE: remember to use: bitcoind -daemon -walletrbf

# set fee low
print('set super low fee:', rpc_connection.settxfee(0.0000001))

# send coin
faucet = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
tx = rpc_connection.sendtoaddress(faucet, 0.013)
print('original tx:', tx)
 
# increase default fee
print('reset fee:', rpc_connection.settxfee(0.0001))

# do the replace by fee
rbf = rpc_connection.bumpfee(tx)
print('new tx:', rbf['txid'])
print('oldfee', rbf['origfee'])
print('newfee:', rbf['fee'])
```
