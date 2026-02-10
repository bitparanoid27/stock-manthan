from analysis import stock_manthan
from rich.console import Console
from rich.table import Table
from rich import box
import config as sm_checklist_config


def present_report(report, ticker, fkconfig):
    # creating class instances
    console = Console()
    table = Table(title="Stock Manthan Report", style="white", header_style="bold cyan", box=box.HEAVY_HEAD)
    table.add_column("Metric"),
    table.add_column("Value"),
    table.add_column("Threshold"),
    table.add_column("Result")

    def add_metric_row(metric_key, metric_name, threshold_key, comparison_logic):
        value = report.get(metric_key)
        threshold = getattr(fkconfig, threshold_key)

        # Handle missing data first
        if value is None:
            table.add_row(metric_name, "N/A", f"{threshold}", "[yellow]N/A[/yellow]")
            return  # Stop the function here for this metric

        is_pass = comparison_logic(value, threshold)
        verdict_str = "[green]PASS[/green]" if is_pass else "[red]FAIL[/red]"

        value_str = f"{value:.4f}"  # Use .4f for 4 decimal places, or .2% for percentage
        threshold_str = f"{threshold}"

        table.add_row(metric_name, value_str, threshold_str, verdict_str)

    table.add_row("Valuation Stage"),
    add_metric_row(
        metric_key='revenue_growth_3y',
        metric_name='3Y Revenue CAGR',
        threshold_key='MIN_REVENUE_CAGR_3Y',
        comparison_logic=lambda v, t: v > t
    )
    add_metric_row(
        metric_key='profit_growth_3y',
        metric_name='3Y Profit CAGR',
        threshold_key='MIN_PROFIT_CAGR_3Y',
        comparison_logic=lambda v, t: v > t
    )
    add_metric_row(
        metric_key='roe_ttm',
        metric_name='RoE TTM',
        threshold_key='MIN_ROE_CURRENT',
        comparison_logic=lambda v, t: v > t
    )
    add_metric_row(
        metric_key='roe_5y',
        metric_name='5Y Median RoE',
        threshold_key='MIN_ROE_AVG_5Y',
        comparison_logic=lambda v, t: v > t
    ),
    add_metric_row(
        metric_key='roce_ttm',
        metric_name='Return on Capital Employed TTM',
        threshold_key="MIN_ROCE_CURRENT",
        comparison_logic=lambda v, t: v > t
    ),
    add_metric_row(
        metric_key='roce_5y',
        metric_name='5y Median Return on Capital Employed',
        threshold_key='MIN_ROCE_AVG_5Y',
        comparison_logic=lambda v, t: v > t
    ),
    add_metric_row(
        metric_key='debt_to_equity',
        metric_name='Debt to Equity ratio',
        threshold_key='MAX_DEBT_TO_EQUITY',
        comparison_logic=lambda v, t: v < t
    ),
    add_metric_row(
        metric_key='price_growth_3y',
        metric_name='3y share price CAGR',
        threshold_key='MIN_RETURN_3Y',
        comparison_logic=lambda v, t: v > t
    )
    table.add_row("Valuation stage"),
    add_metric_row(
        metric_key='cfo_pat_ratio',
        metric_name='CFO/PAT Ratio',
        threshold_key='CFO_PAT',
        comparison_logic=lambda v, t: v > t
    ),
    add_metric_row(
        metric_key='avg_tax_5y',
        metric_name='Tax rate',
        threshold_key='MIN_TAX_RATE',
        comparison_logic=lambda v, t: v > t
    ),
    add_metric_row(
        metric_key='equity_multiplier',
        metric_name='Equity Multiplier',
        threshold_key='MAX_EQUITY_MULTIPLIER',
        comparison_logic=lambda v, t: v < t
    ),
    add_metric_row(
        metric_key='current_peg_ratio',
        metric_name='Current PEG ratio',
        threshold_key='PEG_RATIO',
        comparison_logic=lambda v, t: v < t
    ),
    add_metric_row(
        metric_key='conservative_peg_ratio',
        metric_name='Conservative PEG ratio',
        threshold_key='PEG_RATIO',
        comparison_logic=lambda v, t: v < t
    ),
    add_metric_row(
        metric_key='cvc_ratio',
        metric_name='Current valuation co-efficient CVC',
        threshold_key='CVC_RATIO',
        comparison_logic=lambda v, t: v < t
    ),

    console.print(table)


if __name__ == "__main__":
    # # 1. Create a FAKE report object for testing.
    # #    This is the key. You don't need to run your whole analysis engine.
    # #    Just pretend you did, and create a sample of the data.
    # fake_report = {
    #     'revenue_growth_3y': 0.1075,
    #     'profit_growth_3y': 0.0971,
    #     'roe_ttm': 0.3211,
    #     'pe_ttm': None  # Simulate a failed calculation
    # }
    #
    # # 2. Create a FAKE config object for testing.
    # #    In a real scenario, you would 'import config'
    # class FakeConfig:
    #     MIN_REVENUE_CAGR_3Y = 0.08
    #     MIN_PROFIT_CAGR_3Y = 0.10
    #     MIN_ROE_CURRENT = 0.15

    stock_report = stock_manthan("GOOGL")

    # 3. Call your function with the fake data.
    present_report(stock_report, "GOOGL", sm_checklist_config)
