from flask import Flask, render_template, request, redirect, url_for, flash, Response
from datetime import datetime, date, timedelta
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd


load_dotenv()

from supabase import create_client, Client

key = os.environ.get('SUPABASE_KEY')
url = os.environ.get('SUPABASE_URL')
supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello")

@app.route("/companies-data")
def companies_data():
    response = supabase.table('raw_companies_database').select("name", "size", "industry", "website").execute()

    # Access the data from the response
    companies_data = response.data

    # Check if companies_data is not empty or None
    if not companies_data:
        print("No data found.")
        return "No data found."

    # Pass the data to the template
    return render_template("companies-data.html", title="Companies", companies=companies_data)

@app.context_processor
def inject_current_datetime():
    return dict(current_datetime=datetime.utcnow())
