from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

words = ["python", "hangman", "college", "project", "telangana"]

hints = {
    "python": "🐍 Programming language",
    "hangman": "🎮 Game name",
    "college": "🏫 Place of study",
    "project": "💻 Work assignment",
    "telangana": "✈️ State name"
}

hangman_stages = [
    "😵\n\n\n",
    "😵\n |\n\n",
    "😵\n/|\n\n",
    "😵\n/|\\\n\n",
    "😵\n/|\\\n/ \n"
]


# 🔄 Start a new game
def new_game():
    global word, guessed, tries
    word = random.choice(words)
    guessed = []
    tries = 5


# First game
new_game()


@app.route("/", methods=["GET", "POST"])
def index():
    global word, guessed, tries

    message = ""
    feedback = ""

    if request.method == "POST" and tries > 0:
        guess = request.form["guess"].lower()

        if guess and guess not in guessed:
            guessed.append(guess)

            if guess in word:
                feedback = "✅ Correct Guess! 🎉"
            else:
                tries -= 1
                feedback = "❌ Wrong Guess! 😢"

    # Display word with spaces
    display = " ".join([c if c in guessed else "_" for c in word])

    # Win / Lose messages
    if "_" not in display:
        message = "🎉 You Win! 🏆"
    elif tries == 0:
        message = f"💀 Game Over! Word was: {word}"

    stage_index = min(5 - tries, 4)

    return render_template(
        "index.html",
        hangman=hangman_stages[stage_index],
        display_word=display,
        hint=hints[word],
        message=message,
        feedback=feedback,
        tries=tries
    )


# 🔄 Restart Game
@app.route("/restart")
def restart():
    new_game()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)