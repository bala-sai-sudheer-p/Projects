from flask import Flask, render_template, request
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Movies with poster URLs you provided
movies = {
    "RRR": {
        "image": "https://m.media-amazon.com/images/I/61XUSNN2vrL._SL1200_.jpg",
        "cast": "NTR Jr, Ram Charan, Alia Bhatt",
        "hours": "3h 7m",
        "price": 250,
        "location": "Hyderabad",
        "theatre": "PVR Cinemas"
    },
    "Animal": {
        "image": "https://wallpapercave.com/wp/wp13286327.jpg",
        "cast": "Ranbir Kapoor, Rashmika Mandanna",
        "hours": "3h 21m",
        "price": 300,
        "location": "Bangalore",
        "theatre": "INOX"
    },
    "Salaar": {
        "image": "https://scontent.fvga5-1.fna.fbcdn.net/v/t39.30808-6/480518543_1167473244734990_4274049636494953563_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=KaGEwM3iGpwQ7kNvwFYbHgF&_nc_oc=AdmTaWbvABq3Ziz7LUcUCsZr5Zb5yeVdLtzpddK8ftrhDGoLAxWq9XLQU2c-ttyabi0&_nc_zt=23&_nc_ht=scontent.fvga5-1.fna&_nc_gid=7E-RHbXdHsAh05eMGs6lwQ&oh=00_Afogz2NlWpgdBHp2sKKRagBePHj9JHbru6jukbYFm45-qw&oe=69744EBC",
        "cast": "Prabhas, Prithviraj Sukumaran, Shruti Haasan",
        "hours": "2h 55m",
        "price": 280,
        "location": "Chennai",
        "theatre": "Cinepolis"
    }
}

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/book", methods=["POST"])
def book():
    try:
        movie_name = request.form.get("movie")
        tickets = request.form.get("tickets")

        if not movie_name or not tickets:
            return "Form data missing!", 400
        if movie_name not in movies:
            return "Movie not found!", 404

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return render_template(
            "book.html",
            movie=movie_name,
            tickets=tickets,
            time=time,
            movies=movies
        )
    except Exception as e:
        app.logger.error(f"Error booking movie: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

