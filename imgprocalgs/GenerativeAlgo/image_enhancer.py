import os
import requests
from imgprocalgs.base.common_base import ImageAlgorithmBase


class ImageEnhancer(ImageAlgorithmBase):
    
    def __init__(self, imageInput: str, outputImage: str, prompt: str = None):
        self.image_path = imageInput
        self.output_path = outputImage
        self.prompt = prompt or "Enhance the Quality of Image"

    def process(self):
        files = {
            "image": open(self.image_path, "rb")
        }

        data = {
            "prompt": self.prompt
        }

        response = requests.post(
            "https://api.image_enhancer.com/enhance",
            headers={
                "Authorization": f"Bearer {os.getenv('GENAI_API_KEY')}"
            },
            files=files,
            data=data
        )

        response.raise_for_status()

        with open(self.output_path, "wb") as imageEnhance:
            imageEnhance.write(response.content)
