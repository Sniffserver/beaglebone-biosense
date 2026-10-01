from biosense.filters import remove_dc


def test_dc_removed():
    out = remove_dc([100.0] * 2000)
    assert abs(out[-1]) < 1e-6
