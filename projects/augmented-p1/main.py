import argparse
import math
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
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == "vt":
                self.texcoords.append(map(float, values[1:3]))
            elif values[0] == "f":
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split("/")
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords))


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
    while True:
        ret, frame = cap.read()
        if not ret:
            print("unable to read frame")
            return
        kp_frame, des_frame = orb.detectAndCompute(frame, None)
        matches = bf.match(des_model, des_frame)
        matches = sorted(matches, key=lambda x: x.distance)
        if len(matches) < MIN_MATCHES:
            src_pts = np.float32([kp_model[m.queryIdx].pt for m in matches]).reshape(
                -1, 1, 2
            )
            dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in matches]).reshape(
                -1, 1, 2
            )
            homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if args.rectangle:
                h, w = model.shape
                pts = np.float32(
                    [[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]
                ).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, homography)
                frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
            if homography is not None:
                try:
                    projection = projection_matrix(camera_params, homography)
                    frame = render(frame, obj, projection, model, False)
                except:
                    pass
            if args.matches:
                frame = cv2.drawMatches(
                    model, kp_model, frame, kp_frame, matches[:10], 0, flags=2
                )
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            print("not enough matches %d/%d" % (len(matches), MIN_MATCHES))
    cap.release()
    cv2.destroyAllWindows()
    return 0


def render(img, obj, projection, model, color=False):
    vertices = obj.vertices
    scale_matrix = np.eye(3) * 3
    h, w = model.shape
    for face in obj.faces:
        face_vertices = face[0]
        points = np.array([vertices[vertex - 1] for vertex in face_vertices])
        points = np.dot(points, scale_matrix)
        points = np.array([[p[0] + w / 2, p[1] + h / 2, p[2]] for p in points])
        dst = cv2.perspectiveTransform(points.reshape(-1, 1, 3), projection)
        imgpts = np.int32(dst)
        if color is False:
            cv2.fillConvexPoly(img, imgpts, DEFAULT_COLOR)
        else:
            color = hex_to_rgb(face[-1])
            color = color[::-1]
            cv2.fillConvexPoly(img, imgpts, color)
    return img


def projection_matrix(camera_params, homography):
    homography *= -1
    rotate_and_translate = np.dot(np.linalg.inv(camera_params), homography)
    col_1 = rotate_and_translate[:, 0]
    col_2 = rotate_and_translate[:, 1]
    col_3 = rotate_and_translate[:, 2]
    l = math.sqrt(np.linalg.norm(col_1, 2) * np.linalg.norm(col_2, 2))
    rotate_1 = col_1 / l
    rotate_2 = col_2 / l
    translation = col_3 / l
    c = rotate_1 + rotate_2
    p = np.cross(rotate_1, rotate_2)
    d = np.cross(c, p)
    rotate_1 = np.dot(
        c / np.linalg.norm(c, 2) + d / np.linalg.norm(d, 2), 1 / math.sqrt(2)
    )
    rotate_2 = np.dot(
        c / np.linalg.norm(c, 2) - d / np.linalg.norm(d, 2), 1 / math.sqrt(2)
    )
    rotate_3 = np.cross(rotate_1, rotate_2)
    projection = np.stack((rotate_1, rotate_2, rotate_3, translation)).T
    return np.dot(camera_params, projection)


def hex_to_rgb(hex):
    hex_color = hex.lstrip("#")
    h_len = len(hex_color)
    return tuple(
        int(hex_color[i : i + h_len // 3], 16) for i in range(0, h_len, h_len // 3)
    )


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
