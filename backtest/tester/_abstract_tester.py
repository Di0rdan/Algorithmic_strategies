from .. import make_timestamp


class AbstractTester:

    def _step(self, timestamp, *args, **kwargs):
        raise NotImplementedError

    def _run(self, start: int, finish: int, tick_size, *args, **kwargs):
        for timestamp in range(start, finish, tick_size):
            self._step(timestamp, *args, **kwargs)
