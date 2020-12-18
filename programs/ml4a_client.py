from ml4a import image
from ml4a.models import neural_style


def run(settings):
    neural_style.params.gpu = '0'
    neural_style.params.backend = 'cudnn'

    config = {
        'content_image': image.tubingen(),
        'style_image': image.starrynight(),
        'size': 640,
        'num_iterations': 100
    }

    img = neural_style.run(config)
    image.save(img, 'ml4aimage.png')
    return 'ml4aimage.png'
