import os
from pathlib import Path
from forward import *
from mask2polygon import mask_to_polygon
from save import save_geojson
from utils import load_img, draw_polylines
from parse_args import parse_args
import sys


def run(image_path: str, config: dict, save_path: Path, device: str = "cpu") -> None:
    image = load_img(config["path_to_data"] + image_path)
    seg_mask = get_mask(image, config["model"], config["data_params"], device)
    polygons = mask_to_polygon(seg_mask)
    save_geojson(polygons,  (save_path / image_path).with_suffix(".geojson"))
    draw_polylines(image, polygons, str(save_path / image_path))


def main(args = None) -> None:
    if args is None:
        args = sys.argv[1:]
    config = parse_args(args)
    save_path = Path(config["save_path"])
    save_path.mkdir(parents=True, exist_ok = True)
    if torch.cuda.is_available() and config["device"] == "cuda":
        device = "cuda"
    else:
        device = "cpu"
    for title in os.listdir(config["path_to_data"]):
        if any((title.endswith(".jpeg"), title.endswith(".jpg"), title.endswith(".png"))):
            run(title, config, save_path, device)


if __name__ == "__main__":
    main()
