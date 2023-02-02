from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.utils import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT
from web3 import Web3

def deploy_fund_me():
    account = get_account()
    my_address = {"from":account}
    
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(
        price_feed_address, 
        my_address, 
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print(f"Contract Deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()