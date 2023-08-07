from flask import Flask, render_template, request
from arbitrage import get_upcoming_events, get_arbitrage_events, create_table
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def arbitrage():
    if request.method == "POST":
        upcoming = get_upcoming_events()
        arbs = get_arbitrage_events(upcoming)
        df = create_table(arbs)
        print(f"Found {len(df)} arbs")
    else:
        df = pd.DataFrame()

    return render_template("arbitrage.html", table=df)

@app.route("/ml")
def ml():
    
    return render_template("ml.html")

if __name__ == "__main__":
    app.run(debug=True)