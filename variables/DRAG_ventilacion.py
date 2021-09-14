class drag_ventilacion:
    def __init__(self, dinamic_pressure, drag_area, drag):
        self.dinamic_pressure = dinamic_pressure
        self.drag_area = drag_area
        self.drag = drag

    def drag_coefficient(self):
        self.drag/(self.dinamic_pressure * self.drag_area)

