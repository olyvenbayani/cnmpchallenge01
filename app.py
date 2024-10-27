from flask import Flask, jsonify
import random

app = Flask(__name__)

# Expanded list of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "What do you call fake spaghetti? An impasta!",
    "I told my wife she should embrace her mistakes... so she gave me a hug.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you get if you cross a snowman and a vampire? Frostbite!",
    "I would tell you a joke about an elevator, but it's an uplifting experience.",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
    "How does a penguin build its house? Igloos it together!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "I tried to catch fog yesterday... Mist.",
    "What did the janitor say when he jumped out of the closet? Supplies!",
    "What’s orange and sounds like a parrot? A carrot!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "I told my computer I needed a break, and now it won’t stop sending me KitKats!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why can't you hear a pterodactyl go to the bathroom? Because the 'P' is silent!"
]

@app.route('/joke', methods=['GET'])
def get_joke():
    joke = random.choice(jokes)
    return jsonify({'joke': joke})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
