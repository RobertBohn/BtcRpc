```
# 3.3: Setting Up Your Wallet

# create an address for receiving payments
address = rpc_connection.getnewaddress('', 'legacy')
print('new address: ', address)

# sign a message using the new address
signature = rpc_connection.signmessage(address, 'Hello, World')
print('signature: ', signature)

# verify the message
result = rpc_connection.verifymessage(address, signature, 'Hello, World')
print('verify: ', result)

# skipping: backupwallet, importwallet, dumpwallet, dumpprivkey, importprivkey
```
