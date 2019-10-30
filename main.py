def main(_input):
    """Return the number of milliseconds in string

    y year
    w week
    d day
    m minute
    """
    if _input.endswith("m"):
        minutes = float(_input.rstrip("m"))
        return minutes * 60 * 1000
    else:
        return 0


def test_main():
    assert main("") == 0
    assert main("1m") == 60 * 1000
    assert main("1.5m") == 90 * 1000
