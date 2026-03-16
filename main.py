from models.bicycle_model import BicycleModel
from paths.l_shape import LShape
from algorithms.pid import Pid
from visualizer import Visualizer

model = BicycleModel()
path  = LShape()
pid   = Pid()
vis   = Visualizer(path.path_points)

state      = {'x': 0.0, 'y': 0.0, 'yaw': 0.0, 'v': 0.0}
trajectory = []

while True:
    ref = path.get_reference(state)
    if ref is None:
        break
    control    = pid.compute(state, ref)
    state      = model.update(state, control, dt=0.1)
    trajectory.append((state['x'], state['y']))
    vis.update(state, trajectory)