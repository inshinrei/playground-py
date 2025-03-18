from collections import defaultdict

from OpenGL.GLUT import glutMotionFunc, glutMouseFunc, glutKeyboardFunc, glutSpecialFunc
from OpenGL.raw.GLUT import glutGet, GLUT_WINDOW_WIDTH, GLUT_WINDOW_HEIGHT, GLUT_DOWN, GLUT_RIGHT_BUTTON, \
    GLUT_LEFT_BUTTON, glutPostRedisplay, GLUT_MIDDLE_BUTTON, GLUT_KEY_UP, GLUT_KEY_DOWN, GLUT_KEY_LEFT, GLUT_KEY_RIGHT


class Interaction(object):
    def __init__(self):
        self.pressed = None
        self.translation = [0, 0, 0, 0]
        # self.trackball = trackball.Trackball(theta=-25, distance=15)
        self.mouse_loc = None
        self.callbacks = defaultdict(list)
        self.register()

    def register(self):
        glutMouseFunc(self.handle_mouse_button)
        glutMotionFunc(self.handle_mouse_move)
        glutKeyboardFunc(self.handle_keystroke)
        glutSpecialFunc(self.handle_keystroke)

    def translate(self, x, y, z):
        self.translation[0] = x
        self.translation[1] = y
        self.translation[2] = z

    def handle_mouse_button(self, button, mode, x, y):
        x_size, y_size = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = y_size - y  # invert, opengl coordinate system
        self.mouse_loc = (x, y)
        if mode == GLUT_DOWN:
            self.pressed = button
            if button == GLUT_RIGHT_BUTTON:
                pass
            elif button == GLUT_LEFT_BUTTON:
                self.trigger('pick', x, y)
            elif button == 3:
                self.translate(0, 0, 1.0)
            elif button == 4:
                self.translate(0, 0, -1.0)
        else:
            self.pressed = None
        glutPostRedisplay()

    def handle_mouse_move(self, x, screen_y):
        x_size, y_size = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = y_size - screen_y
        if self.pressed is not None:
            dx = x - self.mouse_loc[0]
            dy = y - self.mouse_loc[1]
            if self.pressed == GLUT_RIGHT_BUTTON and self.trackball is not None:
                self.trackball.drug_to(self.mouse_loc[0], self.mouse_loc[1], dx, dy)
            elif self.pressed == GLUT_LEFT_BUTTON:
                self.trigger('move', x, y)
            elif self.pressed == GLUT_MIDDLE_BUTTON:
                self.translate(dx / 60.0, dy / 60.0, 0)
            else:
                pass
            glutPostRedisplay()
        self.mouse_loc = (x, y)

    def handle_keystroke(self, key, x, screen_y):
        x_size, y_size = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = y_size - screen_y
        if key == 's':
            self.trigger('place', 'sphere', x, y)
        elif key == 'c':
            self.trigger('place', 'cube', x, y)
        elif key == GLUT_KEY_UP:
            self.trigger('scale', up=True)
        elif key == GLUT_KEY_DOWN:
            self.trigger('scale', up=False)
        elif key == GLUT_KEY_LEFT:
            self.trigger('rotate_color', forward=True)
        elif key == GLUT_KEY_RIGHT:
            self.trigger('rotate_color', forward=False)
        glutPostRedisplay()

    def register_callback(self, name, f):
        self.callbacks[name].append(f)

    def trigger(self, name, *args, **kwargs):
        for callback in self.callbacks[name]:
            callback(*args, **kwargs)
