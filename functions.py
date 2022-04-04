def shorter_text(article: str):
    if len(article) > 197:
        final_article = ' '.join(article[0:198].split(' ')[:-1]) + '...'
        return final_article
    else:
        return article


def news_articles_creator(article_description, article_name):
    all_states = [] # все штаты)))
    for name in article_description.keys():
        state_name = name
        message = article_description[state]
        link_to_news = article_name[state]
        state = f'<p><a href="{link_to_news}"><b>{state_name}</b></a><br>{shorter_text(message)}</p>'
        all_states.append(state)
    return all_states
