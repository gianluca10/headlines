import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

NEWS_FEEDS = {#'ARABNEWS' : 'http://www.arabnews.com/cat/1/rss.xml',
              'BBC' : 'http://feeds.bbci.co.uk/news/rss.xml',
              'CNN': 'http://rss.cnn.com/rss/edition.rss',
              'FOX': 'http://feeds.foxnews.com/foxnews/latest',
              #'REPUBBLICA': 'http://www.repubblica.it/rss/homepage/rss2.0.xml'
              }


@app.route('/', methods=['GET', 'POST'])
@app.route('/<publication>')
def get_news():
    query = request.form.get('publication')
    articles = []
    for pub in NEWS_FEEDS:
        if query and pub != query:
            continue
        print(pub)
        feed = feedparser.parse(NEWS_FEEDS[pub])
        first_article = feed['entries'][0]
        articles.append(first_article)
    return render_template('home.html', articles=articles)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
