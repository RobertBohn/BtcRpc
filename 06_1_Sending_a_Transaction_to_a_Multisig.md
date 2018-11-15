```
# 6.1: Sending a Transaction with a Multisig

# on remote machine 
address1 = rpc_connection.getnewaddress()   # 2MtpRbPXEcGcPgGj4byxFuPnUBL6NPF8jJx
address1info = rpc_connection.getaddressinfo(address1)
addr1pubkey = address1info['pubkey']        # 02b5b98618335c76f6a2efb63e84e7207a102c249189426a6fbccbd249a24c1192

# on my machine 
address2 = rpc_connection.getnewaddress()    # 2N4H9NKtsTWzGFyPaSorYVXqcevgjK3uCyW
address2info = rpc_connection.getaddressinfo(address2)
addr2pubkey = address2info['pubkey'] # 025517bda3de56cf0e9279d4a3e9975f46c34bb8199cc404956e7b21dd46f7a1fd

# create a 2 of 2 multisig
addresses = [addr1pubkey, addr2pubkey]  
multisig = rpc_connection.createmultisig(2, addresses) 
address = multisig['address'] # 2N3S2zoLdM3GZjy5iPNzgnu8cspqR2M28Jr
redeemScript = multisig['redeemScript']   # 522102b5b98618335c76f6a2efb63e84e7207a102c249189426a6fbccbd249a24c119221025517bda3de56cf0e9279d4a3e9975f46c34bb8199cc404956e7b21dd46f7a1fd52ae

# send funds to the multisig address
rpc_connection.sendtoaddress(address, 0.02) # 5bedc0b46500989e0395400e2505e240a2be573c1448e14dedf926162c8db9af
```
