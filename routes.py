from flask import Blueprint, render_template, request, redirect, flash
from .scraper import fetch_case_data
from .database import save_query

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    case_data = None
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        filing_year = request.form["filing_year"]

        try:
            case_data, raw_html = fetch_case_data(case_type, case_number, filing_year)
            save_query(case_type, case_number, filing_year, raw_html)
        except Exception as e:
            flash(f"Error: {str(e)}")

    return render_template("index.html", data=case_data)