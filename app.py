from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

# answer = {}

@app.get('/questions')
def questions():
    prompts = silly_story.prompts
    return render_template("questions.html",
                           prompts = prompts)

@app.get('/results')
def results():
    # for prompt in prompts:
    #     prompt_value = request.args["prompt"]
    #     answer.update({prompt: prompt_value})
    madlib = silly_story.get_result_text(request.args)
    return render_template("results.html", madlib = madlib)