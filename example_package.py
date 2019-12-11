import requests

url = 'http://www.bbc.co.uk/news'

response = requests.get(url)

## Shows if it recognises the link
print(response.status_code)

#prints the code of the content in the page
print(response.content)

