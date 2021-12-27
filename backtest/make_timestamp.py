from numpy import datetime64 as numpy_datetime


def make_timestamp(timestamp):
    if timestamp is int:
        return timestamp
    try:
        return int(timestamp)
    except:
        pass
    try:
        return numpy_datetime(timestamp).tolist().timestamp()
    except:
        pass
    if timestamp is str:
        if timestamp in ['millisecond', 'ms']:
            return 1
        elif timestamp in ['second', 'sec', 's']:
            return 1000
        elif timestamp in ['minute', 'min', 'm']:
            return 1000 * 60
        elif timestamp in ['hour', 'h']:
            return 1000 * 60 * 60
        else:
            raise ValueError(f"unexpectd value for tick_size: {timestamp}")
    else:
        raise ValueError(f"unexpected type for tick_size: {type(timestamp)}")
