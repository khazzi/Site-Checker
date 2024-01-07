import requests

def check_site_connectivity(url):
    try:
        response = requests.get(url)
        # Check if the response status code is in the success range (200-299)
        if response.status_code // 100 == 2:
            return True, f"Site is reachable. Status Code: {response.status_code}"
        else:
            return False, f"Site is reachable, but returned an unexpected status code: {response.status_code}"
    except requests.ConnectionError:
        return False, "Failed to connect to the site."

# Example usage:
site_url = "https://www.example.com"
is_connected, message = check_site_connectivity(site_url)

print(message)
