from paths.base_path import BasePath
import numpy as np
from math import atan2

class LShape(BasePath):
    """
    
    """
    
    def __init__(self):
        
        r = 10 # 半径
        spacing = 0.1 # 点间距
        
        # 生成路径
        # 第一段：
        seg1_x = np.arange(0, 190, spacing) 
        seg1_y = np.zeros(len(seg1_x))
        
        # 圆弧段：圆心在(190,-10)，从0度到90度（顺时针）
        arc_len = np.pi / 2 * r
        n_arc = int(arc_len / spacing)
        theta = np.linspace(np.pi/2, 0, n_arc)
        arc_x = 190 + r * np.cos(theta)
        arc_y = -10 + r * np.sin(theta)
        
        # 第二段:
        seg2_x = np.full(int(190 / spacing), 200) # full ，第一个参数是数组长度，第二个是填充的值，两百个点，每个点都是200
        seg2_y = np.arange(-10, -200, -spacing)[:len(seg2_x)]
        
        # 拼接
        x = np.concatenate([seg1_x, arc_x, seg2_x])
        y = np.concatenate([seg1_y, arc_y, seg2_y])
        self.path_points = np.column_stack([x,y])
               
        self.current_index = 0
        
        
    def get_reference(self, state) -> dict:
        
        # 当前位置
        x = state['x']
        y = state['y']
        
        # 找目标点索引
        
        # 找目标点只从current_index后面找
        remaining_points = self.path_points[self.current_index:]
        
        # 算距离
        dx = remaining_points[:, 0] - x  # 所有点的x差值
        dy = remaining_points[:, 1] - y  # 所有点的y差值
        distances = np.sqrt(dx**2 + dy**2)
        
        # 更新索引，只能前进
        self.current_index = np.argmin(distances) + self.current_index
        
        # 取当前点和下一个点
        target = self.path_points[self.current_index]
        next_idx = min(self.current_index + 1, len(self.path_points) - 1)
        next_target = self.path_points[next_idx]
        
        # 算方向角
        dy = next_target[1] - target[1]
        dx = next_target[0] - target[0]
        yaw = atan2(dy, dx)
        return {'x': target[0], 'y': target[1], 'yaw': yaw, 'v': 2.0}