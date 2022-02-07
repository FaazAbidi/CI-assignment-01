
from abc import ABC, abstractmethod

class Problem(ABC):
    """
    This is an abstract class for a problem. This will just act as parent class for all problems.
    """
    def __init__(self):
        this.data = {}
        this.initial_population = []