import pystorms
import numpy as np
import pytest


def test_alpha():
    """
    Tests for Alpha Scenario
    """
    # Initalize your environment
    env = pystorms.scenarios.alpha()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 28
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps


def test_beta():
    """
    Tests for Beta Scenario
    """
    # Initalize your environment
    env = pystorms.scenarios.beta()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 7
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps


def test_gamma():
    """
    Tests for Gamma Scenario
    """
    # Initalize your environment
    env = pystorms.scenarios.gamma()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 11
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps

    # All valves closed - remanent water in basins
    env = pystorms.scenarios.gamma()
    done = False
    while not done:
        done = env.step(np.zeros(11))
    assert env.performance() > 10 ** 5


def test_gamma_volume_halved():
    """
    Tests for Gamma Scenario, with all basins volume halved
    """
    # Initalize your environment
    env = pystorms.scenarios.gamma_volume_halved()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 11
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps

    # All valves closed - remanent water in basins
    env = pystorms.scenarios.gamma_volume_halved()
    done = False
    while not done:
        done = env.step(np.zeros(11))
    assert env.performance() > 10 ** 5


def test_gamma_1yr_volume_halved():
    """
    Tests for Gamma Scenario, with all basins volume halved over 1 year of rainfall simulation

    only run sim once bc it takes a long time
    """
    import datetime
    # Initalize your environment
    env = pystorms.scenarios.gamma_1yr_volume_halved()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 11
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps
    assert env.performance() > 10 ** 5
    assert env.data_log['simulation_time'][0] == datetime.datetime(2021, 1, 1, 0, 0, 1)
    assert env.data_log['simulation_time'][-1] == datetime.datetime(2021, 12, 31, 0, 0)


def test_theta():
    """
    Tests for Theta Scenario
    """
    # Initalize your environment
    env = pystorms.scenarios.theta()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 2
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps


def test_epsilon():
    """
    Tests for Epsilon Scenario
    """
    # Initalize your environment
    env = pystorms.scenarios.epsilon()
    done = False
    steps = 0
    while not done:
        state = env.state()
        # Check if performance measure is raising error
        if steps < 1:
            with pytest.raises(ValueError):
                env.performance()
        done = env.step()
        steps += 1
        # Check for length of state being returned
        assert len(state) == 13
        # Check if data log is working
        assert len(env.data_log["performance_measure"]) == steps

if __name__ == "__main__":
    test_alpha()
    test_beta()
    test_gamma()
    test_gamma_volume_halved()
    test_gamma_1yr_volume_halved()
    test_theta()
    test_epsilon()
