from easyquant.quotation import use_quotation
from RSI import RSIStrategy

print("backtest 回测 测试 ")

quotation = use_quotation("jqdata")


trade_days = quotation.get_all_trade_days()

end_date = "2021-12-24"

stock_code = "002230"
size = 500

bars = quotation.get_bars(stock_code, size, end_dt=end_date)

# strategy = CCIStrategy(stock_code, bars, days=size)
# strategy = BOLLStrategy(stock_code, bars, days=size)

# strategy = MACDStrategy(stock_code, bars, days=size)

strategy = RSIStrategy(stock_code, bars, days=size)
strategy.process()
strategy.show_plt()
