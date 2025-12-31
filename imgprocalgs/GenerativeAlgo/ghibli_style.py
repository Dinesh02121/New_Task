import os
import requests
from imgprocalgs.base.common_base import ImageAlgorithmBase


class GhibliStyleImage(ImageAlgorithmBase):
   

    def __init__(self, imageInput: str, imageOutput: str, prompt: str = None):
        self.image_path = imageInput
        self.output_path = imageOutput
        self.prompt = prompt or (
            "Generate Studio Ghibli Style Image "
        )

    def process(self):
        files = {
            "image": open(self.image_path, "rb")
        }

        data = {
            "prompt": self.prompt,
            "style": "ghibli"
        }

        response = requests.post(
            "https://api.ghibli_style/style-transfer",
            headers={
                "Authorization": f"Bearer {os.getenv('GENAI_API_KEY')}"
            },
            files=files,
            data=data
        )

        response.raise_for_status()

        with open(self.output_path, "wb") as ghibliFile:
            ghibliFile.write(response.content)
