from flask import Flask, render_template, request, redirect

from src.models.rental_repository import (
    create_listing,
    get_all_listings
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


if __name__ == "__main__":
    app.run(debug=True)