def increment(time, seconds):
    """
    Este es un modifier.
    >> print_time(start)
    (09:45:00)
    >> increment(start,10)
    >> print_time(start)
    (09:45:10)

    Osea que sin un return, modifico el valor de start
    Un modifier modifica el objeto, no crea otro nuevo
    """
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1