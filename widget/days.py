from datetime import datetime
from dateutil.relativedelta import relativedelta

# 輸入起始與結束日期
start_str = input("請輸入開始日期 (格式 YYYY/MM/DD): ")
end_str = input("請輸入結束日期 (格式 YYYY/MM/DD): ")

# 轉為 datetime 格式
start_date = datetime.strptime(start_str, "%Y/%m/%d")
end_date = datetime.strptime(end_str, "%Y/%m/%d")

# 計算總天數
total_days = (end_date - start_date).days

# 使用 relativedelta 計算年月日差
delta = relativedelta(end_date, start_date)

# 顯示結果
print(f"總共相隔：{delta.years} 年 {delta.months} 月 {delta.days} 天")
print(f"總共相隔：{total_days} 天")
