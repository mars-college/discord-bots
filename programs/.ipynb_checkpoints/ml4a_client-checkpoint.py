from ml4a import image
from ml4a.models import neural_style


def run(settings):
    neural_style.params.gpu = '0'
    neural_style.params.backend = 'cudnn'

    config = {
        'content_image': image.tubingen(),
        'style_image': image.starrynight(),
        'size': 720,
        'num_iterations': 500
    }

    img = neural_style.run(config)
    image.save(img, 'myimage.png')
    return 'myimage.png'
