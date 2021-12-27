from ._abstract_tester import AbstractTester
from ..data_manager import DataLoader
from ..metric import AbstractMetric
from .. import make_timestamp


class Tester(AbstractTester):

    def __init__(self, model, stock_exchange, ticker, freq, metric):
        self.model = model
        self.data_manager = DataLoader(stock_exchange, ticker, freq)
        self.metric = AbstractMetric()
        print(
            '''
            Tester.__init__ not implemented yet
            TODO:
                * add metric chooser
                * remove "from ..metric import AbstractMetric" from header
            '''
        )

    def _step(self, timestamp, **kwargs):
        data = self.data_manager.get(timestamp)
        self.model.update(timestamp, data)
        predict = self.model.predict(timestamp)
        if kwargs.get('metric_mode', '') != 'off':
            self.metric.update(timestamp, data, predict)

    def test(self, start, finish, historical_period=0, frequency='minute'):
        start = make_timestamp(start)
        finish = make_timestamp(finish)
        historical_period = make_timestamp(historical_period)
        frequency = make_timestamp(frequency)

        if start > finish:
            raise ValueError(f"start > finish: {start} > {finish}")
        if finish - start < historical_period:
            raise ValueError(f"historical period too large")

        self._run(start, start + historical_period, frequency, metrick_mode='off')
        self._run(start + historical_period, finish, frequency)

    def get_metric(self):
        return self.metric.get()
