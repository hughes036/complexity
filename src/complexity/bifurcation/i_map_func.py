from abc import ABC, abstractmethod


class IMapFunc(ABC):
    """Interface for map functions."""

    def __init__(self, r: float):
        self.r = r

    @abstractmethod
    def __call__(self, x: float) -> float:
        """Map a point (x, y) to another point (x, y)."""
        pass
