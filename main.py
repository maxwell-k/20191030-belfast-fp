DURATIONS = {"m": 60 * 1000, "h": 60 * 60 * 1000, "d": 24 * 60 * 60 * 1000}


def main(_input):
    """Return the number of milliseconds in string

    y year
    w week
    d day
    m minute

    In addition:

    h hour
    """
    return sum(
        sum(
            float(component.rstrip(code)) * duration
            for code, duration in DURATIONS.items()
            if component.endswith(code)
        )
        for component in _input.split(" ")
    )


def test_main():
    assert main("") == 0
    assert main("1m") == 60 * 1000
    assert main("1.5m") == 90 * 1000
    assert main("1h") == 60 * 60 * 1000
    assert main("1h 1m") == 61 * 60 * 1000
    assert main("1d") == 24 * 60 * 60 * 1000
