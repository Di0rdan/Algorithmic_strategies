from ._abstract_data_manager import AbstractDataManager


class DataLoader(AbstractDataManager):

    def __init__(self, stock_exchange, ticker, freq):
        super().__init__(stock_exchange, ticker, freq)
        print("init DataLoader not implemented")

    def get(self, timestamp):
        return 0
