# referenced code here: https://machinelearningmastery.com/develop-arch-and-garch-models-for-time-series-forecasting-in-python/
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

aapl = pd.read_csv("Dataset\Equities\AAPL.csv")
meta = pd.read_csv("Dataset\Equities\META.csv")
orcl = pd.read_csv("Dataset\Equities\ORCL.csv")

df_aapl = pd.DataFrame(data=aapl)
df_meta = pd.DataFrame(data=meta)
df_orcl = pd.DataFrame(data=orcl)
df_aapl.rename(columns={"Close": "aapl_close"}, inplace=True)
df_meta.rename(columns={"Close": "meta_close"}, inplace=True)
df_orcl.rename(columns={"Close": "orcl_close"}, inplace=True)
# print(df_aapl)

aapl_close = df_aapl["aapl_close"]
meta_close = df_meta["meta_close"]
orcl_close = df_orcl["orcl_close"]


# print(aapl_close)
# print(meta_close)
# print(orcl_close)
assert aapl_close.shape == meta_close.shape == orcl_close.shape

date = pd.to_datetime(df_aapl["Date"])
portfolio = pd.DataFrame(date)
portfolio = portfolio.join(aapl_close)
portfolio = portfolio.join(meta_close)
portfolio = portfolio.join(orcl_close)
# print(portfolio)
# print(f"portfolio shape: {portfolio.shape}")

portfolio.set_index('Date', inplace=True)

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(portfolio["aapl_close"], label="appl_close")
ax.plot(portfolio["meta_close"], label="meta_close")
ax.plot(portfolio["orcl_close"], label="orcl_close")

ax.legend()

# Format x-ticks
ax.xaxis.set_major_locator(mdates.YearLocator())  # to display one tick per year
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # to format the date as 'YYYY-MM'

# Rotate date labels automatically
fig.autofmt_xdate()

ax.set_title('Stock Price Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Stock Price')
ax.grid(True)

plt.show()