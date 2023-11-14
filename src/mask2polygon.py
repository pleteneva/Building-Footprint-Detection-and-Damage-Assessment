import numpy as np
from skimage import measure
from shapely.geometry import Polygon


def mask_to_polygon(mask: np.array, min_area: int = 2000):
    threshold = (np.min(mask) + np.max(mask)) / 2
    contours = measure.find_contours(mask, threshold, positive_orientation='low', fully_connected='high')
    polygons = []
    for contour in contours:
        for i in range(len(contour)):
            row, col = contour[i]
            contour[i] = (col - 1, row - 1)

        poly = Polygon(contour)
        poly = poly.simplify(1.0, preserve_topology=False)
        if poly.area < min_area:
            continue
        polygons.append(poly)
    return polygons
