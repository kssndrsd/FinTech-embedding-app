from flask import Flask, render_template
from datetime import datetime, date, timedelta
import os
from dotenv import load_dotenv

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
    companies = supabase.table('companies').select("name", "size", "industry").execute()
    return render_template("companies-data.html", title="Companies", companies=companies.get('data'))

@app.context_processor
def inject_current_datetime():
    return dict(current_datetime=datetime.utcnow())
