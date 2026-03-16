import matplotlib.pyplot as plt
from math import cos, sin

class Visualizer:
    def __init__(self, path_points):
        self.path_points = path_points
        
        # 左1大图，右3小图
        self.fig = plt.figure(figsize=(20, 10))
        self.ax_map   = self.fig.add_subplot(1, 3, 1)
        self.ax_v     = self.fig.add_subplot(3, 3, 2)
        self.ax_acc   = self.fig.add_subplot(3, 3, 5)
        self.ax_steer = self.fig.add_subplot(3, 3, 8)
        self.ax_ev    = self.fig.add_subplot(3, 3, 3)
        self.ax_ed    = self.fig.add_subplot(3, 3, 6)
        self.ax_eyaw  = self.fig.add_subplot(3, 3, 9)
        plt.ion()
        plt.tight_layout(pad=3.0)

    def update(self, state, trajectory, control_history):
        # 清屏
        
        self.ax_map.cla()
        self.ax_v.cla()
        self.ax_acc.cla()
        self.ax_steer.cla()
        self.ax_ev.cla()
        self.ax_ed.cla()
        self.ax_eyaw.cla()
        
        # 左图：轨迹
        self.ax_map.plot(self.path_points[:, 0], self.path_points[:, 1], 'r--', label='reference')
        if len(trajectory) > 1:
            xs = [p[0] for p in trajectory]
            ys = [p[1] for p in trajectory]
            self.ax_map.plot(xs, ys, 'b-', label='actual')
        x   = state['x']
        y   = state['y']
        yaw = state['yaw']
        self.ax_map.annotate('',
            xy=(x + 5*cos(yaw), y + 5*sin(yaw)),
            xytext=(x, y),
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
        self.ax_map.axis('equal')
        self.ax_map.grid(True)
        self.ax_map.legend()
        self.ax_map.set_title('Trajectory')

        # 右图：时间轴
        t = list(range(len(control_history)))

        # 速度
        vs = [s['v'] for s in control_history]
        self.ax_v.plot(t, vs, 'b-')
        self.ax_v.set_ylabel('v (m/s)')
        self.ax_v.set_title('Velocity')
        self.ax_v.grid(True)

        # 加速度
        accs = [c['accel'] for c in control_history]
        self.ax_acc.plot(t, accs, 'g-')
        self.ax_acc.set_ylabel('accel (m/s²)')
        self.ax_acc.set_title('Acceleration')
        self.ax_acc.grid(True)

        # 转向角
        steers = [c['steering'] for c in control_history]
        self.ax_steer.plot(t, steers, 'r-')
        self.ax_steer.set_ylabel('steering (rad)')
        self.ax_steer.set_title('Steering')
        self.ax_steer.grid(True)
        
        # 速度误差
        evs = [h['e_v'] for h in control_history]
        self.ax_ev.plot(t, evs, 'b-')
        self.ax_ev.set_ylabel('e_v (m/s)')
        self.ax_ev.set_title('Velocity Error')
        self.ax_ev.grid(True)

        # 横向偏差
        eds = [h['e_d'] for h in control_history]
        self.ax_ed.plot(t, eds, 'g-')
        self.ax_ed.set_ylabel('e_d (m)')
        self.ax_ed.set_title('Lateral Error')
        self.ax_ed.grid(True)

        # 航向角误差
        eyaws = [h['e_yaw'] for h in control_history]
        self.ax_eyaw.plot(t, eyaws, 'r-')
        self.ax_eyaw.set_ylabel('e_yaw (rad)')
        self.ax_eyaw.set_title('Heading Error')
        self.ax_eyaw.grid(True)
        
        plt.pause(0.01)