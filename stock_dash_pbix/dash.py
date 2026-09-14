import pandas as pd
import yfinance as yf

# Jo stocks track karne hai unki list
TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL",
    "META",
    "TSLA",
    "BRK-B",
    "JPM",
    "WMT",
    "TSM",
    "0700.HK",
    "BABA",
    "005930.KS",
    "7203.T",
    "6758.T",
    "NVO",
    "ASML",
    "SAP",
    "SIE.DE",
    "RELIANCE.NS",
    "TCS.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "INFY.NS"
]
PERIOD = "6mo"
INTERVAL = "1d"
OUTPUT_FILE = "stock_dashboard_data.xlsx"

def fetch_data(tickers):
    frames = []
    for ticker in tickers:
        print(f"Fetching {ticker}...")
        df = yf.download(ticker, period=PERIOD, interval=INTERVAL, progress=False)
        if df.empty:
            continue
        df = df.reset_index()
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [c[0] for c in df.columns]
        df["Stock Symbol"] = ticker
        try:
            df["Company Name"] = yf.Ticker(ticker).info.get("shortName", ticker)
        except Exception:
            df["Company Name"] = ticker
        frames.append(df)
    return pd.concat(frames, ignore_index=True)

def clean_data(df):
    df = df.rename(columns={
        "Open": "Opening Price", "Close": "Closing Price",
        "High": "Highest Price", "Low": "Lowest Price",
        "Volume": "Trading Volume"
    })
    df = df.dropna(subset=["Opening Price", "Closing Price"])
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    return df.sort_values(["Stock Symbol", "Date"])

def add_metrics(df):
    df["Daily Return %"] = df.groupby("Stock Symbol")["Closing Price"].pct_change() * 100
    df["MA_7"] = df.groupby("Stock Symbol")["Closing Price"].transform(lambda s: s.rolling(7).mean())
    df["MA_30"] = df.groupby("Stock Symbol")["Closing Price"].transform(lambda s: s.rolling(30).mean())
    return df

if __name__ == "__main__":
    print("Data fetch ho raha hai...")
    raw = fetch_data(TICKERS)
    cleaned = clean_data(raw)
    final = add_metrics(cleaned)
    final.to_excel(OUTPUT_FILE, index=False)
    print(f"Ban gaya: {OUTPUT_FILE}")