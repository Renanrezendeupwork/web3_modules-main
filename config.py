import json
from pathlib import Path

with open('abi/erc20_abi.json') as file:
    ERC20_ABI = json.load(file)
    
    
with open('abi/syncswap/classic_pool.json') as file:
    SYNCSWAP_CLASSIC_POOL_ABI = json.load(file)

with open("abi/syncswap/router.json", "r") as file:
    SYNCSWAP_ROUTER_ABI = json.load(file)
    
with open('abi/syncswap/classic_pool_data.json') as file:
    SYNCSWAP_CLASSIC_POOL_DATA_ABI = json.load(file)
    
# with open("abi/mute/router.json", "r") as file:
#     MUTE_ROUTER_ABI = json.load(file)
    
    
# with open("abi/spacefi/router.json", "r") as file:
#     SPACEFI_ROUTER_ABI = json.load(file)
    
    
    
# with open("abi/pancake/pool.json", "r") as file:
#     PANCAKE_POOL_ABI = json.load(file)
    
# with open("abi/pancake/router.json", "r") as file:
#     PANCAKE_ROUTER_ABI = json.load(file)

# with open("abi/pancake/factory.json", "r") as file:
#     PANCAKE_FACTORY_ABI = json.load(file)

# with open("abi/pancake/quoter.json", "r") as file:
#     PANCAKE_QUOTER_ABI = json.load(file)
    
    

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


SYNCSWAP_CONTRACTS = {
    "router": "0x2da10A1e27bF85cEdD8FFb1AbBe97e53391C0295",
    "classic_pool": "0xf2DAd89f2788a8CD54625C60b55cD3d2D0ACa7Cb"
}


ZKSYNC_TOKENS = {
    "ETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
    "WETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
    "USDC": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4",
    "USDT": "0x493257fd37edb34451f62edf8d2a0c418852ba4c",
    #"BUSD": "0x2039bb4116b4efc145ec4f0e2ea75012d6c0f181",
    #"MATIC": "0x28a487240e4d45cff4a2980d334cc933b7483842",
   # "OT": "0xd0ea21ba66b67be636de1ec4bd9696eb8c61e9aa",
    #"MAV": "0x787c09494ec8bcb24dcaf8659e7d5d69979ee508",
    "WBTC": "0xbbeb516fb02a01611cbbe0453fe3c580d7281011",
}


MUTE_CONTRACTS = {
    "router": "0x8B791913eB07C32779a16750e3868aA8495F5964"
}

PANCAKE_CONTRACTS = {
    "router": "0xf8b59f3c3Ab33200ec80a8A58b2aA5F5D2a8944C",
    "factory": "0x1BB72E0CbbEA93c08f535fc7856E0338D7F7a8aB",
    "quoter": "0x3d146FcE6c1006857750cBe8aF44f76a28041CCc"
}

SPACEFI_CONTRACTS = {
    "router": "0xbE7D1FD1f6748bbDefC4fbaCafBb11C6Fc506d1d"
}