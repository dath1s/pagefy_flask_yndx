from imports import *
from functions import *
from parsers.cinema_parser import *
from parsers.politics_parser import *
from parsers.medicine_parser import *
from parsers.sport_parser import *

app = Flask(__name__)
# run_with_ngrok(app)

# articles
# article_description_dict_cinema = get_cinema_news()
# article_description_dict_medicine = get_medicine_news()
# article_description_dict_politics = get_politics_news()
# article_description_dict_sport, article_name_dict_sport = get_sport_news()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Pagefy',
                           sport=''.join(news_articles_creator(article_description_dict_sport, article_name_dict_sport)))


if __name__ == '__main__':
    app.run()
