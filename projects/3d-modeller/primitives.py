import numpy as np
from OpenGL.GL import *


def scaling(scale):
    s = np.identity(4)
    s[0, 0] = scale[0]
    s[1, 1] = scale[1]
    s[2, 2] = scale[2]
    s[3, 3] = 1
    return s


def translation(displacement):
    t = np.identity(4)
    t[0, 3] = displacement[0]
    t[1, 3] = displacement[1]
    t[2, 3] = displacement[2]
    return t


class Node(object):
    def __init__(self):
        # self.color_index = random.randint(color.MIN_COLOR, color.MAX_COLOR)
        # self.aabb = AABB([.0, .0, .0], [.5, .5, .5])
        self.translation_matrix = np.identity(4)
        self.scaling_matrix = np.identity(4)
        self.selected = False

    def render(self):
        glPushMatrix()
        glMultMatrixf(np.transpose(self.translation_matrix))
        glMultMatrixf(self.scaling_matrix)
        # curr_color = color.COLORS[self.color_index]
        # glColor3f(curr_color[0], curr_color[1], curr_color[2])
        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [.3, .3, .3])
        self.render_self()
        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [.0, .0, .0])
        glPopMatrix()

    def render_self(self):
        raise NotImplementedError()

    def pick(self, start, direction, mat):
        newmat = np.dot(np.dot(mat, self.translation_matrix), np.linalg.inv(self.scaling_matrix))
        results = self.aabb.ray_hit(start, direction, newmat)
        return results

    def select(self, select=None):
        if select is not None:
            self.selected = select
        else:
            self.selected = not self.selected

    def rotate_color(self, forwards):
        self.color_index += 1 if forwards else -1
        # if self.color_index > color.MAX_COLOR:
        #     self.color_index = color.MIN_COLOR
        # if self.color_index < color.MIN_COLOR:
        #     self.color_index = color.MAX_COLOR

    def scale(self, up):
        s = 1.1 if up else 0.9
        self.scaling_matrix = np.dot(self.scaling_matrix, scaling([s, s, s]))

    def translate(self, x, y, z):
        self.translation_matrix = np.dot(self.translation_matrix, translation([x, y, z]))


class Primitive(Node):
    def __init__(self):
        super(Primitive, self).__init__()
        self.call_list = None

    def render_self(self):
        glCallList(self.call_list)


class Sphere(Primitive):
    def __init__(self):
        super(Sphere, self).__init__()
        # self.call_list =


class Cube(Primitive):
    def __init__(self):
        super(Cube, self).__init__()
        # self.call_list =


class HierarchicalNode(Node):
    def __init__(self):
        super(HierarchicalNode, self).__init__()
        self.child_nodes = []

    def render_self(self):
        for child in self.child_nodes:
            child.render()


class SnowFigure(HierarchicalNode):
    def __init__(self):
        super(SnowFigure, self).__init__()
        self.child_nodes = [Sphere(), Sphere(), Sphere()]
        self.child_nodes[0].translate(0, -.6, 0)
        self.child_nodes[1].translate(0, .1, 0)
        self.child_nodes[1].scaling_matrix = np.dot(self.scaling_matrix, scaling([.7, .7, .7]))
        # for child in self.child_nodes:
        # child.color_index = color.MIN_COLOR
        # self.aabb = AABB([.0, .0, .0], [.5, 1.1, .5])
