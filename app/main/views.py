from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_all_news, get_source_news_al, get_source_news_wp,get_source_news_ap, get_source_news_nn
from ..models import Article


@main.route('/')
@main.route('/home')
def home():
    news = get_all_news()
    return render_template('index.html', news=news)


@main.route('/aj-jazeera-english')
def ajazeer():
    news = get_source_news_al()
    return render_template('index.html', news=news)


@main.route('/the-wahington-post')
def wp():
    news = get_source_news_wp()
    return render_template('index.html', news=news)

@main.route('/associated-press')
def ap():
    news = get_source_news_ap()
    return render_template('index.html', news=news)


@main.route('/news.com.au')
def nn():
    news = get_source_news_nn()
    return render_template('index.html', news=news)