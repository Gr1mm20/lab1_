from datetime import datetime, timedelta

def get_time_gmt(gmt):
    try:
        delta = timedelta(hours=int(gmt))
        current_time = datetime.utcnow()
        result_time = current_time + delta
        return result_time
    except ValueError:
        return None


gmt_ = input("Введите смещение по GMT:\t")
result = get_time_gmt(gmt_)
if result:
    print("Смешанное значение даты и времени:", result)
else:
    print("Неверный формат GMT строки.")
  
