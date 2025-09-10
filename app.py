from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    return render_template("index.html", spr = "Karkoli")


@app.route("/ball", methods= ["POST"])
def ball():
    tmp=dict(request.form)
    vprašanje1 = tmp.get("vprasanje1")
    list=["DA", "NE", "MOGOČE", "VPRAŠAJ KASNEJE"]
    r = f"{vprašanje1} = {random.choice(list)} "

    if vprašanje1=="ljubezen":
        r = f"{vprašanje1} = Kupi raje GPU."
    if vprašanje1== "vikend":
        r = f"{vprašanje1} = TikTok all day."
    if vprašanje1=="denar":
        r = f"{vprašanje1} = Burek only."
    if vprašanje1=="profesor":
        r = f"{vprašanje1} = F speedrun."
    if vprašanje1=="!":
        r = f"{vprašanje1} = Ne kriči."


    return render_template("index.html", rezultat = r)







app.run(debug=True)