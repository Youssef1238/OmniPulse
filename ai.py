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
                    [SYSTEM: STRICT DETERMINISTIC MODE]
                    You are a specialized HTML-to-JSON parser. Your output must be 100% valid JSON for python json.loads().

                    [OBJECTIVE]
                    Find the repeating article list and return the CSS selectors.

                    [CRITICAL INSTRUCTION]
                    The link should be a css selector that has the right href attribute.
                    The title should be a css selector that represents the title and has no child tag , only a text.
                    if the title selector has a child , then provide the seletor to the child instead.
                    if that child has a child , provide the selector for the deepest child.

                    [JSON SCHEMA]
                    {{
                    "suitable": boolean,
                    "article": "css_selector_for_container",
                    "title": "css_selector_for_the_exact_tag_containing_text",
                    "link": "css_selector_for_the_exact_a_tag"
                    }}

                    [CONSTRAINTS]
                    - NO markdown code blocks (no ```json). 
                    - Start with '{{' and end with '}}'.
                    - Use '.class' notation.
                    

                    [HTML]
                    {html}
                    """
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content