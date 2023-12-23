from abc import ABC, abstractmethod


class IMapFunc(ABC):
    """Interface for map functions."""

    @abstractmethod
    def __call__(self, y: float) -> float:
        """Map a value y to another value y."""
        pass
