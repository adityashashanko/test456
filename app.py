import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("🔎 Top 5 Blogs Finder")

query = st.text_input("Enter topic:")

def get_top_blogs(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f"https://www.google.com/search?q={query}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for g in soup.select('div.yuRUbf > a'):
        link = g.get('href')
        if link:
            links.append(link)
        if len(links) == 5:
            break

    return links

if st.button("Search Blogs"):
    if query:
        results = get_top_blogs(query)

        st.markdown("### 📌 Top 5 Blog Links")
        for i, link in enumerate(results, start=1):
            st.write(f"{i}. {link}")
    else:
        st.warning("Please enter a topic")
