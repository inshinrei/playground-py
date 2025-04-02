import argparse
import os

import cv2
import numpy as np

MIN_MATCHES = 10
DEFAULT_COLOR = (0, 0, 0)


class ObjLoader:
    def __init__(self, filename, swapyz=False):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        material = None
        for line in open(filename, "r"):
            if line.startswith("#"):
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == "v":
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == "vn":
                pass


def main():
    homography = None
    camera_params = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]])
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    dir_name = os.getcwd()
    model = cv2.imread(os.path.join(dir_name, "ref/model.jpg"), 0)
    kp_model, des_model = orb.detectAndCompute(model, None)
    obj = ObjLoader(os.path.join(dir_name, "models/fox.obj"), swapyz=True)
    cap = cv2.VideoCapture(0)


parser = argparse.ArgumentParser(description="app")
parser.add_argument(
    "-r",
    "--rectangle",
    help="draw rectangle delimiting target surface",
    action="store_true",
)
parser.add_argument(
    "-mk", "--model_keypoints", help="draw model keypoints", action="store_true"
)
parser.add_argument(
    "-fk", "--frame_keypoints", help="draw frame keypoints", action="store_true"
)
parser.add_argument(
    "-ma", "--matches", help="draw matches between keypoints", action="store_true"
)
args = parser.parse_args()
if __name__ == "__main__":
    main()
