```
# 4.1: Sending Coins the Easy Way

# return testnet bitcoin to the faucet they came from
sendto = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
amount = 0.001
balance = rpc_connection.getbalance()

# simple send
if (amount >= balance):
    # ignoring transaction fees for now
    print('don\'t have enough bitcoin to perform this send.')
    exit(0)

tx = rpc_connection.sendtoaddress(sendto, amount)
print(tx)

trans = rpc_connection.gettransaction(tx)
print(trans['details'][0]['category'])
print(trans['details'][0]['amount'])
print(trans['details'][0]['fee'])
```
