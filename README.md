![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124519816/c095d42c-a785-4367-8577-3cf79c7d1ec2)

# Bitcoin Sentiment Analysis

## 1.0. Business Understanding

Cryptocurrencies, led by Bitcoin, have surged in popularity, with debates over their future significance. We recognize the potential of this digital financial system and aim to create a data-driven model for cryptocurrency investors. The project addresses the need for data insights in the volatile Bitcoin market and leverages sentiment analysis from Reddit to understand public perception and trends.

### 1.1. Project Overview

Bitcoin, the 'Digital Gold', reached a $1 trillion market cap in 2021, but its volatility creates uncertainty. Our system combines sentiment and price trend analysis from platforms like Reddit to guide investors through the emotional and numerical complexities of the Bitcoin market.

### 1.2. Problem Statement

In the cryptocurrency world, Binance Investment Group faces a challenge: How to maximize returns and minimize risks in the volatile Bitcoin market? To address this, we're creating a system that integrates sentiment and price trend analysis. Benefits include understanding market psychology, adopting proactive investment strategies, and enhancing risk management. Sentiment analysis offers insights into market sentiment, potentially serving as a leading indicator, allowing investors to prepare for price movements based on sentiment shifts.

## 2.0. Data Understanding

**What data did we use?**

Data files were obtained from [SocialGrep](https://socialgrep.com/datasets/reddit-r-bitcoin-data-for-jun-2022).
The first dataset **Reddit_Comments** This dataset captures public sentiment through comments in the Bitcoin subreddit for June 2022. With 170,032 individual comments, it offers a granular view of public discussions and reactions related to Bitcoin in this specific month.
The second dataset is **Reddit_Posts**. This dataset comprises 7,541 posts from the Bitcoin subreddit for June 2022. It provides insights into the main topics, discussions, and sentiment concerning Bitcoin during this month.

Our third dataset **Bitcoin_Prices** was obtained from [Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrency-historical-prices-coingecko/versions/57?resource=download&select=bitcoin.csv).  This dataset provides a historical view of Bitcoin's market metrics spanning from January 1, 2015, to November 16, 2022. It contains data on Bitcoin's price, trading volume, and market capitalization across 2,876 records. 

## 3.0. Data Preparation

In this stage, data is cleaned, and renaming of the columns is done to aid in clarity and eliminate redundancy. Feature engineering was done to calculate the polarity scores using the VADER sentiment intensity analyzer on text data using a function that Converts to Lowercase, Handles URLs, Handles Numbers, Handle Mentioned Usernames, Expand Contractions, Tokenization, Removing Short Words, Removes Stopwords and Performs Lemmatization.

In the NLP pre-processing phase, the removal of URLs, unnecessary terms, punctuation, and stopwords served to distill the text for sentiment analysis, resulting in a cleaner, more focused dataset primed for accurate emotion and sentiment extraction. The libraries used included Pandas and NLTK. These provided efficient and specialized tools in text cleaning and manipulation for NLP tasks.

  ### 3.1. Exploratory Data Analysis

Let's visualize the word clouds for comments categorized as 'positive', 'negative', and 'neutral' to gain insights into the language   and topics associated with each sentiment category.
  
**Positive words**

![download (1)](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/127657429/0c2b0d2b-0510-4e90-82c7-7186c5c739ae)
  
**Negative words**

![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/2b55d405-ba45-44f8-8c3d-cdd8806a0dff)


**Neutral words**

![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/24965402-83d3-4ae4-aa1d-e6c9196143af)

**Relationship between Sentiment, Trading Volume, and Bitcoin Prices**

![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/18f713ba-f506-435b-aa52-871f2f623a13)

**Sentiment and Price Correlation:** There's a discernible correlation between sentiment and Bitcoin price throughout the month of June. On days when the sentiment is positive, the Bitcoin price tends to rise. Conversely, when the sentiment dips into negative territory, the Bitcoin price often shows a decline. This suggests that public sentiment can be a good indicator of price movement, or vice versa.

**Trade Volume Observations:** Significant trading volumes, as depicted by taller blue bars, often coincide with notable changes in sentiment and price. This is expected, as heightened trading activity often reflects a reaction to prevailing sentiments or significant price movements.


## 4.0. Modelling

We explored the effectiveness of various machine learning models in categorizing text-based data into sentiment classes. We employed a range of models to capture the nuances of sentiment expressed in textual content.

Below is a table showing all the metric results of the different models that we tried. 

![MODEL](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/fdcc2ba4-00ea-4c6c-8a45-93c925fb5354)

## 5.0. Evaluation

**Best Model Selection:**  Our chosen model for deployment is the tuned DistilBERT.

The model results were as follows:

F1 Score: Train - 91.87%, Test - 88.07% 

ROC-AUC Score: Train - 97.25%, Test - 95.31%

Loss: Train - 0.403, Validation - 0.417


**Unseen Test Data Evaluation**

F1 Score: 60% 

ROC-AUC: 74%

Overall the model showed  decent sentiment class differentiation capability.


## 6.0. Deployment

In the deployment process for the Bitcoin Sentiment Analysis application, we did the following:

 Prepared a Streamlit app for user interaction and sentiment analysis.
 
 Managed large model files using Git LFS for efficient version control.
 
 Deployed the app on Streamlit Sharing for public access.
 
![deployment](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/38150405-17df-4905-8b42-9f38807198c0)



## 7.0. Conclusion

- Our preferred sentiment analysis model was DistilBERT, boasting an impressive train and test F1-score of 91.87% and 88.07% respectively. 

- Our study also revealed a moderate positive correlation (0.315) between public sentiment on Reddit and Bitcoin price movements, indicating the potential for sentiment to influence prices. Conversely, sentiment showed a slight negative correlation (-0.220) with Bitcoin trading volume, suggesting that volume increased during negative sentiment periods.
  
- Key terms like "like," "good," and "stupid" were found to be influential in sentiment analysis, reflecting the diverse range of sentiments within the Bitcoin community.


## 8.0. Recommendations

**Real-Time Sentiment Monitoring:** Integrate DistilBERT into a real-time system to track sentiment on cryptocurrency platforms, enabling quick responses to emerging trends.

**Sentiment in Investment:** Use sentiment analysis as an additional input when forecasting Bitcoin price movements. Positive sentiment could signal increased Bitcoin allocation, and vice versa.

**Monitor Trading Volumes:** Be vigilant during periods of negative sentiment coupled with high trading volumes, which might indicate opportunities for strategic buying.

**Community Engagement:** Engage with the Bitcoin community on platforms like Reddit. Address concerns, provide insights, and foster positive sentiment.

**Diversify Data Sources:** Expand sentiment analysis beyond Reddit to include Twitter, forums, and news articles for a broader market sentiment perspective.


## 9.0. What's Next?

**Continuous Model Refinement:** Regularly train and evaluate our model with new data to enhance its robustness and generalization, ensuring it stays relevant as Bitcoin community terminology evolves.

**Consider External Factors:** Acknowledge that correlation isn't causation and explore external factors such as negative news, regulations, and economic influences in our analysis of Bitcoin prices.

**Time Series Forecasting:** Utilize time series forecasting to incorporate multiple indicators and data sources for more informed investment decisions, strengthening recommendations to Binance Investment Group.

**Sentiment as Leading Indicator:** Investigate sentiment as a leading indicator for Bitcoin price by analyzing time lags and performing advanced tests like Granger causality, potentially integrating it into our investment strategies if proven effective.

