#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_from_xprivate_key():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["bitcoin"]["testnet"]["symbol"]
    )
    
    python_hdwallet.from_xprivate_key(
        xprivate_key=_["bitcoin"]["testnet"]["xprivate_key"]
    )

    assert python_hdwallet.cryptocurrency() == _["bitcoin"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["bitcoin"]["testnet"]["symbol"]
    assert python_hdwallet.network() == _["bitcoin"]["testnet"]["network"]
    assert python_hdwallet.strength() is None
    assert python_hdwallet.entropy() is None
    assert python_hdwallet.mnemonic() is None
    assert python_hdwallet.language() is None
    assert python_hdwallet.passphrase() is None
    assert python_hdwallet.seed() is None
    assert python_hdwallet.root_xprivate_key(encoded=False) is None
    assert python_hdwallet.root_xprivate_key() is None
    assert python_hdwallet.root_xpublic_key(encoded=False) is None
    assert python_hdwallet.root_xpublic_key() is None
    assert python_hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["bitcoin"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["bitcoin"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["bitcoin"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["bitcoin"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["bitcoin"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["bitcoin"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["bitcoin"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["bitcoin"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["bitcoin"]["testnet"]["finger_print"]
    assert python_hdwallet.path() is None
    assert python_hdwallet.address() == _["bitcoin"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["testnet"]

    dumps["strength"] = None
    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    dumps["seed"] = None
    dumps["root_xprivate_key"] = None
    dumps["root_xpublic_key"] = None
    dumps["path"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
