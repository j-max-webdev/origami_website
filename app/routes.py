from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Max"}
    folds = [
        {
            "designer": "Jason Schneider",
            "design": "Toad",
            "paper_type": "Kami",
            "paper_size": "6x6",
            "date_folded": "3/23/24"
        },
        {
            "designer": "Akira Yoshizawa",
            "design": "Pinwheel",
            "paper_type": "Kami",
            "paper_size": "6x6",
            "date_folded": "3/22/24"
        }
    ]
    return render_template(
        "index.html",
        title="Keep Folding!",
        user=user,
        folds=folds
    )
