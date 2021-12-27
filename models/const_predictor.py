from ._abstract_model import AbstractModel


class ConstPredictor(AbstractModel):

    def __init__(self, prediction=0):
        self.prediction = prediction

    def update(self, timestamp, data):
        pass

    def predict(self, timestamp):
        return self.prediction
