# FlipKartWebScrapper

This Flask-based web app extracts product reviews from Flipkart using a search string. 
Though it could be optimized, it provides a good starting point for building a web scraper or performing data extraction from e-commerce sites.

This Flask-based web application allows users to scrape product reviews from Flipkart by inputting a search string for a specific product. The app uses libraries such as Flask, Beautiful Soup, and Requests to extract data from Flipkart.

The app has two primary routes: the home page and the result page. The home page displays a search form where users can enter a product's name or a specific search string. Upon submitting the search, the app sends a request to Flipkart's website and retrieves a list of reviews that match the search criteria.

The code for the app is well structured, with separate functions for each page, and proper error handling to provide meaningful error messages to the user. The app also implements logging to record any errors that may occur during the scraping process.

However, the app could be optimized to improve its performance. One issue is that the app makes requests to Flipkart's website for each review, which can slow down the app's performance. To improve this, the app could use techniques such as caching to store the results of previous requests, throttling requests to limit the number of requests made in a certain timeframe, and using asynchronous programming to perform concurrent requests.

Despite these optimization issues, the app can serve as a useful starting point for anyone looking to build a web scraper or extract data from e-commerce websites. It can be easily modified to scrape reviews from other e-commerce sites such as Amazon or Walmart.

In summary, this Flask-based web application provides a simple yet effective way to extract product reviews from Flipkart using a search string input. Although it can be further optimized, it provides a solid foundation for anyone looking to build a web scraper or perform data extraction from e-commerce sites.
