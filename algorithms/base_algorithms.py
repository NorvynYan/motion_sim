from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    
    @abstractmethod
    def compute(self, state, reference) -> dict:
        """
        根据当前状态和参考点计算控制量
        Args:
            state:     当前状态 {'x', 'y', 'yaw', 'v'}
            reference: 参考点   {'x', 'y', 'yaw', 'v'}
        Returns:
            控制量 {'steering', 'accel'}
        """
        
        pass