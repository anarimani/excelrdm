from django.urls import path, re_path
from excelapp.views import (
    auth_views,
    date_views,
    selection_views,
    results_views,
    data_processing,
    statistics,
    utils
)


app_name = "excelapp"

urlpatterns = [
    # احراز هویت
    path("", auth_views.login, name="login"),
    
    # انتخاب تاریخ
    path("select_date/", date_views.select_date, name="select_date"),
    
    # انتخاب فرمان و مشتری و محصول
    path(
        "command_selector/<str:start_date>/<str:end_date>/",
        selection_views.command_selector,
        name="command_selector",
    ),
    path(
        "select_customer/<str:start_date>/<str:end_date>/<str:command>/",
        selection_views.select_customer,
        name="select_customer",
    ),
    path(
        "select_product/<str:start_date>/<str:end_date>/<str:command>/<str:customer>/",
        selection_views.select_product,
        name="select_product",
    ),
    
    # نمایش نتایج
    re_path(
        r"^results/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})/(?P<command>[^/]+)(?:/(?P<customer>[^/]+))?(?:/(?P<product>[^/]+))?/$",
        results_views.results,
        name="results",
    ),
]
