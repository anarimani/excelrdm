import jdatetime
from django.http import JsonResponse

def convert_jalali_to_gregorian(request, jalali_date):
    """تبدیل تاریخ جلالی به میلادی"""
    try:
        year, month, day = map(int, jalali_date.split("-"))
        jalali_date = jdatetime.datetime(year, month, day)
        gregorian_date = jalali_date.togregorian()
        return JsonResponse({"gregorian_date": gregorian_date.strftime("%Y-%m-%d")})
    except:
        return JsonResponse({"error": "فرمت تاریخ معتبر نیست"}, status=400)

def convert_gregorian_to_jalali(request, gregorian_date):
    """تبدیل تاریخ میلادی به جلالی"""
    try:
        year, month, day = map(int, gregorian_date.split("-"))
        gregorian_date = jdatetime.date.fromgregorian(year=year, month=month, day=day)
        return JsonResponse({"jalali_date": str(gregorian_date)})
    except:
        return JsonResponse({"error": "فرمت تاریخ معتبر نیست"}, status=400)
