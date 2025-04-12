def process_command(filtered_df, command, customer=None, product=None):
    """پردازش دستورات مختلف و محاسبه نتایج"""
    try:
        if command == "best_customer":
            return filtered_df["خریدار"].value_counts().idxmax()
        elif command == "customer_product":
            filtered_df = filtered_df[filtered_df["نام_کالا"] == product]
            return filtered_df["خریدار"].value_counts().idxmax()
        elif command == "most_sold":
            return filtered_df["نام_کالا"].value_counts().idxmax()
        elif command == "profit_gained":
            return filtered_df['profit'].sum()
        elif command == "customer_best_product":
            filtered_df = filtered_df[filtered_df["خریدار"] == customer]
            return filtered_df["نام_کالا"].value_counts().idxmax()
        else:
            return "فرمان نامعتبر است"
    except:
        return "داده‌ای موجود نیست"
