import serpapi
from config import config


def get_supervisor(prof_name, university, N=5):
    keywords = prof_name + " " + university
    params = {
        "engine": "google_scholar",
        "q": keywords,
        "api_key": config.SERP_API_KEY,
        "hl": "en",
    }

    search = serpapi.search(params)
    results = search["organic_results"][:N]
    if len(results) == 0:
        return None
    
    combined_results = ""
    for result in results:
        title = result.get('title', 'No title')
        snippet = result.get('snippet', 'No snippet')
        publication_info = result.get('publication_info', {}).get('summary', 'No publication info')
        combined_results += f"Title: {title}\nSnippet: {snippet}\nPublication Summary: {publication_info}\n\n"

    return combined_results
