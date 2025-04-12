import jdatetime

def convert_jalali_to_datetime(jalali_date_str):
    """تبدیل تاریخ جلالی به میلادی"""
    year, month, day = map(int, jalali_date_str.split("-"))
    jalali_date = jdatetime.datetime(year, month, day)
    return jalali_date.togregorian()
