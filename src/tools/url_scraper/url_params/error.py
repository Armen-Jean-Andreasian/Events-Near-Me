class BaseClassError(ValueError):
    def __init__(self, class_name: str, property_name: str):
        self.class_name = class_name
        self.property_name = property_name

    def __str__(self):
        return f"Base class {self.class_name} does not support {self.property_name} property. Its child classes needed."
