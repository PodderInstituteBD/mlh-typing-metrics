from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Sample text to type
sample_text = "The quick brown fox jumps over the lazy dog."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/typing')
def typing():
    return render_template('typing.html', text=sample_text)

@app.route('/result', methods=['POST'])
def result():
    typed_text = request.form['typed_text']
    start_time = float(request.form['start_time'])
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    word_count = len(typed_text.strip().split())
    minutes = elapsed_time / 60
    wpm = round(word_count / minutes) if minutes > 0 else 0

    typed_words = typed_text.strip().split()
    original_words = sample_text.strip().split()
    correct_words = sum(
        1 for i, word in enumerate(typed_words)
        if i < len(original_words) and word == original_words[i]
    )
    accuracy = round((correct_words / len(original_words)) * 100) if original_words else 0

    return render_template("result.html",
                           time=elapsed_time,
                           word_count=word_count,
                           wpm=wpm,
                           accuracy=accuracy)

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)
