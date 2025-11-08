import requests
import bs4
import json
import time
import re
import urllib
import datetime


def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }   
    try:
        response = requests.get(url, headers = headers, timeout = 10)
        response.raise_for_status()
        return bs4.BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы {url}: {e}")
        return None


def extract_article_data(article_url):
    category_from_url = ''
    if '?category=' in article_url:
        clean_url, params = article_url.split('?', 1)
        param_match = re.search(r'category=([^&]+)', params)
        if param_match:
            category_from_url = param_match.group(1)
        article_url = clean_url    
    soup = get_soup(article_url)
    if not soup:
        return None    
    article_data = {
        'title': '',
        'text': '',
        'publication_date': '',
        'url': article_url,
        'category': category_from_url
    }    
    try:
        title_elem = soup.find('h1', class_ = re.compile(r'topic-title|topic-header__title'))
        if not title_elem:
            title_elem = soup.find('h1')
        if title_elem:
            article_data['title'] = title_elem.get_text().strip()
        date_elem = None
        time_selectors = [
            'time[datetime]',
            '.topic-header__time',
            '.b-topic__info time',
            '.topic-info__time',
            '.news-header__date',
            '[class*="time"]',
            '[class*="date"]'
        ]        
        for selector in time_selectors:
            date_elem = soup.select_one(selector)
            if date_elem:
                break
        if not date_elem:
            date_elem = soup.find('time')
        if date_elem:
            datetime_attr = date_elem.get('datetime', '').strip()
            if datetime_attr:
                article_data['publication_date'] = datetime_attr
            else:
                date_text = date_elem.get_text().strip()
                if date_text:
                    article_data['publication_date'] = date_text
        if not article_data['publication_date']:
            date_match = re.search(r'/news/(\d{4})/(\d{2})/(\d{2})/', article_url)
            if date_match:
                year, month, day = date_match.groups()
                article_data['publication_date'] = f"{year}-{month}-{day}"
        if not article_data['publication_date']:
            meta_date = soup.find('meta', property='article:published_time')
            if meta_date:
                article_data['publication_date'] = meta_date.get('content', '').strip()
        category_elem = None
        breadcrumbs = soup.select('.breadcrumbs__item, .b-breadcrumbs__item, [class*="breadcrumb"]')
        if breadcrumbs and len(breadcrumbs) > 1:
            for i in range(1, len(breadcrumbs)-1):
                text = breadcrumbs[i].get_text().strip().lower()
                if text and text not in ['главная', 'лента', 'lenta.ru']:
                    category_elem = breadcrumbs[i]
                    break        
        if not category_elem:
            category_selectors = [
                '.topic-header__rubric',
                '.rubric-label',
                '[class*="rubric"]',
                '.b-topic__rubric'
            ]
            for selector in category_selectors:
                category_elem = soup.select_one(selector)
                if category_elem:
                    break        
        if category_elem:
            category_text = category_elem.get_text().strip()
            if (category_text and 
                len(category_text) > 1 and 
                category_text.lower() not in ['все', 'главная', 'новости']):
                article_data['category'] = category_text
        text_parts = []        
        content_selectors = [
            '.topic-body__content-text',
            '.topic-body__content',
            'div[class*="content"]',
            'div[class*="text"]', 
            'article',
            '.b-topic__content'
        ]        
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                for unwanted in content_elem.select('.ad, .banner, .social, .links, .tags, .read-more'):
                    unwanted.decompose()                
                paragraphs = content_elem.find_all('p')
                for p in paragraphs:
                    text = p.get_text().strip()
                    if (len(text) > 20 and 
                        not re.search(r'читайте также|реклама|подпишись', text.lower())):
                        text_parts.append(text)
                if text_parts:
                    break        
        article_data['text'] = ' '.join(text_parts)        
        if len(article_data['text']) < 100:
            return None            
        return article_data    
    except Exception as e:
        print(f"Ошибка при парсинге статьи {article_url}: {e}")
        return None


def get_article_links_from_page(page_url):
    soup = get_soup(page_url)
    if not soup:
        return []    
    article_links = []
    base_category = ''
    if '/rubrics/' in page_url:
        category_match = re.search(r'/rubrics/([^/]+)', page_url)
        if category_match:
            base_category = category_match.group(1)
    link_selectors = [
        'a[href*="/news/"]',
        'a[href*="/article/"]',
        '.item .title a',
        '.news .title a',
        '.b-text a',
        '.card-full-news a',
        '.topnews a'
    ]   
    for selector in link_selectors:
        links = soup.select(selector)
        for link in links:
            href = link.get('href')
            if href and ('/news/' in href or '/article/' in href):
                full_url = urllib.parse.urljoin(page_url, href)
                if re.search(r'/news/\d{4}/\d{2}/\d{2}/', full_url) or '/article/' in full_url:
                    if base_category and '?' not in full_url:
                        full_url += f'?category={base_category}'
                    article_links.append(full_url)    
    return list(set(article_links))


def collect_articles(base_urls, target_word_count):
    all_articles = []
    total_words = 0
    processed_urls = set()    
    for base_url in base_urls:
        print(f"Обрабатывается страница: {base_url}")
        article_links = get_article_links_from_page(base_url)        
        for article_url in article_links:
            if article_url in processed_urls:
                continue                
            print(f"Парсинг статьи: {article_url}")            
            article_data = extract_article_data(article_url)            
            if article_data and article_data['text']:
                word_count = len(article_data['text'].split())                
                all_articles.append(article_data)
                processed_urls.add(article_url)
                total_words += word_count
                date_info = article_data['publication_date'] if article_data['publication_date'] else "НЕТ ДАТЫ"
                print(f"Статья добавлена. Слов: {word_count}. Дата: {date_info}. Всего слов: {total_words}")                
                if total_words >= target_word_count:
                    print(f"Достигнуто целевое количество слов: {total_words}")
                    return all_articles            
            time.sleep(1)    
    print(f"Собрано {len(all_articles)} статей, всего слов: {total_words}")
    return all_articles


def save_to_jsonl(articles, filename):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for article in articles:
            json_line = json.dumps(article, ensure_ascii = False)
            f.write(json_line + '\n')


def parser(filepath, words):
    base_url = [
        #'https://lenta.ru/',
        #'https://lenta.ru/rubrics/ussr/',
        #'https://lenta.ru/rubrics/life/',
        #'https://lenta.ru/rubrics/forces/',
        #'https://lenta.ru/rubrics/culture/',
        #'https://lenta.ru/rubrics/russia/',
        #'https://lenta.ru/rubrics/media/',
        #'https://lenta.ru/rubrics/sport/',
        #'https://lenta.ru/rubrics/travel/',
        #'https://lentaru/rubrics/science/',
        #'https://lenta.ru/rubrics/economics/'
    ]   
    print("Начало сбора статей с Lenta.ru...")
    articles = collect_articles(base_url, target_word_count = words)
    output_filename = filepath
    save_to_jsonl(articles, output_filename)
    total_words = sum(len(article['text'].split()) for article in articles)
    print(f"\n=== РЕЗУЛЬТАТ ===")
    print(f"Собрано статей: {len(articles)}")
    print(f"Общее количество слов: {total_words}")
    print(f"Файл сохранен: {output_filename}")
    if articles:
        print(f"\nПример первой статьи:")
        first_article = articles[0]
        for key, value in first_article.items():
            if key == 'text':
                preview = value[:100] + "..." if len(value) > 100 else value
                print(f"{key}: {preview}")
            else:
                print(f"{key}: {value}")

