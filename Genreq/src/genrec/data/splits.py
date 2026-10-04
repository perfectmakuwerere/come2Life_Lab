"""Temporal splits.

TODO: leave-last-out per user (last -> test, second last -> val, rest -> train).
Make sure no future interaction appears in any history prompt (leakage control).
"""


def temporal_leave_last_out(ratings):
    raise NotImplementedError
