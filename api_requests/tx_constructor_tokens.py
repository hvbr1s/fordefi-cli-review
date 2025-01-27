def evm_tx_tokens(evm_chain, vault_id, destination, custom_note, on_chain_value, contract_address):

    request_json = {
        "signer_type": "api_signer",
        "type": "evm_transaction",
        "details": {
            "type": "evm_transfer",
            "gas": {
              "type": "priority",
              "priority_level": "medium"
            },
            "to": destination,
            "value": {
               "type": "value",
               "value": on_chain_value
            },
            "asset_identifier": {
                 "type": "evm",
                 "details": {
                     "type": "erc20",
                     "token": {
                         "chain": f"evm_{evm_chain}_mainnet",
                         "hex_repr": contract_address
                     }
                 }
            }
        },
        "note": custom_note,
        "vault_id": vault_id
    }
    return request_json


def sol_tx_tokens(vault_id, destination, custom_note, on_chain_value, program_address):

    request_json = {
        "signer_type": "api_signer",
        "type": "solana_transaction",
        "details": {
            "type": "solana_transfer",
            "to": destination,
            "value": {
                "type": "value",
                "value": on_chain_value
            },
            "asset_identifier": {
                "type": "solana",
                "details": {
                    "type": "spl_token",
                    "token": {
                        "chain": "solana_mainnet",
                        "base58_repr": program_address
                    }
                }
            }
        },
        "note": custom_note,
        "vault_id": vault_id
    }
    return request_json

def sui_tx_tokens(vault_id, destination, custom_note, on_chain_value, program_address):

    request_json = {
        "signer_type": "api_signer",
        "type": "sui_transaction",
        "details": {
            "type": "sui_transfer",
            "to": {
                "type": "hex",
                "address": destination
            },
            "value": {
                "type": "value",
                "value": on_chain_value
            },
            "gas_config": {
                "payment": []
            },
            "asset_identifier": {
                "type": "sui",
                "details": {
                    "type": "coin",
                    "coin_type": {
                        "chain": "sui_mainnet",
                        "coin_type_str": program_address,
                    },
                }
            }
        },
        "note": custom_note,
        "vault_id": vault_id
    }
    return request_json

def ton_tx_jettons(vault_id, destination, custom_note, on_chain_value, program_address):

    request_json = {
        "signer_type": "api_signer",
        "type": "ton_transaction",
        "details": {
            "type": "ton_transfer",
            "to": {
                "type": "hex",
                "address": destination
            },
            "value": {
                "type": "value",
                "value": on_chain_value
            },
            "asset_identifier": {
                "type": "ton",
                "details": {
                    "type": "jetton",
                    "jetton": {
                        "chain": "ton_mainnet",
                        "address": program_address,
                    },
                }
            }
        },
        "note": custom_note,
        "vault_id": vault_id
    }
    return request_json