import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def getSelectors(html):



    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                        You are an expert web scraper. I am providing you with the raw HTML of a webpage. 
                        Analyze the HTML and return a JSON response ONLY with these fields:
                        {{
                        "suitable": boolean,
                        "article": "css_selector",
                        "link": "css_selector",
                        "id": "css_selector"
                        }}

                        Rules:
                        1. "suitable": true if the site has a list of items/articles that increment over time.
                        2. "article": The CSS selector targeting the repeating main container of the item, but be intelligent about it you should see a minimal pattern.
                        3. "link": The CSS selector (relative to the article container) targeting the <a> tag for the item's main URL, give me the exact path from the article to the relevant <a>.
                        4. the selectors must be .class or tag.class , prefrably .class when possible.
                        5. Return ONLY valid JSON. Do not invent classes; only use what is in the provided HTML.

                        HTML to analyze:
                        {html} 
                    """
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content