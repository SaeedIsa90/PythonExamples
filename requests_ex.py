import requests

# Get method
requests.get('https://api.github.com')

# Response
response = requests.get('https://api.github.com')
print(response)

# check all API from response
print(dir(response))

# status code
print(response.status_code)

print(response.content)

print(response.json())

print(response.headers)

# Page NOT found example
r = requests.get('https://api.github.com/saeed')
print(r.status_code)

# Search GitHub's repositories for requests demonstrates params usage
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+
print(response.json()['items'][0])


# Post method
# data can be dictionary, list of tuples, file-obj alike,...
res = requests.post('https://httpbin.org/post', data={'key':'value'})
print(res.json())


res = requests.post('https://httpbin.org/post', json={'key':'value'})
print(res.json())