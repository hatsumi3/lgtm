from io import BytesIO
from pathlib import Path
import requests

class LocalImage(object):
    def __init__(self, path) -> None:
        self._path = path
    
    def get_image(self):
        return open(self._path, 'rb')

class RemoteImage(object):
    def __init__(self, path) -> None:
        self._url = path
    
    def get_image(self):
        data = requests.get(self._url)
        return BytesIO(data.content)

class _LoremFlickr(RemoteImage):
    LOREM_FLICK_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword) -> None:
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICK_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')

def ImageSource(keyword):
    if keyword.startswith(('http://','https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)

def get_image(keyword):
    return ImageSource(keyword).get_image()

KeywordImage = _LoremFlickr
