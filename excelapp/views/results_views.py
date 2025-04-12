from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .data_processing import load_and_filter_excel
from .statistics import process_command

@login_required
def results_view(request, start_date, end_date, command, customer=None, product=None):
    """نمایش نتایج پردازش شده از داده‌های اکسل"""
    filtered_df, error = load_and_filter_excel(start_date, end_date)
    if error:
        result = f"خطا در پردازش: {error}"
    else:
        result = process_command(filtered_df, command, customer, product)

    return render(request, "results.html", {
        "result": result,
        "start_date": start_date,
        "end_date": end_date,
        "command": command,
        "customer": customer,
        "product": product,
    })
