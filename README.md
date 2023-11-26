# Overview

This Python Flask application serves as an interface for searching and comparing company data using text embeddings. It leverages OpenAI's embeddings and a Supabase client for data storage and retrieval. The application allows users to search for companies by text input and find similar companies based on text embeddings.

## Features

Company Search: Users can search for companies by entering text, and the application retrieves similar companies using OpenAI's text embeddings (vector search).
Data Visualization: Displays company data including name, size, industry, website, and description.
API Endpoints: Provides endpoints for retrieving similar company IDs and detailed company data.


## Features & Code Snippets

### Technologies Used

`python`, `flask`, `Bootstrap 5`, `OpenAI`, `Supabase`, 

---

This is how to load the clients for supabase and openai with python

```python
from openai import OpenAI
from supabase import create_client, Client

load_dotenv()

key = os.environ.get('SUPABASE_KEY')
url = os.environ.get('SUPABASE_URL')
supabase: Client = create_client(url, key)

opeani_key = url = os.environ.get('OPENAI_KEY')
client = OpenAI(api_key=opeani_key)
```

---

Usage and Licensing

This repository contains code developed for portfolio demonstration purposes. While the source code is available publicly for viewing and reference, the following restrictions apply:

No Unauthorized Use: The code in this repository is not intended for free use, copying, distribution, or incorporation into other projects or tools without explicit written permission from the authors.
Portfolio Display Only: The primary purpose of making this code public is for display in the author's professional portfolio. It serves to showcase the skills and coding style of the authors.
Contact for Permissions: If you are interested in using any part of this code, please contact the authors directly to discuss potential use cases and obtain permission.

---