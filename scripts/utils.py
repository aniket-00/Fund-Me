from brownie import FundMe, MockV3Aggregator, accounts, network, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from":get_account()}
        )
    print("Mocks Deployed")
    
