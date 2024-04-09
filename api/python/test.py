# wallet_creation.py
import os
import ecdsa
from ecdsa import SigningKey, SECP256k1
from eth_account import Account
from solana.account import Account as SolanaAccount
# Function to create a Bitcoin wallet
def create_bitcoin_wallet():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key
    public_key = vk.to_string().hex()
    private_key = sk.to_string().hex()
    return public_key, private_key

# Function to create an Ethereum wallet
def create_ethereum_wallet():
    acct = Account.create()
    public_key = acct.address
    private_key = acct.key.hex()
    return public_key, private_key

# Function to create a Solana wallet
def create_solana_wallet():
    acct = SolanaAccount()
    public_key = acct.public_key()
    private_key = acct.secret_key()
    return public_key, private_key

# Test the wallet creation functions
def test_wallet_creation():
    bitcoin_public_key, bitcoin_private_key = create_bitcoin_wallet()
    ethereum_public_key, ethereum_private_key = create_ethereum_wallet()
    solana_public_key, solana_private_key = create_solana_wallet()

    print("Bitcoin Wallet:")
    print("Public Key:", bitcoin_public_key)
    print("Private Key:", bitcoin_private_key)
    print()

    print("Ethereum Wallet:")
    print("Public Key:", ethereum_public_key)
    print("Private Key:", ethereum_private_key)
    print()

    print("Solana Wallet:")
    print("Public Key:", solana_public_key)
    print("Private Key:", solana_private_key)
    print()

if __name__ == "__main__":
    test_wallet_creation()
