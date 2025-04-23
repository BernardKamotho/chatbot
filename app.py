from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    (r"hi|hello|hey", ["Hello, How can I assist you today?", "Hi there! How can I help?"]),
    (r"how are you?", ["I'm doing great, thanks for asking!", "I'm good, how about you?"]),
    (r"am good", ["Nice to hear that", "That's better"]),
    (r"(.*)color(.*)", ["I like all colors! What about you?", "I don't have a favorite color!"]),
    (r"(.*)(course|program)(.*)", ["We offer great programs in Android development and Full Stack Development. Would you like to know more about them?"]),
    (r"(.*)android(.*)", ["We offer an Android development program where you'll learn how to build mobile apps using Java and Kotlin. Interested?"]),
    (r"(.*)full stack(.*)", ["Our Full Stack Development program covers both front-end (HTML, CSS, JavaScript) and back-end (Node.js, Django, etc.) technologies. Would you like to join?"]),
    (r"(.*)mobile\s?apps(.*)|(.*)applications(.*)", ["We offer mobile apps training in android and react native"]),
    (r"(.*)", ["Sorry, I didn't understand that. Could you ask something else?", "Can you please clarify?"]),
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    print(user_input)
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
