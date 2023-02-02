from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
        return "Hello, World!"

    @app.route("/greet", methods=["GET", "POST"])
    def greet():
            if request.method == "POST":
                        name = request.form["name"]
                                return render_template("greet.html", name=name)
                                else:
                                            return render_template("greet_form.html")

                                        if __name__ == "__main__":
                                                app.run()

