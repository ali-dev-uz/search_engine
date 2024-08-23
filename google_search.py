import requests

# Replace these with your correct API key and CX
API_KEY = 'AIzaSyB-spA38yNNBo2nx_IrfxQIhDgMbRKC-gM'
CX = '41a40491a64aa4b72'  # Just the ID part

def google_search(query, num_pages=1):

    for page in range(num_pages):
        start = page * 10 + 1  # Calculating the start index for each page
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}&start={start}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for item in data.get('items', []):
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print(f"Snippet: {item['snippet']}")
                print("-" * 60)
            print(len(data.get('items', [])))

        else:
            print("Error:", response.status_code, response.text)
            break  # Stop further requests if an error occurs

# Example Usage: Fetch 3 pages of results
google_search("Artel company", num_pages=10)
