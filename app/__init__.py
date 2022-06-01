import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           title="MLH Fellow",
                           url=os.getenv("URL"))


# Test route to see if my template is rendering as expected
@app.route("/template")
def template():

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
        title="Super Fellow!",
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
                "name":
                "League of Legends",
                "img":
                "https://cdn1.epicgames.com/salesEvent/salesEvent/EGS_LeagueofLegends_RiotGames_S1_2560x1440-ee500721c06da3ec1e5535a88588c77f"
            },
            {
                "name":
                "Valorant",
                "img":
                "https://cdn.dribbble.com/users/2348/screenshots/10696082/media/4a24583ea649f9df1415775a37c84ae5.png?compress=1&resize=1200x900&vertical=top"
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
        }])
