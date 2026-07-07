from flask import Blueprint, render_template, request

teams = Blueprint("teams", __name__)

WORLD_CUP_TEAMS = [
    {"name": "Argentina", "group": "A"},
    {"name": "France", "group": "B"},
    {"name": "England", "group": "C"},
    {"name": "Spain", "group": "D"}
]

@teams.route("/teams")
def team_list():
    return render_template("teams.html", teams=WORLD_CUP_TEAMS)

@teams.route("/team")
def team_detail():
    # ex: /team?name=England
    team_name = request.args.get("name", "Unknown Team")
    return render_template("team.html", team_name= team_name)