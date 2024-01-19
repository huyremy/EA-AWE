import json
import time
from datetime import datetime
import MetaTrader5 as mt5
# Huyremy bypass login get root price
# Kết nối tới MetaTrader 5
if not mt5.initialize():
    print("Không thể kết nối tới MetaTrader 5")
    exit(1)

# Chọn ký hiệu (symbol) của XAUUSD và khung biểu đồ ví dụ H1 (1 giờ)
symbol = "XAUUSD"
timeframe = mt5.TIMEFRAME_M1

while True:
    # Lấy thông tin biểu đồ (chart) của XAUUSD
    chart_info = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1)
    if chart_info is None or len(chart_info) == 0:
        print("Không thể lấy thông tin biểu đồ")
        mt5.shutdown()
        exit(1)

    # Lấy giá bid và ask từ thông tin biểu đồ
    bid = str(chart_info[0][4])  # Chuyển đổi giá bid thành chuỗi
    ask = str(chart_info[0][5])  # Chuyển đổi giá ask thành chuỗi
    time2 = datetime.utcfromtimestamp(chart_info[0][0]).strftime('%Y-%m-%d %H:%M:%S')
    print("XAUUSD:", bid, " ", time2, "\n")
    # Tạo đối tượng dữ liệu JSON
    data = {
        'time': time2,
        'bid': bid,
        'ask': ask
    }

    # Ghi dữ liệu vào tệp JSON
    filename = 'xauusd.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
        time.sleep(1)
    # Tạm dừng chương trình trong 1 giây. 


# Đóng kết nối với MetaTrader 5
mt5.shutdown()
