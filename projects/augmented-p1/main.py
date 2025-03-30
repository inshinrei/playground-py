import argparse


def main():
    pass


parser = argparse.ArgumentParser(description='app')
parser.add_argument('-r', '--rectangle', help='draw rectangle delimiting target surface', action='store_true')
parser.add_argument('-mk', '--model_keypoints', help='draw model keypoints', action='store_true')
parser.add_argument('-fk', '--frame_keypoints', help='draw frame keypoints', action='store_true')
parser.add_argument('-ma', '--matches', help='draw matches between keypoints', action='store_true')
args = parser.parse_args()
if __name__ == '__main__':
    main()
