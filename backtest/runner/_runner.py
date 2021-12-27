from ._abstract_runner import AbstractRunner

class Runner(AbstractRunner):

    def __init__(self, model, stock_exchange, ticker, time_period, hist_period, freq, metric):
        super().__init__(model, stock_exchange, ticker, time_period, hist_period, freq, metric)
        print("init Runner not implemented")
