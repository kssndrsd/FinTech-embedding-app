#Overview#

This Flask application serves as an interface for searching and comparing company data using text embeddings. It leverages OpenAI's embeddings and a Supabase client for data storage and retrieval. The application allows users to search for companies by text input and find similar companies based on text embeddings.

Features

Company Search: Users can search for companies by entering text, and the application retrieves similar companies using OpenAI's text embeddings.
Data Visualization: Displays company data including name, size, industry, website, and description.
API Endpoints: Provides endpoints for retrieving similar company IDs and detailed company data.


##Features & Code Snippets##

---

Company Search
Users can input text to search for similar companies based on text embeddings provided by OpenAI.

```python
Copy code
@app.route('/search_companies', methods=['GET', 'POST'])
def search_companies():
    if request.method == 'POST':
        # ...
        response = client.embeddings.create(
            input=inputed_text,
            model="text-embedding-ada-002"
        )
        # ...
```
This route handles the POST request for searching companies. It uses OpenAI's client to generate text embeddings from the user input.

---

Similarity Calculation
The application calculates the similarity between user input and stored company embeddings.

```python
Copy code
def calculate_similarity(embedding, embeddings_list):
    similarities = cosine_similarity(embedding, embeddings_list)
    return similarities[0]
```
This function uses cosine similarity from scikit-learn to compute similarity scores between the input embedding and stored embeddings.

---

Embedding Conversion
Converts string embeddings stored in the database into numpy arrays.

```python
Copy code
def convert_embedding(str_embedding):
    return np.fromstring(str_embedding.strip("[]"), sep=',', dtype=float)
```
This utility function converts a string representation of an embedding from the database into a numpy array.

---

API Endpoint for Similar Companies
Provides an API endpoint to retrieve IDs of similar companies based on text input.

```python
Copy code
@app.route('/get_similar_ids', methods=['GET'])
def get_similar_ids():
    # ...
    return jsonify(top_ids)
```
This endpoint uses OpenAI's embeddings and stored data to find and return the top similar company IDs.

---

Displaying Company Data
Renders company data including details like name, size, industry, etc.

```python
Copy code
@app.route("/companies-data")
def companies_data():
    # ...
    return render_template("companies-data.html", companies=companies_data)
```
This route fetches company data from Supabase and displays it on a dedicated page.

---

Environment Variables
The application uses environment variables for API keys and database URLs.

```python
Copy code
load_dotenv()
key = os.environ.get('SUPABASE_KEY')
url = os.environ.get('SUPABASE_URL')
supabase: Client = create_client(url, key)
```
It loads environment variables for the Supabase client using dotenv.

---

Usage and Licensing

This repository contains code developed for portfolio demonstration purposes. While the source code is available publicly for viewing and reference, the following restrictions apply:

No Unauthorized Use: The code in this repository is not intended for free use, copying, distribution, or incorporation into other projects or tools without explicit written permission from the authors.
Portfolio Display Only: The primary purpose of making this code public is for display in the author's professional portfolio. It serves to showcase the skills and coding style of the authors.
Contact for Permissions: If you are interested in using any part of this code, please contact the authors directly to discuss potential use cases and obtain permission.
We encourage open-source collaboration and sharing of knowledge but also value the protection of intellectual property and creative rights.

---