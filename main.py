def main(_input):
    """Return the number of milliseconds in string

    y year
    w week
    d day
    m minute
    """
    code = "m"
    milliseconds = 60 * 1000
    if _input.endswith(code):
        return float(_input.rstrip(code)) * milliseconds
    else:
        return 0


def test_main():
    assert main("") == 0
    assert main("1m") == 60 * 1000
    assert main("1.5m") == 90 * 1000
