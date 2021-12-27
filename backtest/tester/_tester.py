from ._abstract_tester import AbstractTester

class Tester(AbstractTester):

    def __init__(self, model, stock_exchange, ticker, time_period, hist_period, freq, metric):
        super().__init__(model, stock_exchange, ticker, time_period, hist_period, freq, metric)

    def start(self):
        pass

    def get_metric(self):
        pass
