"""Simple display filters. Raw data is always stored unfiltered."""


def remove_dc(samples, alpha=0.995):
    """Single-pole high-pass: y[n] = x[n] - x[n-1] + alpha*y[n-1]."""
    out, prev_x, prev_y = [], None, 0.0
    for x in samples:
        if prev_x is None:
            prev_x = x
        prev_y = x - prev_x + alpha * prev_y
        prev_x = x
        out.append(prev_y)
    return out
