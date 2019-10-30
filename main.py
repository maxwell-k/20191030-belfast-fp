DURATIONS = {"m": 60 * 1000, "h": 60 * 60 * 1000}


def main(_input):
    """Return the number of milliseconds in string

    y year
    w week
    d day
    m minute

    In addtion:

    h hour
    """
    result = 0

    for code in DURATIONS:
        if _input.endswith(code):
            result += float(_input.rstrip(code)) * DURATIONS[code]

    return result


def test_main():
    assert main("") == 0
    assert main("1m") == 60 * 1000
    assert main("1.5m") == 90 * 1000
    assert main("1h") == 60 * 60 * 1000
