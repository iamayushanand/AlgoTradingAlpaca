from dotenv import load_dotenv
import os
from alpaca_trade_api.rest import REST,TimeFrame
load_dotenv()
api = REST()

bars=api.get_bars("AAPL", TimeFrame.Hour, "2021-02-08", "2021-02-08", limit=10, adjustment='raw').df
print(bars)
