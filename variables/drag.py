class Drag:
    def __init__(self, drag_coefficient, drag_area, dynamic_pressure) -> None:
        self._drag_coefficient = drag_coefficient
        self._drag_area = drag_area
        self._dynamic_pressure = dynamic_pressure

    @property
    def value(self):
        return self._value
    @property.setter
    def value(self):
        self._value = self._drag_area*self._drag_coefficient*self._dynamic_pressure

    def update_value(self, drag_coefficient, drag_area, dynamic_pressure):
        self