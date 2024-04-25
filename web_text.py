import requests
import re

def extract_text_from_webpage(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Remove style tags and their content
        html_content = re.sub(r'<style[^>]*>.*?</style>', '', response.text, flags=re.DOTALL)

        # Remove all HTML tags
        text = re.sub(r'<[^<]+?>', ' ', html_content)

        # Remove extra spaces and newline characters
        text = re.sub(r'\s+', ' ', text).strip()

        return text
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return None
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
url = "https://www.infosys.com/"
webpage_text = extract_text_from_webpage(url)
if webpage_text:
    print(webpage_text)
