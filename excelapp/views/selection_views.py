from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

def get_available_products(request):
    """نمایش لیست کالاهای موجود در اکسل"""
    try:
        df = pd.read_excel("instance/mydata.xlsx", engine="openpyxl")
        products = df["نام کالا"].dropna().unique().tolist()
        return JsonResponse({"products": products})
    except:
        return JsonResponse({"error": "فایل اکسل پیدا نشد"}, status=500)

def get_available_customers(request):
    """نمایش لیست خریداران موجود در اکسل"""
    try:
        df = pd.read_excel("instance/mydata.xlsx", engine="openpyxl")
        customers = df["خریدار"].dropna().unique().tolist()
        return JsonResponse({"customers": customers})
    except:
        return JsonResponse({"error": "فایل اکسل پیدا نشد"}, status=500)
