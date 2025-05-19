try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("Error: Please install beautifulsoup4. If using an externally managed environment, try:")
    print("1. Create a virtual environment: python3 -m venv venv")
    print("2. Activate it: source venv/bin/activate")
    print("3. Install: pip install beautifulsoup4")
    print("Or use: sudo apt install python3-bs4")
    exit(1)

def scrape_titles(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        titles = [h2.get_text().strip() for h2 in soup.find_all("h2")]
        return titles
    except Exception as e:
        return f"Error parsing HTML: {str(e)}"

# Test the function (simulated HTML)
html_content = """
<html>
<body>
<h2>Title 1</h2>
<p>Some text</p>
<h2>Title 2</h2>
</body>
</html>
"""
print(scrape_titles(html_content))