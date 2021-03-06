from datetime import datetime

def format_date(date):
  return date.strftime('%d/%m/%y')

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))