def add_time(t1, t2):
    from Time import Time
    from int_to_time import int_to_time
    from time_to_int import time_to_int
    from valid_time import valid_time

    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')

    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

    # OLD CODE:
    # from Time import Time

    # sum = Time()
    # sum.hour = t1.hour + t2.hour
    # sum.minute = t1.minute + t2.minute
    # sum.second = t1.second + t2.second

    # if sum.second >= 60:
    #     sum.second -= 60
    #     sum.minute += 1

    # if sum.minute >= 60:
    #     sum.minute -= 60
    #     sum.hour += 1

    # return sum