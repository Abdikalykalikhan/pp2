import datetime
x = datetime.datetime.now()
x_seconds = x.timestamp()

any_data = datetime.datetime(2024,2,16,10,12,10)
any_data_seconds = any_data.timestamp()

print(abs(x_seconds - any_data_seconds))