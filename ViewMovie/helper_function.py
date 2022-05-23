from datetime import datetime


def get_event_date(date):
    today = datetime.now()
    if today.year - date.year <= 0:
        if today.month - date.month <= 0:
            if today.day - date.day <= 0:
                if today.hour - date.hour <= 0:
                    if today.minute - date.minute <= 0:
                        if today.second - date.second <= 0:
                            return "Just Now"
                        else:
                            if today.second - date.second == 1:
                                return "{} second ago".format(today.second - date.second)
                            else:
                                return "{} seconds ago".format(today.second - date.second)
                    else:
                        if today.minute - date.minute == 1:
                            return "{} minute ago".format(today.minute - date.minute)
                        else:
                            return "{} minutes ago".format(today.minute - date.minute)
                else:
                    if today.hour - date.hour == 1:
                        return "{} hour ago".format(today.hour - date.hour)
                    else:
                        return "{} hours ago".format(today.hour - date.hour)
            else:
                if today.day - date.day == 1:
                    return "{} day ago".format(today.day - date.day)
                else:
                    return "{} days ago".format(today.day - date.day)
        else:
            if today.month - date.month == 1:
                return "{} month ago".format(today.month - date.month)
            else:
                return "{} months ago".format(today.month - date.month)
    else:
        if today.year - date.year == 1:
            return "{} year ago".format(today.year - date.year)
        else:
            return "{} years ago".format(today.year - date.year)
