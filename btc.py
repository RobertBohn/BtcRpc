import aws, json, logging
from bitcoinrpc.authproxy import AuthServiceProxy

logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.INFO)

# return testnet coins to:  mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
# testnet 403 Forbidden errors: update remote config: rpcallowip=
# bitcoind -daemon -walletrbf

def getConnection():
    secrets = json.loads(aws.get_secret(aws.MAINNET))
    return AuthServiceProxy("http://%s:%s@%s:%s"%(secrets['user'], secrets['password'], secrets['host'], secrets['port']))
