from abc import ABC, abstractmethod

class BasePath(ABC):
    
    @abstractmethod
    def get_reference(self, state) -> dict:
        """
        根据当前状态返回参考点
        Args:
            state: 当前状态 {'x', 'y', 'yaw', 'v'}
        Returns:
            参考点 {'x', 'y', 'yaw', 'v'}
        """
        
        pass