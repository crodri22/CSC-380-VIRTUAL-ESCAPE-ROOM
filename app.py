from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
app = Flask("__Start__")


@app.route("/", methods = ['POST', 'GET'])
def home():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[0]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        jsdata = request.form['javascript_data']
        print(jsdata)
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home1'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content,
                                             url = 'http://localhost:5000/')


@app.route("/q2", methods = ['POST', 'GET'])
def home1():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[1]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        print(Answers)
        if PossibleChoices[result -1] == Answers:
            print(Answers + ":" +PossibleChoices[result -1])
            print("Correct")
            return redirect(url_for('home2'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q2')   


@app.route("/q3", methods = ['POST', 'GET'])
def home2():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[2]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home3'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q3')

@app.route("/q4", methods = ['POST', 'GET'])
def home3():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[3]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home4'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q4')

@app.route("/q5", methods = ['POST', 'GET'])
def home4():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[4]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home5'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q5')

                                             
@app.route("/q6", methods = ['POST', 'GET'])
def home5():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[5]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home6'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q6')

@app.route("/q7", methods = ['POST', 'GET'])
def home6():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[6]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home7'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q7')

@app.route("/q8", methods = ['POST', 'GET'])
def home7():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[7]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home8'))

    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q8')

@app.route("/q9", methods = ['POST', 'GET'])
def home8():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[8]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            print("Correct")
            return redirect(url_for('home9'))
    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q9')

@app.route("/q10", methods = ['POST', 'GET'])
def home9():
    con = sql.connect("Question.db")
    cur = con.cursor()
    cur.execute("select * from question")
    rows = cur.fetchall()
    question1 = rows[9]
    content = question1[1]
    Answers = question1[2]
    PossibleChoices = question1[3].split(',')
    if request.method == 'POST':
        name = request.form
        result2=name.to_dict(flat=False)
        for key,value in result2.items():
                   result = int(value[0])
        print(PossibleChoices[result -1])
        if PossibleChoices[result -1] == Answers:
            question1 = rows[1]
    return render_template('Questions.html', ans1 = PossibleChoices[0],
                                             ans2 = PossibleChoices[1],
                                             ans3 = PossibleChoices[2],
                                             ans4 = PossibleChoices[3],
                                             content = content, url = 'http://localhost:5000/q10')