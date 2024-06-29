import pystorms
import pytest


def test_load_network():
    network = pystorms.networks.load_network("alpha")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("beta")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("gamma")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("gamma_1yr_normal_storages")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("gamma_1yr_volume_halved")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("gamma_volume_halved")
    assert "inp" == network[-3:]
    # I actually don't think this is used at all. Testing it anyway.
    network = pystorms.networks.load_network("new_gamma_1yr_volume_halved")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("epsilon")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("theta")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("delta")
    assert "inp" == network[-3:]
    network = pystorms.networks.load_network("zeta")
    assert "inp" == network[-3:]
    with pytest.raises(ValueError):
        pystorms.networks.load_network("purushotham")
