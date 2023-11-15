import requests

def check_web_response(url):
    try:
        response = requests.get(url, timeout=5)  # 5-second timeout
        return response.elapsed.total_seconds()  # Response time in seconds
    except requests.RequestException:
        return None

# Example usage
url = 'http://yourwebsite.com'
response_time = check_web_response(url)
if response_time is not None:
    print(f"Response time for {url} is {response_time} seconds.")
else:
    print(f"Failed to get a response from {url}")
