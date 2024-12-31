from flask import Flask

import PetoiRobot

app = Flask(__name__)

PetoiRobot.autoConnect()
PetoiRobot.sendSkillStr("kup",3)


@app.route("/jump")
def jump():
    print("Jump!")
    PetoiRobot.sendSkillStr("kbf")
    return "<b>Jumped!</b>"