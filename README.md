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

#### Clone the repository
``git clone https://github.com/bitparanoid27/stock-manthan.git
cd stock-manthan``

#### Create and activate virtual environment
`python -m venv venv`

#### Activate (Mac/Linux)
`source venv/bin/activate`

#### Activate (Windows)
`venv\Scripts\activate`

##### Install dependencies
`pip install -r requirements.txt`

### 3. OpenBB Configuration
This project does not use a standard .env file for keys. Instead, it pulls credentials from the OpenBB local configuration.
Ensure your JSON configuration (typically located in ~/.openbb_terminal/ or handled via openbb.user.credentials) is correctly set up with your active API provider keys.

To verify your setup, you can run:
`openbb login`

### Note: The script expects the OpenBB environment to be pre-authorized to fetch financial statements and daily price data.
📈 Usage
To run the analysis engine and generate a report for the target tickers, execute:
`python presentation.py`

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
--- 
## Output
<img width="722" height="692" alt="image" src="https://github.com/user-attachments/assets/14a79349-db67-4579-b13a-25a6d9c78539" />

# Disclaimer: This tool is for educational purposes. It provides data analysis based on a specific methodology and does not constitute financial advice.

