from dotenv import load_dotenv
import os
import requests
import scipy
import numpy as np
from io import BytesIO
from PIL import Image

from instabot import Bot 
from instabot.api.api_photo import compatible_aspect_ratio, get_image_size

load_dotenv()


bot = None


def url_to_image(url):
    finished = False
    max_tries, n_tries = 5, 0
    img = None
    while not finished:
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            finished = True
        except:
            time.sleep(5)
            n_tries += 1
            finished = n_tries >= 10
    return img


# helper functions for optimizing for instagram from https://github.com/basnijholt/instacron
def strip_exif(img):
    """Strip EXIF data from the photo to avoid a 500 error."""
    data = list(img.getdata())
    image_without_exif = Image.new(img.mode, img.size)
    image_without_exif.putdata(data)
    return image_without_exif


def _entropy(data):
    """Calculate the entropy of an image"""
    hist = np.array(Image.fromarray(data).histogram())
    hist = hist / hist.sum()
    hist = hist[hist != 0]
    return -np.sum(hist * np.log2(hist))


def crop(x, y, data, w, h):
    """Crop an image"""
    x = int(x)
    y = int(y)
    return data[y : y + h, x : x + w]


def crop_maximize_entropy(img, min_ratio=4/5, max_ratio=90/47):
    """Crop image so as fit inside Instagram's aspect ratio constraints while maximizizing entropy"""
    from scipy.optimize import minimize_scalar

    w, h = img.size
    data = np.array(img)
    ratio = w / h
    if ratio > max_ratio:  # Too wide
        w_max = int(max_ratio * h)

        def _crop(x):
            return crop(x, y=0, data=data, w=w_max, h=h)

        xy_max = w - w_max
    else:  # Too narrow
        h_max = int(w / min_ratio)

        def _crop(y):
            return crop(x=0, y=y, data=data, w=w, h=h_max)

        xy_max = h - h_max

    to_minimize = lambda xy: -_entropy(_crop(xy))  # noqa: E731
    x = minimize_scalar(to_minimize, bounds=(0, xy_max), method="bounded").x
    return Image.fromarray(_crop(x))


def setup():
    global bot
    os.system('rm -rf config')
    bot = Bot()
    bot.login(username=os.getenv('INSTAGRAM_USERNAME'), 
              password=os.getenv('INSTAGRAM_PASSWORD'))
    

def run(message):
    if not message.attachments:
        return None

    if bot is None:
        setup()

    urls = [attachment.url for attachment in message.attachments
            if os.path.splitext(attachment.url)[1].lower() in ['.jpg', '.jpeg', '.png']]
    
    url = urls[0]
    img = url_to_image(url)
    img = strip_exif(img).convert('RGB')
    w, h = img.size
    
    # https://www.tailwindapp.com/blog/instagram-image-size-guide-2020
    if not compatible_aspect_ratio((w, h)):
        img = crop_maximize_entropy(img)

    img.save('mytestimage.jpg')
    result = bot.upload_photo("mytestimage.jpg", caption="quack quack")
    
    if isinstance(result, dict) and 'code' in result:
        return 'Success! https://www.instagram.com/p/{}'.format(result['code'])
    else:
        return 'Ooops, something went wrong in the upload :('
