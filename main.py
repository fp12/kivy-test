import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line
from math import sqrt, sin, cos, pi
from kivy.graphics import Mesh
from kivy.properties import NumericProperty

def draw_hexagon(radius, x, y):
    r = radius
    a = 2 * pi / 6
    vertices=[]
    for i in range(6):
        vertices += [ 
            x + cos(i * a) * r,
            y + sin(i * a) * r,
            cos(i * a),
            sin(i * a),
        ]
    Mesh(vertices=vertices, indices=range(6), mode='triangle_fan')

def hex_to_pixel(q, r, size):
    x = size * 3/2 * q
    y = size * sqrt(3) * (r + q/2)
    return (x, y)

class Hexagon(Widget):
    radius = NumericProperty(20)
    front_radius = NumericProperty(5)
    q = NumericProperty(0)
    r = NumericProperty(0)

    def __init__(self, q, r, **kwargs):
        self.q = q
        self.r = r
        super(Hexagon, self).__init__(pos=hex_to_pixel(q, r, 21, **kwargs))


class HexMap(RelativeLayout):
    def __init__(self, **kwargs):
        super(HexMap, self).__init__(**kwargs)

        map_radius = 6
        for q in range(-map_radius, map_radius+1):
            r1 = max(-map_radius, -q - map_radius)
            r2 = min(map_radius, -q + map_radius)
            for r in range(r1, r2+1):
                hexagon = Hexagon(q, r, )
                hexagon.width=50*sqrt(3)
                self.add_widget(hexagon)


class MyApp(App):
    def build(self):
        return HexMap()

if __name__ == '__main__':
    MyApp().run()
