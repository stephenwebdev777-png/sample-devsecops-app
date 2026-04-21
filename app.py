# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     result = None
#     if request.method == "POST":
#         num1 = request.form.get("num1")
#         num2 = request.form.get("num2")
#         operation = request.form.get("operation")

#         try:
#             num1 = float(num1)
#             num2 = float(num2)

#             if operation == "add":
#                 result = num1 + num2
#             elif operation == "sub":
#                 result = num1 - num2
#             elif operation == "mul":
#                 result = num1 * num2
#             elif operation == "div":
#                 result = num1 / num2
#         except:
#             result = "Error"

#     return render_template("index.html", result=result)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)








# valnarability code
# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     result = ""

#     if request.method == "POST":
#         expression = request.form.get("expression")

#         try:
#             result = str(eval(expression))
#         except:
#             result = "Error"

#     return render_template("index.html", result=result)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

    # just add a comment in app.py
# test change









from flask import Flask, render_template, request
import re

app = Flask(__name__)

# ✅ Allow only safe math characters
def safe_eval(expression):
    if not re.match(r'^[0-9+\-*/().% ]+$', expression):
        return "Invalid input"

    try:
        return str(eval(expression))
    except:
        return "Error"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")

        # Limit input length (prevent abuse)
        if len(expression) > 50:
            result = "Input too long"
        else:
            result = safe_eval(expression)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


