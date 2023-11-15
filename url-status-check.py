import requests

def check_url(url):
    try:
        response = requests.get(url, timeout=5)  # Adjust timeout as needed
        return response.status_code
    except requests.RequestException as e:
        return str(e)

def main(urls):
    for url in urls:
        status = check_url(url)
        print(f"URL: {url}, Status: {status}")

# List of URLs to check
urls_to_check = [
    'http://example.com',
    'http://nonexistentwebsite.com',
    # Add more URLs here
]

main(urls_to_check)
