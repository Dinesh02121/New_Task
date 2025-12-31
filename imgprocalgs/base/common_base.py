from abc import ABC, abstractmethod
import numpy as np

class ImageAlgorithmBase(ABC):
    """
    Base class for all image processing algorithms
    """

    def __init__(self, image: np.ndarray):
        self.image = image

    def validate_image(self):
        if self.image is None:
            raise ValueError("Input image cannot be None")

    @abstractmethod
    def process(self):
        """
        Each algorithm must implement this
        """
        pass
