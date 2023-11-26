import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd
from openai import OpenAI

load_dotenv()

url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(url, key)

opeani_key = url = os.environ.get('OPENAI_KEY')
client = OpenAI(api_key=opeani_key)

# Get the text to concat:

response = supabase.table('raw_companies_database').select("name", "size", "industry", "id", "description").execute()
extracted_data = response.data

def transform_dict(single_dict):
    company_id = single_dict['id']
    concatted_values = " ".join([str(value) for key, value in single_dict.items() if key != 'id'])
    return {'id': company_id, 'concatted_for_embedding': concatted_values}

# Transform each dictionary in the list
transformed_data = [transform_dict(d) for d in extracted_data]

for element in transformed_data:
    inputed_text = element["concatted_for_embedding"]

    response = client.embeddings.create(
        input=inputed_text,
        model="text-embedding-ada-002"
    )

    embeding = response.data[0].embedding
    # print(embeding)

    company_id = element["id"]
    input_text = element["concatted_for_embedding"]
    embeding_to = embeding

    response = supabase.table('embedings').insert({
        "company_id": company_id,
        "content": str(inputed_text),
        "embedding": embeding_to
    }).execute()