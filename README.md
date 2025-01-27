# Fordefi CLI

A command-line interface for broadcasting transactions using the Fordefi API.

⚠️ This tool is still in development, please test extensively with _small amounts_.

## Prerequisites

- Python 3.x
- Fordefi API User Token and API Signer (setup instructions can be found [here](https://docs.fordefi.com/developers/program-overview))

## Setup

1. Install `uv` package manager:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Set up the project and install dependencies:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   uv sync
   ```

3. Configure environment variables:
   Create a `.env` file in the root directory with your Fordefi API user token:
   ```plaintext
   FORDEFI_API_USER_TOKEN="your_token"
   ```
4. Place your API Signer's `.pem` private key file in a `/secret` directory in the root folder.

5. Start the Fordefi API Signer:
   ```bash
   docker run --rm --log-driver local --mount source=vol,destination=/storage -it fordefi.jfrog.io/fordefi/api-signer:latest
   ```
   Then select "Run signer" in the Docker container.

6. Make the script executable:
   ```bash
   chmod +x fordefi_cli.py
   ```

## Usage

```bash
./fordefi_cli --vault <VAULT_ID> --to <ADDRESS> --chain <NETWORK> --value <AMOUNT> [OPTIONS]
```

### Required Arguments

- `--vault`: The vault ID from which to send the transaction
- `--to`: The destination address
- `--chain`: Network on which to broadcast the transaction (`sol`, `evm`, `sui`, `ton`, `apt`, `btc`)
- `--value`: Amount to send

### Optional Arguments

- `--evm-chain`: Required only if ecosystem is 'evm'. Currently supported options: `arbitrum`, `optimism`, `ethereum`, `bsc`
- `--token`: Token ticker (e.g., 'usdc', 'weth'). Omit for native assets like ETH, SOL, SUI, APT, BTC, TON etc.
- `--note`: Optional custom note for the transaction.

### Example

```bash
./fordefi_cli --vault c1a0a9db-8520-45f9-ac0e-d004df2316c0 --destination 0x123... --chain evm --evm-chain arbitrum --value 1.5 --token usdc --note "Test transfer"
```

The transaction will be broadcast after confirming all details.

## This tool currently supports the following networks and assets:

- Ethereum (ETH)
- BSC (BNB and USDT)
- Arbitrum (ETH and USDC)
- Solana (SOL and USDC)
- Sui (SUI and USDC)
- Ton (TON and USDT)
- Aptos (APT coins only)
- Bitcoin


## Adding more assets

You can extend the CLI to support additional tokens and networks by modifying the `configs/ecosystem_configs.py` file. The configuration is organized by ecosystem (e.g., 'sol', 'evm') and includes settings for both native assets and tokens.

### Adding new tokens

To add a new token, locate the appropriate ecosystem and add your token configuration under the `tokens` section:

```python
# For EVM tokens:
"evm": {
    "tokens": {
        "ethereum": {  # Chain name
            "new_token": {  # Token ticker (lowercase)
                "contract_address": "0x...",  # Token contract address
                "decimals": 18  # Token decimals
            }
        }
    }
}

# For Solana tokens:
"sol": {
    "tokens": {
        "new_token": {  # Token ticker (lowercase)
            "decimals": 6,
            "program_address": "..."  # SPL token program address
        }
    }
}
```
