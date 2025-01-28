from dotenv import load_dotenv

load_dotenv()

ECOSYSTEM_CONFIGS = {
    "sol": {
        "native": {
            "decimals": 9,  # lamports
            "unit_name": "SOL"
        },
        "tokens": {
            "usdc": {
                "decimals": 6,
                "program_address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
            }
            # Add more Solana tokens here as needed
        },
    },
    "evm": {
        "native": {
            "decimals": 18,  # wei
            "unit_name": "ETH"
        },
        "tokens": {
            "arbitrum": {
                "usdc": {
                    "contract_address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
                    "decimals": 6
                },
                "usdt": {
                    "contract_address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
                    "decimals": 6
                }
            },
            "bsc": {
                "usdt": {
                    "contract_address": "0x55d398326f99059fF775485246999027B3197955",
                    "decimals": 18
                }
            },
            "ethereum": {
                "usdt": {
                    "contract_address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                    "decimals": 6
                }
            }
            # Add more ERC20 tokens here as needed
        },
    },
    "sui": {
        "native": {
            "decimals": 9,  # mist
            "unit_name": "SUI"
        },
        "tokens": {
            "usdc": {
                "decimals": 6,
                "program_address": "0xdba34672e30cb065b1f93e3ab55318768fd6fef66c15942c9f7cb846e2f900e7::usdc::USDC"
            }
            # Add more SUI tokens here as needed
        },
    },
    "apt": {
        "native": {
            "decimals": 8, # octa
            "unit_name": "APT"
        },
    },
    "ton": {
        "native": {
            "decimals": 9,  # nanotons
            "unit_name": "TON"
        },
        "tokens": {
            "usdt": {
                "decimals": 6,
                "program_address": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs"
            }
            # Add more TON jettons here as needed
        },
    },
    "btc": {
        "native": {
            "decimals": 8,  # satoshis
            "unit_name": "BTC"
        },
    }
}
