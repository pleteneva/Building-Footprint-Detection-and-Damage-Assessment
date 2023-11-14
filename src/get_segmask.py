import cv2
import torch
import numpy as np
from building_footprint_segmentation.helpers.normalizer import min_max_image_net
from building_footprint_segmentation.utils.py_network import to_input_image_tensor
from model import load_model
from image_fragment.fragment import ImageFragment


CROP_TO_DIM = (384, 384, 3)


def get_mask(image: np.array,
             model_config: dict,
             data_params: dict,
             device: str = "cpu",
             ) -> np.array:
    model = load_model(model_config["backbone"], model_config["weights"], device)
    h, w = data_params["resize"]
    if image.shape[0] > h or image.shape[1] > w:
        input_image = cv2.resize(image, (w, h))
    else:
        input_image = image.copy()
    mask = np.zeros(input_image.shape, dtype=np.float32)
    image_fragment = ImageFragment.image_fragment_3d(
        fragment_size = (384, 384, 3), org_size = input_image.shape)
    for fragment in image_fragment:
        fragmented_image = fragment.get_fragment_data(input_image)
        img = min_max_image_net(img = fragmented_image)
        tensor_image = to_input_image_tensor(img).unsqueeze(0)
        with torch.no_grad():
            prediction = model(tensor_image)
            prediction = prediction.sigmoid()[0, 0, :, :].detach().cpu().numpy()
        mask = fragment.transfer_fragment(transfer_from = cv2.cvtColor(prediction, cv2.COLOR_GRAY2RGB),
                                        transfer_to = mask)
    if input_image.shape[:2] != image.shape[:2]:
        mask = cv2.resize(mask, image.shape[:2][::-1])
    return mask[:,:,0]
