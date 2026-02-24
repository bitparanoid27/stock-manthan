This is the codified version of Stock Manthan process as highlighted in the book Stock Manthan - The hunt for Multibagger stocks [ https://www.goodreads.com/book/show/55591522-stock-manthan ]. 
In the book process was applied for the Indian stock, but I've used to same process to sift and find out multi-bagger stocks in the US stocks. 

The process is quite simple it basically filtering stocks on certains criteria as listed below: 
For a stock to clear initial screening it must satisfy the below criteria.
  - Sales / revenue growth for last 3 years >= 8%
  - Profit growth for last 3 year >= 10%
  - Minimum return on investment for last 3 years >= 15%
  - Average return on investment for last 5 years >= 14%
  - Minimum return on capital employed for last 3 years >= 15%
  - Minimum return on capital employed for last 5 years >= 14%
  - Maximum debt to equity ratio = 1.0
  - Stock price appreciation in last 3 years >= 30%

This ensures we're only selecting stocks where sales are increasing, shareholders funds are appreciating, capital employed is working in favour of earning returns for shareholders, and debt is under-control. So it eliminates companies which using debt to growth more than the acceptable limit. 

For the valuation phase the above selected stock(s) must satisfy the below mentioned criteria:
- Cashflow to operations / Profit after tax ratio should be >= 75%
- Firm's tax slab should be in the acceptable range ( 18% to 36% )
- Equity multiplier should be < 4
- Peg ratio i.e. P/E ratio / growth should be < 2
- CVC ratio co-efficient of valuation < 2. It's stock 5 years (60 months) of average p/e divided by (60 months) stock price. It helps us understand whether the stock is being fairly priced. Ideal cvc ratio should be around 1.

stock manthan report for Google date 24/02/2026 
<img width="718" height="682" alt="image" src="https://github.com/user-attachments/assets/5808079a-9f5f-4d63-9faf-b03fa8f275bb" />

The project is still being developed, so additional functionalities such as md&a would be added to decipher the corporate lingo to retrieve insights for for DIY investor. 

# Stock Manthan: US Equity Screening Engine 📈

A quantitative financial analysis tool built to automate the "Stock Manthan" methodology for the US Stock Market. This engine sifts through thousands of equities to identify high-quality, "multi-bagger" stocks using rigorous financial KPIs and valuation metrics.

---

## 🚀 Overview
Based on the principles in the book *Stock Manthan*, this project replaces manual spreadsheet analysis with a codified system. It evaluates companies based on growth, capital efficiency, debt management, and fair-value pricing.

### Core Evaluation Logic:
1.  **Fundamental Screening:** Filters for 3-5 year trends in Revenue, Profit, ROI, and ROCE (all >15%).
2.  **Solvency Check:** Ensures Debt-to-Equity is < 1.0 to avoid over-leveraged companies.
3.  **Valuation Phase:** Calculates the **CVC Ratio (Coefficient of Valuation)** using 60 months of historical P/E and price data to determine if a stock is fairly priced (target ≈ 1.0).

## 🛠 Tech Stack
*   **Language:** Python 3.9+
*   **Data Aggregation:** [OpenBB SDK](https://openbb.co/), [Financial Modeling Prep (FMP)](https://site.financialmodelingprep.com/)
*   **Data Processing:** Pandas, NumPy
*   **Environment Management:** Python-dotenv

## ⚙️ Setup & Installation

### 1. Prerequisites
*   A **Financial Modeling Prep (FMP) API Key** (Get one [here](https://site.financialmodelingprep.com/developer/docs/)).
*   An **OpenBB** account for financial data retrieval.

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/bitparanoid27/stock-manthan.git
cd stock-manthan

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt``` 

### 3. OpenBB Configuration
This project does not use a standard .env file for keys. Instead, it pulls credentials from the OpenBB local configuration.
Ensure your JSON configuration (typically located in ~/.openbb_terminal/ or handled via openbb.user.credentials) is correctly set up with your active API provider keys.

To verify your setup, you can run:
`openbb login`

### Note: The script expects the OpenBB environment to be pre-authorized to fetch financial statements and daily price data.
📈 Usage
To run the analysis engine and generate a report for the target tickers, execute:
` python presentation.py `

🔍 Key Metrics Tracked
  The engine implements a multi-stage filtering algorithm:
    Sales/Profit Growth: >= 8% - 10% over 3 years.
    Capital Returns: ROI/ROCE >= 15% (3yr/5yr averages).
    Price Appreciation: >= 30% over 3 years.
    Integrity Check: Cashflow to Operations / PAT ratio >= 75%.
    Valuation: PEG Ratio < 2.0 and Equity Multiplier < 4.

## 🗺 Roadmap

- MD&A Analysis: Parsing "Management Discussion & Analysis" from SEC filings to detect corporate sentiment.
- Batch Processing: Ability to screen entire sectors (e.g., S&P 500 Technology) in a single run.
- Database Integration: Moving from real-time API calls to a PostgreSQL cache for faster historical lookups.

# Disclaimer: This tool is for educational purposes. It provides data analysis based on a specific methodology and does not constitute financial advice.
