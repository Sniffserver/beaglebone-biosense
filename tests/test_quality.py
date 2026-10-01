from biosense.quality import flags, interval_jitter_ms, is_clipped


def test_clipping():
    assert is_clipped(32767)
    assert is_clipped(-32768)
    assert not is_clipped(0)


def test_jitter():
    t = [0, 4_000_000, 8_500_000]
    j = interval_jitter_ms(t, 4.0)
    assert j[0] == 0.0
    assert abs(j[1] - 0.5) < 1e-9


def test_flags():
    assert flags(0, 1.0, 4.0) == []
    assert flags(32767, 10.0, 4.0) == ["clip", "jitter"]
