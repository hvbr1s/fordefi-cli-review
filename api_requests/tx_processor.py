from decimal import Decimal
from dotenv import load_dotenv
from configs.ecosystem_configs import ECOSYSTEM_CONFIGS
from api_requests.tx_constructor_native import (evm_tx_native, sol_tx_native, sui_tx_native, ton_tx_native, aptos_tx_native, btc_tx_native)
from api_requests.tx_constructor_tokens import evm_tx_tokens, sol_tx_tokens, sui_tx_tokens, ton_tx_jettons

load_dotenv()

def process_transaction(ecosystem, evm_chain, vault_id, destination, value, custom_note, token):

    # 1) Grab the ecosystem config
    eco_config = ECOSYSTEM_CONFIGS.get(ecosystem)
    if not eco_config:
        raise ValueError(f"Ecosystem '{ecosystem}' is not supported.")

    # 2) Sanitize the value
    try:
        value = Decimal(value.replace(",", "."))
    except Exception:
        raise ValueError(f"Invalid amount provided: '{value}'")

    # 3) Native vs. Token logic
    if not token:
        # ---- NATIVE COIN TRANSFER ----
        # We wecide which native tx builder to call
        tx_functions = {
            "sol": sol_tx_native,
            "evm": evm_tx_native,
            "sui": sui_tx_native,
            "ton": ton_tx_native,
            "apt": aptos_tx_native,
            "btc": btc_tx_native
        }
        builder = tx_functions.get(ecosystem)
        if not builder:
            raise ValueError(f"No native TX builder found for {ecosystem}.")

        # EVM native has a different signature that requires an extra evm argument that represents the network (ethereum, bsc, arbitrum, optimism, etc)
        if ecosystem == "evm":
            return builder(evm_chain, vault_id, destination, custom_note, str(value))
        else:
            return builder(vault_id, destination, custom_note, str(value))

    else:
        # 4b) Token logic
        if ecosystem == "evm":
            #-----ERC20------
            evm_config = ECOSYSTEM_CONFIGS["evm"]
            if evm_chain not in evm_config["tokens"]:
                raise ValueError(f"Chain '{evm_chain}' is not supported in EVMC config.")

            chain_tokens = evm_config["tokens"][evm_chain]
            if token not in chain_tokens:
                raise ValueError(f"Token '{token}' is not supported on chain '{evm_chain}'.")

            token_info = chain_tokens[token]
            contract_address = token_info["contract_address"]
            decimals = token_info["decimals"]
            
            # Convert to on-chain value
            multiplier = Decimal(10) ** decimals
            on_chain_value = str(int(Decimal(value) * multiplier))

            # Call function to build json
            return evm_tx_tokens(
                evm_chain, vault_id, destination, custom_note, on_chain_value, contract_address
            )

        elif ecosystem == "sol":
            #-----SPL------
            sol_config = ECOSYSTEM_CONFIGS["sol"]
            if token not in sol_config["tokens"]:
                raise ValueError(f"Token '{token}' is not supported on Solana.")

            token_info = sol_config["tokens"][token]
            program_address = token_info["program_address"]
            decimals = token_info["decimals"]

            multiplier = Decimal(10) ** decimals
            on_chain_value = str(int(Decimal(value) * multiplier))

            return sol_tx_tokens(
                vault_id, destination, custom_note, on_chain_value, program_address
            )
        elif ecosystem == "sui":
            #-----Coins------
            sui_config = ECOSYSTEM_CONFIGS["sui"]
            if token not in sui_config["tokens"]:
                raise ValueError(f"Token '{token}' is not supported on SUI.")

            token_info = sui_config["tokens"][token]
            program_address = token_info["program_address"]
            decimals = token_info["decimals"]

            multiplier = Decimal(10) ** decimals
            on_chain_value = str(int(Decimal(value) * multiplier))

            return sui_tx_tokens(
                vault_id, destination, custom_note, on_chain_value, program_address
            )
        
        elif ecosystem == "ton":
            #-----Jettons------
            ton_config = ECOSYSTEM_CONFIGS["ton"]
            if token not in ton_config["tokens"]:
                raise ValueError(f"Token '{token}' is not supported on SUI.")

            token_info = ton_config["tokens"][token]
            program_address = token_info["program_address"]
            decimals = token_info["decimals"]

            multiplier = Decimal(10) ** decimals
            on_chain_value = str(int(Decimal(value) * multiplier))

            return ton_tx_jettons(
                vault_id, destination, custom_note, on_chain_value, program_address
            )

        else:
            raise ValueError(f"No token TX builder found for ecosystem '{ecosystem}'.")