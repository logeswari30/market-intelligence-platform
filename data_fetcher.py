import requests

API_KEY = "82b748b717ae4d30b7a39c1865da4d62"

def fetch_data(sector):
    url = f"https://newsapi.org/v2/everything?q={sector}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            return "Error fetching data from News API"
        
        data = response.json()
        articles = data.get("articles", [])
        
        if not articles:
            return "No recent news found for this sector."
        
        result = ""
        for article in articles[:5]:   # Top 5 news
            title = article.get("title", "")
            description = article.get("description", "")
            
            result += f"- {title}\n  {description}\n\n"
        
        return result
    
    except Exception as e:
        return f"Error: {str(e)}"