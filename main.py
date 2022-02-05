import flask

app = flask.Flask (__name__)


Tv_shows = ["Ghost Adventures", "See No Evil", "Sister, Sister", "Sailor Moon", "Paranormal Witness", "Man Vs. Food", "Disappeared", "Married at First Sight", "Four Weddings", "What Not to Wear"]

Pictures = ["/static/ghost-adventures.jpeg", "/static/seeNoEvil.jpg", "/static/SisterSister.jpg", "/static/sailorMoon.jpeg", "/static/ParanormalWit.jpg", "/static/ManVsFood.jpeg", "/static/disappeared.jpeg", "/static/MarriedAt1stSight.jpeg", "/static/4Weddings.jpg", "/static/whatnottowear.jpeg"]

@app.route("/")
def index():
    return flask.render_template("index.html", len = len(Tv_shows), Tv_shows = Tv_shows, Pictures = Pictures)


if (__name__) == "__main__":
    app.run(use_reloader = True, debug=True)
