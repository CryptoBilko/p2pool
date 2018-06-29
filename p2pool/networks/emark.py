from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['emark']
SHARE_PERIOD = 24 # seconds
CHAIN_LENGTH = 7*24*60*60//10 # shares
REAL_CHAIN_LENGTH = 7*24*60*60//10 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 15 # blocks
IDENTIFIER = '6012865EBAD2C803'.decode('hex') #654d61726b
PREFIX = ''.decode('hex')
P2P_PORT = 5556
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 6667
BOOTSTRAP_ADDRS = 'poolmining.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: None if 60007 <= v else 'eMark version too old. Upgrade to 1.1.0.0 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 33
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
