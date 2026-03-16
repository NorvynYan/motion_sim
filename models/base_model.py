from abc import ABC, abstractmethod

class BaseModel(ABC):
    
    @abstractmethod
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
        pass