from typing import Dict, NamedTuple
from eth_utils import decode_hex
from utils.constants import (
    MIN_DEPOSIT_AMOUNT,
    MAX_DEPOSIT_AMOUNT,
    PULSECHAIN_MIN_DEPOSIT_AMOUNT,
    PULSECHAIN_MAX_DEPOSIT_AMOUNT,
)

DEPOSIT_CLI_VERSION = '2.5.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes

    @property
    def MAX_DEPOSIT_AMOUNT(self) -> int:
        if self.NETWORK_NAME.lower().startswith('pulsechain'):
            return PULSECHAIN_MAX_DEPOSIT_AMOUNT
        return MAX_DEPOSIT_AMOUNT

    @property
    def MIN_DEPOSIT_AMOUNT(self) -> int:
        if self.NETWORK_NAME.lower().startswith('pulsechain'):
            return PULSECHAIN_MIN_DEPOSIT_AMOUNT
        return MIN_DEPOSIT_AMOUNT


MAINNET = 'mainnet'
GOERLI = 'goerli'
PRATER = 'prater'
SEPOLIA = 'sepolia'
ZHEJIANG = 'zhejiang'
PULSECHAIN = 'pulsechain'
PULSECHAIN_DEVNET = 'pulsechain-devnet'
PULSECHAIN_TESTNET_V4 = 'pulsechain-testnet-v4'


# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))
# PulseChain
PulseChainSetting = BaseChainSetting(
    NETWORK_NAME=PULSECHAIN,
    GENESIS_FORK_VERSION=bytes.fromhex('00000369'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('3357ba0018a2582aeabe4ae847aa17d50a3a99aaeb66293c01f80a83aecd0c90'))
# PulseChain Devnet
PulseChainDevnetSetting = BaseChainSetting(
    NETWORK_NAME=PULSECHAIN_DEVNET,
    GENESIS_FORK_VERSION=bytes.fromhex('20000089'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4aedc10744730347aa6c22010bd781a4f32e8369e06c788da4bfdadd11c816fe'))
# PulseChain Testnet V4
PulseChainTestnetV4Setting = BaseChainSetting(
    NETWORK_NAME=PULSECHAIN_TESTNET_V4,
    GENESIS_FORK_VERSION=bytes.fromhex('00000943'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d81664ba97279a6fa0832041b4aee6009172b4750a99467ff670a9faf3a34e64'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
    PULSECHAIN: PulseChainSetting,
    PULSECHAIN_DEVNET: PulseChainDevnetSetting,
    PULSECHAIN_TESTNET_V4: PulseChainTestnetV4Setting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
