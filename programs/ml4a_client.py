import random
import numpy as np
from ml4a import image
from ml4a.models import neural_style


neural_style.params.gpu = '0'
neural_style.params.backend = 'cudnn'


def run(settings):

    content_images = [
        image.monalisa(),
        image.tubingen(),
        image.escher(),
        image.fridakahlo(),
        image.hokusai(),
        image.monalisa(),
        image.starrynight(),
        image.scream(),
        image.tubingen(),    
        "flowers.jpg",
        "fire.jpg",
        "lightning.jpg",
        "nebula.jpg"]
    
    style_images = [
        image.escher(),
        image.hokusai(),
        image.starrynight(),
        "flowers.jpg",
        "fire.jpg",
        "lightning.jpg",
        "nebula.jpg",
        "https://www.ignant.com/wp-content/uploads/2014/03/2High_Voltage_Image_MakingPhillip-Stearns01-360x272.jpg",
        "https://scene360.com/wp-content/uploads/2014/12/phillip-stearns-09.jpg",
        "https://morrismuseum.org/wp-content/uploads/2019/09/Elan.-Out-of-Place-2019.-Photo-by-Cameran-Ko.-Smaller-1.jpg",
        "https://i.ytimg.com/vi/IZCZV5-v3S4/maxresdefault.jpg",
        
    ]    
    
    octave_ratio = np.random.normal(1.6, 0.5)
    style_scale = np.random.normal(1, 0.2)
    normalize_gradients = random.choice([True, False])
    original_colors = random.choice([False]*5+[True])
    content_weight = random.choice([0, 0, 2.5, 4, 5])

    content = random.choice(content_images)
    style = content
    while style == content:
        style = random.choice(style_images)

    config = {
        'content_image': content,
        'style_image': style,
        'size': 576,
        'num_iterations': [800, 400, 200],
        'style_scale': style_scale,
        'octave_ratio': octave_ratio,
        'normalize_gradients': normalize_gradients,
        'original_colors': original_colors
    }
    
    print(config)
    
    img = neural_style.run(config)
    image.save(img, 'ml4aimage.png')
    return 'ml4aimage.png'
