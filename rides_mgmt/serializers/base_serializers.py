import json


class PointSerializer:
    def __init__(self, point):
        self.point = json.loads(point)

    def as_tuple(self):
        return self.point.get('lat'), self.point.get('lon')
