**Bitcoin Sentiment Analysis**

**Project Overview**

Bitcoin, the 'Digital Gold,' reached a $1 trillion market cap in 2021, but its volatility creates uncertainty. Our system combines sentiment and price trend analysis from platforms like Reddit to guide investors through the emotional and numerical complexities of the Bitcoin market.

**Problem Statement**

In the cryptocurrency world, Binance Investment Group faces a challenge: How to maximize returns and minimize risks in the volatile Bitcoin market? To address this, we're creating a system that integrates sentiment and price trend analysis. Benefits include understanding market psychology, adopting proactive investment strategies, and enhancing risk management. Sentiment analysis offers insights into market sentiment, potentially serving as a leading indicator, allowing investors to prepare for price movements based on sentiment shifts.

**Data Science Process Used**

 The Data Science Process that is adhered to in this analysis is the **CRISP-DM Process :**

**1.0. Business Understanding**

Cryptocurrencies, led by Bitcoin, have surged in popularity, with debates over their future significance. We recognize the potential in this digital financial system and aim to create a data-driven model for cryptocurrency investors. The project addresses the need for data insights in the volatile Bitcoin market and leverages sentiment analysis from Reddit to understand public perception and trends.

**2.0. Data Understanding**

***What data did we use?***

Data files were obtained from [SocialGrep](https://socialgrep.com/datasets/reddit-r-bitcoin-data-for-jun-2022).
The firt dataset **Reddit_Comments** This dataset captures public sentiment through comments in the Bitcoin subreddit for June 2022. With 170,032 individual comments, it offers a granular view of public discussions and reactions related to Bitcoin in this specific month.
The second dataset **Reddit_Posts** .This dataset comprises 7,541 posts from the Bitcoin subreddit for June 2022. It provides insights into the main topics, discussions, and sentiment concerning Bitcoin during this month.

Our third dataset **Bitcoin_Prices** was obtained from .[https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrency-historical-prices-coingecko/versions/57?resource=download&select=bitcoin.csv).  This dataset provides a historical view of Bitcoin's market metrics spanning from January 1, 2015, to November 16, 2022. It contains data on Bitcoin's price, trading volume, and market capitalization across 2,876 records. 

**3.0. Data Preparation**

In this stage, data is cleaned, renaming of the columnsis done to aid in clarity and eliminate redundancy.Feature engineering was done to calculate the polarity scores using the VADER sentiment intensity analyzer on text data using a function that Converts to Lowercase,Handle URLs,Handle Numbers,Handle Mentioned Usernames,Expand Contractions,Tokenization,Removing Short Words,Remove Stopwords and Perform Lemmatization.

In the NLP pre-processing phase, the removal of URLs, unnecessary terms, punctuation, and stopwords served to distill the text for sentiment analysis, resulting in a cleaner, more focused dataset primed for accurate emotion and sentiment extraction. The libraries used included, Pandas, NLTK, POS tagging. These provided efficient and specialized tools in text cleaning and manipulation for NLP tasks.

  ***EDA***

  Lets visualize the word clouds for comments categorized as 'positive', 'negative', and 'neutral' to gain insights into the language   and topics associated with each sentiment category.


  <div align="center">
  <h3>Positive Words</h3>
  <img src=" ![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/b22fd999-a43d-4323-9182-ba27232ff184)" alt="Positive Words" width="200">
</div>

<div align="center">
  <h3>Negative Words</h3>
  <img src="![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/bab75dbd-4fbd-475b-80cb-d4b671b97ac7)jpg" alt="Negative Words" width="200">
</div>

  <div align="center">
  <h3>Neutral Words</h3>
  <img src="![image](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/ce06ff52-0255-48c0-b7b1-925036e20160)
" alt="Neutral Words" width="200">
</div>
  
  
  


  


  
  
**4.0. Modelling**

We explored the effectiveness of various machine learning models in categorizing text-based data into sentiment classes. We employed a range of models to capture the nuances of sentiment expressed in textual content.
The best performing models was DistilBERT.

Below is a table showing all the metric results of the diffrent models that we tried. 

![IMG_7741](https://github.com/Crypto-Web-Weavers/Bitcoin-Sentiment-Analysis/assets/124693318/2124991e-411d-47da-818d-263538c3cc0f)






**5.0. Conclusion**

Our preferred sentiment analysis model was DistilBERT, which delivered an impressive 88.11% test accuracy. Our study also revealed a moderate positive correlation (0.315) between public sentiment on Reddit and Bitcoin price movements, indicating the potential for sentiment to influence prices. Conversely, sentiment showed a slight negative correlation (-0.220) with Bitcoin trading volume, suggesting that volume increased during negative sentiment periods. Key terms like "like," "good," and "stupid" were found to be influential in sentiment analysis, reflecting the diverse range of sentiments within the Bitcoin community.


**6.0 Model Recommendation For Our Stakeholder**

**Real-Time Sentiment Monitoring:** Integrate DistilBERT into a real-time system to track sentiment on cryptocurrency platforms, enabling quick responses to emerging trends.

**Sentiment in Investment:** Use sentiment analysis as an additional input when forecasting Bitcoin price movements. Positive sentiment could signal increased Bitcoin allocation, and vice versa.

**Monitor Trading Volumes:** Be vigilant during periods of negative sentiment coupled with high trading volumes, which might indicate opportunities for strategic buying.

**Community Engagement:** Engage with the Bitcoin community on platforms like Reddit. Address concerns, provide insights, and foster positive sentiment.

**Diversify Data Sources:** Expand sentiment analysis beyond Reddit to include Twitter, forums, and news articles for a broader market sentiment perspective.


**7.0. Whats Next ?**

**Continuous Model Refinement:** Regularly train and evaluate our model with new data to enhance its robustness and generalization, ensuring it stays relevant as Bitcoin community terminology evolves.

**Consider External Factors:** Acknowledge that correlation isn't causation and explore external factors such as negative news, regulations, and economic influences in our analysis of Bitcoin prices.

**Time Series Forecasting:** Utilize time series forecasting to incorporate multiple indicators and data sources for more informed investment decisions, strengthening recommendations to Binance Investment Group.

**Sentiment as Leading Indicator:** Investigate sentiment as a leading indicator for Bitcoin price by analyzing time lags and performing advanced tests like Granger causality, potentially integrating it into our investment strategies if proven effective.





