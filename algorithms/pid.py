from algorithms.base_algorithms import BaseAlgorithm
from math import sin, cos, pi

class Pid(BaseAlgorithm):
    
    def __init__(self):
        
        self.kp_yaw = 20.0
        self.kd_yaw = 0.0
        self.kp_d = 0.0
        self.kp_v = 0.5
        
        self.prev_e_yaw = 0.0
        self.dt = 0.1
        
    def compute(self, state, reference) -> dict:
        """
        根据当前状态和参考点计算控制量
        Args:
            state:     当前状态 {'x', 'y', 'yaw', 'v'}
            reference: 参考点   {'x', 'y', 'yaw', 'v'}
        Returns:
            控制量 {'steering', 'accel'}
        """
        
        x_now = state['x']
        y_now = state['y']
        yaw_now = state['yaw']
        
        x_ref = reference['x']
        y_ref = reference['y']
        yaw_ref = reference['yaw']
        
        v_now = state['v']
        v_ref = reference['v']
        
        e_yaw = yaw_ref - yaw_now
        if e_yaw > pi:
            e_yaw -= 2 * pi
        if e_yaw < -pi:
            e_yaw += 2 * pi
    
        e_d = (x_ref - x_now) * sin(yaw_ref) - (y_ref - y_now) * cos(yaw_ref)  
        d_term = (e_yaw - self.prev_e_yaw) / self.dt
        self.prev_e_yaw = e_yaw
        
        e_v = v_ref - v_now
        
        steering = self.kp_yaw * e_yaw + self.kd_yaw * d_term + self.kp_d * e_d
        max_steer = 0.5
        steering = max(-max_steer, min(max_steer, steering))
        accel    = self.kp_v * e_v  
        
        return {
            'steering': steering,
            'accel':    accel,
            'e_d':      e_d,
            'e_yaw':    e_yaw
        }