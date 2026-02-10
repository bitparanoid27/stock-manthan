from openbb import obb
import pandas as pd
from datetime import datetime, timedelta


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


def get_stock_fundamental_data(stock_symbol):
    try:
        if not stock_symbol:
            print("Stock symbol cannot be empty")
            return

        print(f"Retrieving fundamental data for {stock_symbol}")

        income_statement = obb.equity.fundamental.income(stock_symbol, provider="fmp", limt=5).to_df()
        balance_statement = obb.equity.fundamental.balance(stock_symbol, provider="fmp", limt=5).to_df()
        cashflow_statement = obb.equity.fundamental.cash(stock_symbol, provider="fmp", limt=5).to_df()

        five_years_ago = (datetime.now() - timedelta(days=5 * 365)).strftime('%Y-%m-%d')
        price_data = obb.equity.price.historical(stock_symbol, start_date=five_years_ago, provider='yfinance').to_df()

        print(f"Data retrieval complete")

    #     Merging independent dataframes into a single dataframe

        staged_master_df = pd.concat([income_statement, balance_statement, cashflow_statement], axis=1)
        cleaned_master_df = staged_master_df.loc[:, ~staged_master_df.columns.duplicated()]
        master_df = cleaned_master_df.sort_index(ascending=True)
        print(master_df)

        # Retrieving quarterly data

        qtr_income_statement = obb.equity.fundamental.income(stock_symbol, period="quarter", provider="fmp", limit=4).to_df()
        qtr_balance_statement = obb.equity.fundamental.balance(stock_symbol, period="quarter", provider="fmp", limit=4).to_df()
        qtr_cashflow_statement = obb.equity.fundamental.cash(stock_symbol, period="quarter", provider="fmp", limit=4).to_df()

        staged_master_quarter_df = pd.concat([qtr_income_statement, qtr_balance_statement, qtr_cashflow_statement], axis=1)
        cleaned_master_quarter_df = staged_master_quarter_df.loc[:, ~staged_master_quarter_df.columns.duplicated()]
        master_quarter_df = cleaned_master_quarter_df.sort_index(ascending=True)
        print(master_quarter_df)

        return master_df, price_data, master_quarter_df

    except Exception as e:
        print(f"An error occurred: {e}")
