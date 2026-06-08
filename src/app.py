from flask import Flask, render_template, request, redirect

from src.models.rental_repository import (
    create_listing,
    get_all_listings
)

from src.models.dashboard_repository import (
    get_dashboard_stats
)

from src.models.dashboard_repository import (
    get_dashboard_stats,
    get_city_analysis
)

from src.models.dashboard_repository import (
    get_dashboard_stats,
    get_city_analysis,
    get_best_deals
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_listing", methods=["POST"])
def add_listing():

    create_listing(
        request.form["address"],
        request.form["city"],
        request.form["state"],
        request.form["zip_code"],
        request.form["price"]
    )

    return redirect("/listings")


@app.route("/listings")
def listings():

    listings = get_all_listings()

    return render_template(
        "listings.html",
        listings=listings
    )

@app.route("/dashboard")
def dashboard():

    stats = get_dashboard_stats()

    return render_template(
        "dashboard.html",
        stats=stats
    )

@app.route("/analysis")
def analysis():

    analysis_data = get_city_analysis()

    return render_template(
        "analysis.html",
        analysis_data=analysis_data
    )

@app.route("/deals")
def deals():

    deals_data = get_best_deals()

    return render_template(
        "deals.html",
        deals_data=deals_data
    )


if __name__ == "__main__":
    app.run(debug=True)