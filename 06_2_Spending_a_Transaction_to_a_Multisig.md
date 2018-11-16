```
# 6.2: Spending a Transaction with a Multisig

# collect data from the creation
address1 = '2MtpRbPXEcGcPgGj4byxFuPnUBL6NPF8jJx'
addr1pubkey = '02b5b98618335c76f6a2efb63e84e7207a102c249189426a6fbccbd249a24c1192'

address2 = '2N4H9NKtsTWzGFyPaSorYVXqcevgjK3uCyW'
addr2pubkey = '025517bda3de56cf0e9279d4a3e9975f46c34bb8199cc404956e7b21dd46f7a1fd'

address = '2N3S2zoLdM3GZjy5iPNzgnu8cspqR2M28Jr'
redeem_script = '522102b5b98618335c76f6a2efb63e84e7207a102c249189426a6fbccbd249a24c119221025517bda3de56cf0e9279d4a3e9975f46c34bb8199cc404956e7b21dd46f7a1fd52ae' 

utxo_txid = '5bedc0b46500989e0395400e2505e240a2be573c1448e14dedf926162c8db9af'

# import the address. note: this will likely timeout, so wait until it clears to continue
rpc_connection.importaddress(address)

# get unspent tx data
unspent = rpc_connection.listunspent(1,9999999,[address])
for utxo in unspent:
    if (utxo['txid'] == utxo_txid):
        utxo_vout = utxo['vout']
        utxo_spk = utxo['scriptPubKey']
        amount = utxo['amount']

recipient = rpc_connection.getrawchangeaddress()
fee = 0.0001

# create raw transaction
inputs = [{'txid':utxo_txid,'vout':utxo_vout}]
outputs = {recipient : round(float(amount)-fee,8) }
rawtx = rpc_connection.createrawtransaction(inputs,outputs)

# sign on first machine
privkey = rpc_connection.dumpprivkey(address1)
prevtxs = [{'txid': utxo_txid, 'vout': utxo_vout, 'scriptPubKey': utxo_spk, 'redeemScript': redeem_script}]
privkeys = [privkey]

signedraw = rpc_connection.signrawtransactionwithkey(rawtx,privkeys,prevtxs)
signedraw1 = signedraw['hex']

# sign on second machine
privkey = rpc_connection.dumpprivkey(address2)
prevtxs = [{'txid': utxo_txid, 'vout': utxo_vout, 'scriptPubKey': utxo_spk, 'redeemScript': redeem_script}]
privkeys = [privkey]

signedraw = rpc_connection.signrawtransactionwithkey(signedraw1,privkeys,prevtxs)
signedraw2 = signedraw['hex']

# send it
print(rpc_connection.sendrawtransaction(signedraw2))  
```
