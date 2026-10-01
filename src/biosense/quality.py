"""Per-sample quality flags."""

CLIP_MARGIN = 64  # counts from full scale


def is_clipped(raw):
    return raw >= 32767 - CLIP_MARGIN or raw <= -32768 + CLIP_MARGIN


def interval_jitter_ms(t_ns, expected_ms):
    """Return list of |interval - expected| in ms for consecutive timestamps."""
    return [abs((b - a) / 1e6 - expected_ms) for a, b in zip(t_ns, t_ns[1:])]


def flags(raw, jitter_ms, max_jitter_ms):
    out = []
    if is_clipped(raw):
        out.append("clip")
    if jitter_ms is not None and jitter_ms > max_jitter_ms:
        out.append("jitter")
    return out
