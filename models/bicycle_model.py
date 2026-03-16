from models.base_model import BaseModel
from math import cos, sin, tan

class BicycleModel(BaseModel):
    """
    运动学自行车模型
    """
    def __init__(self, L: float = 2.5):
        """
        Args:
            L: 轴距（米），默认2.5m
        """
        self.L = L

    def update(self, state: dict, control: dict, dt: float) -> dict:
        """
        更新车辆状态
        Args:
            state:   当前状态 {'x', 'y', 'yaw', 'v'}
            control: 控制输入 {'steering', 'accel'}
            dt:      时间步长（秒）
        Returns:
            新的state dict
        """
        L        = self.L
        x        = state['x']
        y        = state['y']
        yaw      = state['yaw']
        v        = state['v']
        steering = control['steering']
        accel    = control['accel']

        x   = x   + v * cos(yaw) * dt
        y   = y   + v * sin(yaw) * dt
        yaw = yaw + v / L * tan(steering) * dt
        v   = v   + accel * dt

        return {'x': x, 'y': y, 'yaw': yaw, 'v': v}