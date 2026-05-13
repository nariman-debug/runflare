import requests


sites = {
    'python': 'https://python.org',
    'pornhub': 'https://pornhub.com',
    'youtube': 'https://youtube.com',
    'files': 'https://files.ir',
    'uplod': 'https://uplod.ir',
    'django-rest-framework': 'https://www.django-rest-framework.org/',
}

for site, url in sites.items():
    try:
        resp = requests.get(url, timeout=10)
        print('⇓' * 30)
        print(f'{site}: {resp.url}')
        print(f'status: {resp.status_code}')
        print('⇑' * 30, '\n')
    except requests.exceptions.RequestException as e:
        print('⇓' * 30)
        print(f'{site}: {url}')
        print(f'status: Error: {e}')
        print('⇑' * 30, '\n')
