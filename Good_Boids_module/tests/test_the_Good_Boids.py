from Good_Boids_module.Update_Boids import Boids
import numpy as np
from nose.tools import assert_almost_equal, assert_greater
from nose.tools import assert_less, assert_equal, assert_sequence_equal
from numpy.testing import assert_array_equal
import os
import yaml
from Good_Boids_module.tests.record_fixtures import configuration_file


def test_Good_boids_for_regression():
    regression_data = yaml.load(open('fixture.yaml'))

    before_positions = list(regression_data["before_positions"])
    before_velocities = list(regression_data["before_velocities"])

    new_positions = list(Boids(configuration_file).get_raw_positions(before_positions, before_velocities))
    after_positions = list(regression_data["after_positions"])

    new_velocities = list(Boids(configuration_file).get_raw_velocities(before_positions, before_velocities))
    after_velocities = list(regression_data["after_velocities"])

    for i in range(len(new_positions)):
        assert_almost_equal(new_positions[0][i], after_positions[0][i], delta=0.1)
        assert_almost_equal(new_positions[1][i], after_positions[1][i], delta=0.1)
        assert_almost_equal(new_velocities[0][i], after_velocities[0][i], delta=3)
        assert_almost_equal(new_velocities[1][i], after_velocities[1][i], delta=3)

test_Good_boids_for_regression()