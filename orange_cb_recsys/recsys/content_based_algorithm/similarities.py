from abc import ABC, abstractmethod
from scipy.spatial.distance import cosine as cosine_distance
import numpy as np


class Similarity(ABC):
    """
    Class for the various types of similarity
    """
    def __init__(self):
        pass

    @abstractmethod
    def perform(self, v1: np.ndarray, v2: np.ndarray):
        """
        Calculates the similarity between v1 and v2
        """
        raise NotImplementedError


class CosineSimilarity(Similarity):
    """
    Computes cosine similarity of given numpy arrays
    """
    def __init__(self):
        super().__init__()

    def perform(self, v1: Vector, v2: Vector):
        return v1.similarity(v2)
