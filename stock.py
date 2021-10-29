import akshare as ak
import numpy as np
import datetime as dt

end = dt.datetime.now()
ed = end.strftime('%Y%m%d')
start = end + dt.timedelta(days=-9)
sd = start.strftime('%Y%m%d')

cl = ()
spot = ak.stock_zh_a_spot_em()
st = np.array(spot[['代码']])
for s in st:
	code = str(s)[2:8]
	ak.stock_zh_a_hist(
		symbol=code,
		period = 'daily',
		start_date=sd,
		end_date=ed,
		adjust='qfq'
	)


#stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sh600582", adjust="hfq")
#print(stock_zh_a_daily_hfq_df) 