# Programming with Bitcoin Core

## Introduction
I wanted to take a deep dive into Bitcoin. So I'm working through Christopher Allen's [Learning Bitcoin from the Command Line](https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line) tutorial. At the same time I wanted to learn how to program Bitcoin in Python using Jeff Garzik's [python-bitcoinrpc](https://github.com/jgarzik/python-bitcoinrpc). This project is the resulting examples and notes from that process.

## Requirements
I set up a test-net version of Bitcoin. Installed python-bitcoinrpc. For my examples I start the main python code with these lines:

```
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging, datetime

logging.basicConfig()
logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)

rpc_host = '127.0.0.1'
rpc_port = '18332'
rpc_user = 'bitcoinrpc'
rpc_password = 'my-password'

rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
```

**PART TWO: BITCOIN-CLI**

* [3.3: Setting Up Your Wallet](03_3_Setting_Up_Your_Wallet.md)
* [3.4: Receiving a Transaction](03_4_Receiving_a_Transaction.md)
* [4.1: Sending Coins the Easy Way](04_1_Sending_Coins_The_Easy_Way.md)
* [4.2: Creating a Raw Transaction](04_2_Creating_a_Raw_Transaction.md)
* [4.4: Sending Coins with Raw Transactions](04_4_Sending_Coins_with_a_Raw_Transaction.md)
* [5.2: Resending a Transaction with RBF](05_2_Resending_a_Transaction_with_RBF.md)
* [5.3: Funding a Transaction with CPFP](05_3_Funding_a_Transaction_with_CPFP.md)
* [6.1: Sending a Transaction with a Multsig](06_1_Sending_a_Transaction_to_a_Multisig.md)
* [6.2: Spending a Transaction with a Multsig](06_2_Spending_a_Transaction_to_a_Multisig.md)
* [6.4: Sending a Transaction with a Locktime](06_4_Sending_a_Transaction_with_a_Locktime.md)
* [6.5: Sending a Transaction with Data](06_5_Sending_a_Transaction_with_Data.md)

**PART THREE: BITCOIN SCRIPTING**

