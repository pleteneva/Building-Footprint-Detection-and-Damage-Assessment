from shapely import geometry
from pathlib import Path
import json


# Save the polygons as a GeoJSON file
def save_geojson(polygons, save_path: Path) -> None:
    geo_dict = {"type": "FeatureCollection",
                "features": [{"type": "Feature", "geometry": a} for a in [geometry.mapping(b) for b in polygons]]}
    json.dumps(geo_dict, indent=4)
    with save_path.open("w") as f:
        json.dump(geo_dict, f)
    return
