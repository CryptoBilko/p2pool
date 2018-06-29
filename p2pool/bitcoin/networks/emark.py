import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'e4e8e9e5'.decode('hex')
P2P_PORT = 5556
ADDRESS_VERSION = 53
RPC_PORT = 6666
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'eMarkaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*210000000
POW_FUNC = data.hash256
BLOCK_PERIOD = 120 # s
SYMBOL = 'DEM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'eMark') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/eMark/') if platform.system() == 'Darwin' else os.path.expanduser('~/.eMark'), 'eMark.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://185.194.142.165:3001/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://185.194.142.165:3001/ext/getaddress/'
TX_EXPLORER_URL_PREFIX = 'http://185.194.142.165:3001/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
