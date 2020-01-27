from datetime import datetime

def format_calculation_result(result):
    """To avoid too long integer output, we should format
    calculation results.

    :param result: int
    :return: format number output
    """
    if not result:
        return
    MAX = 100000000
    if int(result) > MAX:
        return format(result, 'e')
    return result


def get_time_consumed(start_time):
    """Calculate time difference from start_time to now

    :param start_time: datetime
    :return: time_consumed
    """
    return datetime.now() - start_time
