from imports import *

sport_url = 'https://beta.matchtv.ru/news'
sport_ans = requests.get(sport_url)
sport_soup = BeautifulSoup(sport_ans.text, 'html.parser')


def get_sport_news():
    news_massive = sport_soup.find('div', class_='articles-table').findAll('div', class_="articles-table__cell-content")
    article_name_dictionary_sport = {}

    # формирование словаря с артиклями и ссылками на статью
    for page in news_massive:
        article = page.find('div', class_="articles-table__title").find('a',
                                                                        class_='link-wrapper__link articles-table__link').find(
            'div', class_='articles-table__title-text').text
        link_to_new = 'https://beta.matchtv.ru' + page.find('div', class_="articles-table__title").find('a',
                                                                                                        class_='link-wrapper__link articles-table__link').get(
            'href')
        article_name_dictionary_sport[article] = link_to_new

    article_description_dict_sport = {}

    for key in article_name_dictionary_sport.keys():
        try:
            article_page = BeautifulSoup(requests.get(article_name_dictionary_sport[key]).text, 'lxml')
            first_sentence_finder = article_page.find('div',
                                                      class_='video-page__body feed-body video-page__body--without-authors feed-body--centered-images').find(
                'p').text.replace('\xa0', ' ')
            article_description_dict_sport[key] = first_sentence_finder
        except Exception:
            pass

    for_db_sport = []
    for key in article_description_dict_sport.keys():
        for_db_sport.append(key, article_description_dict_sport[key], article_name_dictionary_sport[key])

    return for_db_sport


print(get_sport_news())
connection = sqlite3.connect('news.db')
cursor = connection.cursor()
# cursor.executemany('INSERT INTO q1_person_name(first_name, last_name) VALUES (?,?)', data_person_name)
