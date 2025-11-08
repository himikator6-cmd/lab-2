import json
import re


def read_jsonl_news_text(filename, category = 'all'):
    results = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        if (category == 'all'):
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                data = json.loads(line)
                results.append(data['text'])
        else:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                data = json.loads(line)
                if (data['category'] == category):
                    results.append(data['text'])                  
    return results


def news_to_text_converter(news):
    text = ' '.join(news)
    return text


def text_extractor(filename, category = 'all'):
    news = read_jsonl_news_text(filename, category)
    text = news_to_text_converter(news)
    return text


def clean_html(html_text):
    cleaned_text = re.sub(r'<[^>]+>', '', html_text)
    cleaned_text = re.sub(r'&[^;]+;', '', cleaned_text)
    return cleaned_text


def text_lower(text):
    lower_text = text.lower()
    return lower_text


def clean_space(space_text):
    cleaned_text = re.sub(r'\s+', ' ', space_text).strip()
    return cleaned_text


def cleaner(text):
    text1 = clean_html(text)
    text2 = text_lower(text1)
    text3 = clean_space(text2)
    return text3


