import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():

    # **Shape of Data**
    #
    # experiences = [{
    #    "name": string,
    #    "role": string,
    #    "date": string
    # }, ...]
    #
    # hobbies = [{
    #    "name": string,
    #    "img": string
    # }, ...]
    #
    # education = [{
    #    "name": string,
    #    "location": string
    # }, ...]

    return render_template(
        "main.jinja",
        title="Bobo the Baboon",
        url=os.getenv("URL"),
        experiences=[
            {
                "name": "Meta",
                "role": "Production Engineer",
                "date": "XX 2021 - XX 2022"
            },
            {
                "name": "Google",
                "role": "Software Engineer",
                "date": "XX 2020 - XX 2021"
            },
            {
                "name": "Amazon",
                "role": "Systems Development Engineer",
                "date": "XX 2019 - XX 2020"
            },
        ],
        hobbies=[
            {
                "name": "Gaming",
                "img": "./img/game.jpg"
            },
            {
                "name": "Working Out",
                "img": "./img/gym.jpg"
            },
        ],
        educations=[{
            "name": "Yale University",
            "location": "New Haven, CT"
        }, {
            "name": "Harvard University",
            "location": "Cambridge, MA"
        }, {
            "name": "Stanford University",
            "location": "Stanford, CA"
        }],
    )
