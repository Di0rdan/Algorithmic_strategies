class AbstractModel:

    def update(self, timestamp, data):
        raise NotImplemented

    def predict(self, timestamp):
        raise NotImplemented
