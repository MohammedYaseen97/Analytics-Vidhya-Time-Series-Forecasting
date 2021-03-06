My solution to solve a time series forecasting challenge on Analytics Vidhya's website - [Time Series Forecasting](https://datahack.analyticsvidhya.com/contest/practice-problem-time-series-2/).

My score : 190.3344967260

## About Practice Problem: Time Series
Time Series forecasting & modeling plays an important role in data analysis. Time series analysis is a specialized branch of statistics used extensively in fields such as Econometrics & Operation Research.

Time Series is being widely used in analytics & data science. This is specifically designed time series problem for you and challenge is to forecast traffic.

## Data
We are provided with a Time Series problem involving prediction of number of commuters of JetRail, a new high speed rail service by Unicorn Investors. We are provided with 2 years of data(Aug 2012-Sept 2014) and using this data we have to forecast the number of commuters for next 7 months.

We are given 2 years of data(2012-2014) at hourly level with the number of commuters travelling and we need to estimate the number of commuters for future.

## Approach
I have used the Holt-Winter method of moving averages to calculate the moving averages which takes into account the level, trend and seasonality. Not bad for a first time, huh ? ;)
