import pandas as pd
import jdatetime

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_excel(self.file_path, engine="openpyxl")
        self.df.columns = self.df.columns.str.strip().str.lower().str.replace(" ", "_")
        self.df["Gregorian_Date"] = self.df["تاریخ"].apply(self.convert_jalali_to_datetime)

    def convert_jalali_to_datetime(self, jalali_date_str):
        year, month, day = map(int, jalali_date_str.split("-"))
        jalali_date = jdatetime.datetime(year, month, day)
        return jalali_date.togregorian()

    def filter_data(self, start_date, end_date):
        return self.df[
            (self.df["Gregorian_Date"] >= pd.to_datetime(start_date)) &
            (self.df["Gregorian_Date"] <= pd.to_datetime(end_date))
        ]