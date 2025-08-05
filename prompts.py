# system and user prompt 

def system_prompt():
    return "You are an assistant that summarizes the content of a webpage into markdown. Ignore navigation text."

def user_prompt(website):
    return f"""You are looking at a website titled "{website.title}".

The contents of this website are as follows. Please summarize it in markdown:

{website.text[:4000]}
"""