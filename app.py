from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/quiz', methods=['POST'])
def quiz():
    operation = request.form.get('operation')
    symbols = {'+': '+', '-': '-', '*': '*', '/': '/'}
    numbers = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(5)]
    return render_template('question.html', operation=symbols[operation], numbers=numbers)


@app.route('/result', methods=['POST'])
def result():
    correct_answers = 0
    total_questions = int(request.form.get('total_questions'))

    for i in range(total_questions):
        user_answer = float(request.form.get(f'answer_{i}'))
        if user_answer == eval(request.form.get(f'question_{i}')):
            correct_answers += 1

    incorrect_answers = total_questions - correct_answers
    return render_template('result.html', correct=correct_answers, incorrect=incorrect_answers)

if __name__ == '__main__':
    app.run(debug=True)
