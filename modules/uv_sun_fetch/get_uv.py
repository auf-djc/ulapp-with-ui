import requests

def get_uv_index(api_key, city):
    try:
        base_url = "http://api.weatherapi.com/v1/current.json"
        params = {
            'key': api_key,
            'q': city,
        }
        
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Print the entire response content for debugging
        print(f"Response content: {data}")

        if 'current' in data and 'uv' in data['current']:
            uv_index = data['current']['uv']
        else:
            uv_index = "N/A"

        return {
            'uv_index': uv_index
        }
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        print(f"Response content: {response.content}")
        return {
            'uv_index': "N/A"
        }
    except Exception as e:
        print(f"Error fetching UV Index: {e}")
        return {
            'uv_index': "N/A"
        }
