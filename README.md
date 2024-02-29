# Stock Dashboard

This Stock Dashboard allows you to visualize stock data interactively. To get started, follow the installation instructions and setup guide below.

## Installation

First, clone this repository to your local machine. Then, install the required packages using pip:

```bash
pip3 install yfinance
pip3 install plotly-express
pip3 install streamlit
pip3 install alpha-vantage
pip3 install python-dotenv
```

## API Key Setup

To fetch stock data, you'll need an API key from Alpha Vantage.

1. Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
2. Create a `.env` file in the root directory of this project.
3. Add the following line to your `.env` file, replacing `your_api_key_here` with your actual API key:

```env
API_KEY=your_api_key_here
```

## Launching the Dashboard
To view the dashboard locally, run the following command in your terminal:
```bash
streamlit run Stock_Dashboard.py
```

## Screenshots

Here are some screenshots of what the dashboard looks like:

![Screenshot 1](https://github.com/QiQiEva/Stock-Dashboard/assets/138655040/52053f08-4c09-404d-8551-ef07550c945e)

![Screenshot 2](https://github.com/QiQiEva/Stock-Dashboard/assets/138655040/adb4ec37-4e3c-4856-9e7a-532670bb0005)

![Screenshot 3](https://github.com/QiQiEva/Stock-Dashboard/assets/138655040/0c54106c-b0e7-44a2-ad60-7e4387044c3b)
