from flask import Blueprint, render_template, request

teams = Blueprint("teams", __name__)

WORLD_CUP_TEAMS = [
    {"name": "Argentina", "group": "A"},
    {"name": "France", "group": "B"},
    {"name": "England", "group": "C"},
    {"name": "Spain", "group": "D"},
    {"name": "Canada", "group": "A"},
    {"name": "Portugal", "group": "B"},
]

@teams.route("/teams")
def team_list():
    return render_template("teams.html", teams=WORLD_CUP_TEAMS)

@teams.route("/team")
def team_detail():
    # ex: /team?name=England
    team_name = request.args.get("name", "Unknown Team")
    return render_template("team.html", team_name= team_name)


@teams.route("/search")
def search():
    group = request.args.get("group", "")
    # filtered = [team for team in WORLD_CUP_TEAMS if team["group"] == group] if group else WORLD_CUP_TEAMS

    if group: # is group empty/null or not !
        filtered = [] # initialize the filtered list

        for team in WORLD_CUP_TEAMS: # go through each element
            if team["group"] == group: # if the criteria matches
                filtered.append(team) # then, add it to the list
    else: # if no query
        filtered = WORLD_CUP_TEAMS # use the whole list


    return render_template("search.html", teams= filtered, group= group)

