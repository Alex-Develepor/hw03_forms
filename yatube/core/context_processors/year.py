import datetime as dt


def year(request):
    now = dt.datetime.now()
    now = now.year
    return {
        'year': int(now)
    }