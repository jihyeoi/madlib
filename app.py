from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.get('/questions/')
def questions():
    prompts = request.args['noun']

    return render_template("questions.html",
                           prompts=noun)




    silly_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],

)



