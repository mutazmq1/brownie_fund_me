from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    active_netowrk = network.show_active()
    if (
        active_netowrk in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or active_netowrk in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Loading mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
        print("Mocks deployed...")
