import requests
import json
from PyQt5.QtCore import QDate, Qt


current_date = QDate.currentDate()
label_date = current_date.toString(Qt.ISODate)
def get_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&from=',label_date,'&apiKey=d56a722eb571486d9ca18ed02ceb9edd'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d56a722eb571486d9ca18ed02ceb9edd'
