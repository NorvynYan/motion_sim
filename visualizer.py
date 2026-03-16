import matplotlib.pyplot as plt
from math import cos, sin 

class Visualizer:
    def __init__(self, path_points):
        # 初始化matplotlib figure
        # 存path_points用于画参考路径
        
        self.path_points = path_points
        self.fig, self.ax = plt.subplots(figsize = (8,10))
        plt.ion() # 开启交互模式，进入实时更新
        
    def update(self, state, trajectory):
        # 清屏
        # 画参考路径
        # 画历史轨迹
        # 画车辆当前位置和朝向
        # plt.pause(0.01)
        
        self.ax.cla()   # 清屏
        
        # 画参考路径
        self.ax.plot(self.path_points[:, 0], self.path_points[:, 1], 'r--', label = 'reference')
        
        # 画历史轨迹
        if len(trajectory) > 1:
            xs = [p[0] for p in trajectory]
            ys = [p[1] for p in trajectory]
            self.ax.plot(xs, ys, 'b-', label = 'actual')
            
        # 画车辆朝向箭头
        x   = state['x']
        y   = state['y']
        yaw = state['yaw']
        self.ax.annotate('', 
        xy=(x + 5*cos(yaw), y + 5*sin(yaw)),
        xytext=(x, y),
        arrowprops=dict(arrowstyle='->', color='green', lw=2))
        
        
        self.ax.axis('equal')
        self.ax.grid(True)
        self.ax.legend()
        plt.pause(0.01)