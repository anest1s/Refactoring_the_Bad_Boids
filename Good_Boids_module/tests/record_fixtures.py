import os
import yaml
from Good_Boids_module.Update_Boids import Boids

configuration_file = os.path.join(os.path.dirname(__file__), "config_test.yaml")

get = Boids(configuration_file)
before_positions = get.initial_positions().tolist()
before_velocities = get.initial_velocities().tolist()
after_positions = get.update_positions().tolist()
after_velocities = get.update_velocities().tolist()

fixture = {"before_positions": before_positions, "before_velocities": before_velocities,
           "after_positions": after_positions, "after_velocities": after_velocities}
fixture_file = open("fixture.yaml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
