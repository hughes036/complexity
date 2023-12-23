from abc import ABC, abstractmethod


class IMapFunc(ABC):
    """Interface for map functions."""

    def __call__(self, y: float) -> float:
        """Map a value y to another value y."""
        try:
            return self.interate(y)
        except RuntimeWarning:
            # TODO how to handle RuntimeWarning: overflow encountered in scalar power (produces 'inf' value)
            # for some reason, this is not caught by the except clause
            return float("inf")
    @abstractmethod
    def interate(self, y: float) -> float:
        """Iterate the map function once."""
        return self.__call__(y)
