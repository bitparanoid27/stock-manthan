from data_provider import get_stock_fundamental_data
import pandas as pd
from datetime import datetime, timedelta
from utils import safe_calculator


# Logical thought one master fns calling 15 independent functions
# Those independent functions will be various criteria parameters such sales growth for last 3 years > 8 etc.

@safe_calculator
def revenue_growth_3y(financial_df):
    latest_year = financial_df['fiscal_year'].max()
    start_year = latest_year - 3
    current_year_revenue = financial_df[financial_df['fiscal_year'] == latest_year]['revenue'].item()
    start_year_revenue = financial_df[financial_df['fiscal_year'] == start_year]['revenue'].item()

    cagr_revenue_growth = (current_year_revenue / start_year_revenue) ** (1 / 3) - 1
    print(f"Sales growth {cagr_revenue_growth}")
    return cagr_revenue_growth


@safe_calculator
def profit_growth_3y(financial_df):
    latest_year = financial_df['fiscal_year'].max()
    start_year = latest_year - 3
    current_year_profit = financial_df[financial_df['fiscal_year'] == latest_year]['total_pre_tax_income'].item()
    start_year_profit = financial_df[financial_df['fiscal_year'] == start_year]['total_pre_tax_income'].item()

    cagr_profit_growth = (current_year_profit / start_year_profit) ** (1 / 3) - 1
    print(f"Profit growth {cagr_profit_growth}")
    return cagr_profit_growth


@safe_calculator
def return_on_equity_growth_ttm(financial_qtr_df):
    shareholders_fund_data = financial_qtr_df['total_assets'] - financial_qtr_df['total_liabilities']
    latest_shareholders_fund = shareholders_fund_data.iloc[0]

    net_income_data = financial_qtr_df['bottom_line_net_income']
    total_net_income = net_income_data.sum()
    ttm_roe = total_net_income / latest_shareholders_fund

    print(f"Trailing Twelve Months ROE: {ttm_roe}")
    return ttm_roe


@safe_calculator
def return_on_equity_growth_5y(financial_df):
    # latest_year = financial_df['fiscal_year'].max()
    # start_year = latest_year - 3
    # current_year_assets = financial_df[financial_df['fiscal_year'] == latest_year]['total_assets'].item()
    # current_year_liabilities = financial_df[financial_df['fiscal_year'] == latest_year]['total_liabilities'].item()
    # shareholders_fund = current_year_assets - current_year_liabilities

    shareholders_fund_data = financial_df['total_assets'] - financial_df['total_liabilities']
    net_income = financial_df['bottom_line_net_income']
    # roe = (net_income/shareholders_fund_data) * 100
    roe = net_income / shareholders_fund_data
    # current_roe = net_income.iloc[0]/shareholders_fund_data.iloc[0]
    return_on_equity_median = roe.median()

    # print(shareholders_fund_data)
    # print(net_income)
    # print(roe)
    # print(f"Current ROE {current_roe}")
    print(f"5Y Median ROE growth {return_on_equity_median}")
    return return_on_equity_median

    # if return_on_equity_median/100 > 0.18:
    #     return return_on_equity_median
    # elif return_on_equity_median/100 > 0.15:
    #     return return_on_equity_median


@safe_calculator
def return_on_capital_employed_ttm(financial_qtr_df):
    ebit_data = financial_qtr_df['ebit']
    total_ebit = ebit_data.sum()

    shareholders_fund_data = financial_qtr_df['total_assets'] - financial_qtr_df['total_liabilities']
    latest_shareholders_fund = shareholders_fund_data.iloc[0]

    debt_data = financial_qtr_df['total_debt']
    latest_debt = debt_data.iloc[0]
    latest_capital_employed = latest_shareholders_fund + latest_debt

    ttm_roce = total_ebit / latest_capital_employed
    print(f"Trailing Twelve Months ROCE: {ttm_roce}")
    return ttm_roce


@safe_calculator
def return_on_capital_employed_growth_5y(financial_df):
    ebit = financial_df['ebit']
    shareholders_fund_data = financial_df['total_assets'] - financial_df['total_liabilities']
    debt_data = financial_df['total_debt']
    capital_employed = shareholders_fund_data + debt_data

    # print(shareholders_fund_data)
    # print(debt_data)
    # print(capital_employed)

    roce_data = ebit / capital_employed
    # current_roce = ebit.iloc[0]/capital_employed.iloc[0]
    roce_median = roce_data.median()
    # print(f"Current ROCE {current_roce}")
    print(f"5Y Median ROCE growth {roce_median}")
    return roce_median


@safe_calculator
def debt_to_equity(financial_df):
    total_debt_data = financial_df['total_debt']
    shareholders_fund_data = financial_df['total_assets'] - financial_df['total_liabilities']

    debt_to_equity_ratio = total_debt_data.iloc[0] / shareholders_fund_data.iloc[0]
    print(f"Debt to equity ratio {debt_to_equity_ratio}")
    return debt_to_equity_ratio


@safe_calculator
def share_price_growth_3y(price_df):
    current_year = datetime.now().date()
    last_year = current_year.replace(year=current_year.year - 1)
    first_year = current_year.replace(year=current_year.year - 3)

    current_year_price = price_df.asof(current_year)['close']
    last_year_price = price_df.asof(last_year)['close']
    first_year_price = price_df.asof(first_year)['close']

    total_price_growth = (current_year_price / first_year_price) - 1
    print(f"Price growth over 3 years {total_price_growth}")
    return total_price_growth


# Valuation phase

@safe_calculator
def cfo_pat_ratio(financial_df):
    sum_of_cfo = financial_df['operating_cash_flow'].sum()
    sum_of_pat = financial_df['bottom_line_net_income'].sum()

    cfo_pat_data = (sum_of_cfo / sum_of_pat)
    print(f"CFO/PAT Ratio: {cfo_pat_data}")
    return cfo_pat_data


@safe_calculator
def avg_tax_rate_5y(financial_df):
    effective_tax_rate = financial_df['income_tax_expense'] / financial_df['total_pre_tax_income']
    avg_tax_rate = effective_tax_rate.mean()
    print(f"Avg tax rate : {avg_tax_rate}")
    return avg_tax_rate


@safe_calculator
def continuous_commitment_to_growth(financial_df):
    revenue_data = financial_df['revenue'].iloc[::-1]
    revenue = revenue_data.diff()
    revenue_growth = (revenue.dropna() > 0).all()
    print(f"Continuous revenue growth: {revenue_growth}")

    pat_data = financial_df['bottom_line_net_income'].iloc[::-1]
    pat = pat_data.diff()
    pat_growth = (pat.dropna() > 0).all()
    print(f"Continuous profit after tax growth growth: {pat_growth}")

    diluted_eps_data = financial_df['diluted_earnings_per_share'].iloc[::-1]
    diluted_eps = diluted_eps_data.pct_change()
    diluted_eps_growth = diluted_eps.dropna().mean()
    print(f"Continuous EPS growth: {diluted_eps_growth}")

    conservative_diluted_eps_growth = min(diluted_eps_growth, 0.30)
    print(f"Conservative EPS growth: {conservative_diluted_eps_growth}")
    return revenue_growth, pat_growth, diluted_eps_growth, conservative_diluted_eps_growth


@safe_calculator
def equity_multiplier(financial_df):
    total_assets = financial_df['total_assets']
    total_assets_5y_avg = total_assets.mean()

    total_equity = financial_df['total_assets'] - financial_df['total_liabilities']
    total_equity_5y_avg = total_equity.mean()

    total_equity_multiplier = (total_assets_5y_avg / total_equity_5y_avg)
    print(f"Equity multiplier: {total_equity_multiplier}")
    return total_equity_multiplier


@safe_calculator
def price_to_earnings_ratio(financial_qtr_df, price_df):
    current_year = datetime.now().date()
    # current_market_price = price_df.asof(current_year)['close']
    market_price = price_df['close'].iloc[-1]
    print(f"Current market price: {market_price} & price-date {current_year}")

    ttm_earnings = financial_qtr_df['diluted_earnings_per_share'].sum()
    if ttm_earnings <= 0:
        print(f"Earnings reported less than or close 0")
    else:
        pe_ratio = (market_price / ttm_earnings)
        print(f"Current Price/Earnings ratio: {pe_ratio}")
        return pe_ratio


@safe_calculator
def peg_ratio(pe_ratio_data, eps_growth_data, conservative_eps_growth_data):
    # pe_data = price_to_earnings_ratio(financial_qtr_df, price_df)
    # _, _, eps_data, conservative_eps_data = continuous_commitment_to_growth(financial_df)
    # conservative_eps_data = continuous_commitment_to_growth(financial_df)

    pe_data = pe_ratio_data
    eps_data = eps_growth_data
    conservative_eps_data = conservative_eps_growth_data

    eps = eps_data * 100
    conservative_eps = conservative_eps_data * 100
    current_peg_ratio = (pe_data / eps)
    print(f"Current PEG ratio: {current_peg_ratio} ")

    conservative_peg_ratio = (pe_data / conservative_eps)
    print(f"Conservative PEG ratio: {conservative_peg_ratio} ")
    return current_peg_ratio, conservative_peg_ratio


@safe_calculator
def cvc_ratio(price_df, financial_df, financial_qtr_df, pe_ratio_data):
    # code to find close prices of last 5 years
    today_date = datetime.now().date()
    five_years_ago = today_date.replace(year=today_date.year - 5)
    month_end_data = pd.date_range(five_years_ago, today_date, freq='BME')

    sorted_prices = price_df.sort_index()
    month_end_prices_data = sorted_prices.reindex(month_end_data, method='ffill')['close']

    annual_eps_data = financial_df[['period_ending', 'diluted_earnings_per_share']]
    annual_eps_data_df = annual_eps_data.copy()
    ttm_eps_data = financial_qtr_df['diluted_earnings_per_share'].sum()

    # convert series into a dataframe
    month_end_prices_data_df = month_end_prices_data.reset_index()

    # Need common columns to merge so using index and period_ending by renaming them date
    # & dt.year line helps us merge two table with 60 row and 5 row info without losing data
    month_end_prices_data_df['year'] = month_end_prices_data_df['index'].dt.year
    month_end_prices_data_df = month_end_prices_data_df.rename(columns={'index': 'date'})

    # Convert the 'period_ending' column to datetime datatype.
    annual_eps_data_df['period_ending'] = pd.to_datetime(annual_eps_data_df['period_ending'])
    annual_eps_data_df['year'] = annual_eps_data_df['period_ending'].dt.year
    annual_eps_data_df = annual_eps_data_df.rename(columns={'period_ending': 'date'})

    # Data collection and aggregation for current year i.e. using quarterly data
    quarter_eps_data = financial_qtr_df[['period_ending', 'diluted_earnings_per_share']]
    quarter_eps_data_df = quarter_eps_data.copy()
    quarter_eps_data_df['period_ending'] = pd.to_datetime(quarter_eps_data_df['period_ending'])
    quarter_eps_data_df['year'] = quarter_eps_data_df['period_ending'].dt.year
    quarter_eps_data_df = quarter_eps_data_df.rename(columns={'period_ending': 'date'})

    cvc_data = pd.merge(month_end_prices_data_df, annual_eps_data_df, on='year', how="left")

    current_year = datetime.now().year
    cvc_data.loc[cvc_data['year'] == current_year, 'diluted_earnings_per_share'] = ttm_eps_data
    cvc_data['historical_pe'] = cvc_data['close'] / cvc_data['diluted_earnings_per_share']
    median_pe_5y = cvc_data['historical_pe'].median()

    cvc_number = pe_ratio_data / median_pe_5y
    # print(f"{cvc_data}")
    print(f"Current valuation co-efficient: {cvc_number}")
    return cvc_number


@safe_calculator
def stock_manthan(search_stock_symbol):
    sec_returned_data, price_returned_data, sec_returned_quarter_data = get_stock_fundamental_data(search_stock_symbol)
    # print(f"SEC returned data: {sec_returned_data} ")

    if sec_returned_data is None:
        print(f"In-valid symbol or error in retrieving data or maybe searching for premium tickers")
        return None

    # creating a report of all collected data:
    report = {}

    print(f"Testing the first independent fn")
    report['revenue_growth_3y'] = revenue_growth_3y(sec_returned_data)
    report['profit_growth_3y'] = profit_growth_3y(sec_returned_data)

    report['roe_ttm'] = return_on_equity_growth_ttm(sec_returned_quarter_data)
    report['roe_5y'] = return_on_equity_growth_5y(sec_returned_data)

    report['roce_ttm'] = return_on_capital_employed_ttm(sec_returned_quarter_data)
    report['roce_5y'] = return_on_capital_employed_growth_5y(sec_returned_data)

    report['debt_to_equity'] = debt_to_equity(sec_returned_data)

    report['price_growth_3y'] = share_price_growth_3y(price_returned_data)
    report['cfo_pat_ratio'] = cfo_pat_ratio(sec_returned_data)
    report['avg_tax_5y'] = avg_tax_rate_5y(sec_returned_data)
    revenue_growth, pat_growth, eps_growth, conservative_eps_growth = continuous_commitment_to_growth(sec_returned_data)
    report['revenue_growth'] = revenue_growth
    report['pat_growth'] = pat_growth
    report['eps_growth'] = eps_growth
    report['conservative_eps_growth'] = conservative_eps_growth

    report['equity_multiplier'] = equity_multiplier(sec_returned_data)
    report['pe_ttm'] = price_to_earnings_ratio(sec_returned_quarter_data, price_returned_data)
    current_peg_ratio, conservative_peg_ratio = peg_ratio(report.get('pe_ttm'),
                                                          report.get('eps_growth'),
                                                          report.get('conservative_eps_growth'))

    report['current_peg_ratio'] = current_peg_ratio
    report['conservative_peg_ratio'] = conservative_peg_ratio
    report['cvc_ratio'] = cvc_ratio(price_returned_data, sec_returned_data, sec_returned_quarter_data,
                                    report.get('pe_ttm'))

    print(f"Evaluation report for the stock {search_stock_symbol} /n {report}")
    return report


# stock_manthan("AAPL")
