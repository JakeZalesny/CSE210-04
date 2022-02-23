class Actor:
    def __init__(self):
        self._text = ""
        self._font_size = 15
        self._color = (255, 255, 255,)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        
