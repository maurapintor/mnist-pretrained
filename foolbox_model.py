import foolbox as fb
import torch

from model import MNISTModel
from model_madry import Model


def create():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    weights_path = fb.zoo.fetch_weights(
        'https://github.com/maurapintor/mnist-pretrained/releases/download/v1.2/mnist_cnn.pt',
        unzip=False
    )
    model = MNISTModel()
    state_dict = torch.load(weights_path, map_location=device)
    model.load_state_dict(state_dict)
    model.eval()

    preprocessing = {'mean': 0.5,
                     'std': 0.5}

    fmodel = fb.models.PyTorchModel(model, bounds=(0, 1),
                                    preprocessing=preprocessing,
                                    device=device)

    return fmodel
