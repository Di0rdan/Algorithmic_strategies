class AbstractTester:

    def __init__(self, model, stock_exchange, ticker, time_period, hist_period, freq, metric):
        pass

    def start(self):
        raise NotImplementedError

    def get_metric(self):
        raise NotImplementedError
