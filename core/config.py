from web3 import Web3

USE_ALL_TOKEN_BALANCE = True
RPC_URL = "testnet.dplabs-internal.com"
ROUTER_ADDRESS = Web3.to_checksum_address("0xa6b579684e943f7d00d616a48cf99b5147fc57a5")
DELAY_SWAP = 2
DELAY_ERROR = 5
MAX_RETRY = 3
SLIPPAGE = 0.01
GAS_LIMIT = 300000
GAS_PRICE = 0.0035
GAS_MULTIPLIER = 1.1
BASE_TOKEN = "PHRS"
MIN_NATIVE_BALANCE = 0.0001
SWAP_PERCENTAGE = 0.3

GTE_TOKENS = {
    "PHRS": {"address": Web3.to_checksum_address("0xacb0366aaba8440277c4d0615bf4ac60b34cccd2"), "decimals": 18},
    "USDC": {"address": Web3.to_checksum_address("0xad902cf99c2de2f1ba5ec4d642fd7e49cae9ee37"), "decimals": 18},
    
    "ETH": {"address": None, "decimals": 18},
}

ERC20_ABI = '[{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"type":"function"}]'
ROUTER_ABI = '[{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}]'
