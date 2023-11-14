from building_footprint_segmentation.seg.binary.models import DLinkNet34, ReFineNet
from torch.utils import model_zoo
from building_footprint_segmentation.utils.py_network import adjust_model


def load_model(backbone: str, weights_url: str, device: str = "cpu"):
    if backbone == "DLinkNet34":
        model = DLinkNet34()
    elif backbone == "ReFineNet":
        model = ReFineNet()
    else:
        raise ValueError(f"Invalid backbone {backbone}")
    state_dict = model_zoo.load_url(
        weights_url,
        progress = True,
        map_location = device)
    if "model" in state_dict:
        state_dict = state_dict["model"]
    state_dict = adjust_model(state_dict)
    model.load_state_dict(state_dict)
    model.to(device)
    return model
