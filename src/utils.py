import numpy as np
import cv2
import argparse
import yaml
from typing import Optional


def load_img(image_path: str) -> np.array:
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def draw_polylines(image: np.array, polygons, save_path: str) -> None:
    for poly in polygons:
        x, y = poly.exterior.xy
        pts = list(map(lambda i: [int(x[i]), int(y[i])], range(len(x))))
        pts = np.array(pts, np.int32)
        cv2.polylines(image, [pts], isClosed = True, color = (0, 255, 0), thickness = 3)
    print(f"Saving image to {save_path}")
    cv2.imwrite(save_path, image[:,:, ::-1])
    return None


def parse_args(args):
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('--config', help='path to config', default="config.yml")
    config = yaml_parser(parser.parse_args(args).config)
    return config


def yaml_parser(
    path: Optional[str] = None,
    data: Optional[str] = None,
    loader: yaml.SafeLoader = yaml.SafeLoader
) -> dict:
    if path:
        with open(r"{}".format(path)) as file:
            return yaml.load(file, Loader=loader)
    elif data:
        return yaml.load(data, Loader=loader)

    raise ValueError('Either a path or data should be defined as input')
