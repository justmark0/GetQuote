from flask import Flask, render_template
from random import randint
app = Flask(__name__)


quotes = ['I have always believed that each man makes his own happiness and is responsible for his own problems. It is a simple philosophy. Ray Kroc, Grinding It Out', 'When we have respect for ourselves and others, we gravitate towards connections that encourage that. Simeon Lindstrom, Codependency - Loves Me, Loves Me Not', 'Anger is the ultimate destroyer of your own peace of mind. Dalai Lama', 'A man should have the aim and the determination to be honest and upright and sincere in all that he undertakes. If he adds persistency to this he can hardly help being successful L. R. Ellert, Success In Life', "Only one thing is ever guaranteed, that is that you will definitely not achieve the goal if you don't take the shot. Wayne Gretzky", "Don't be afraid. Be focused. Be determined. Be hopeful. Be empowered. Michelle Obama", 'The fact is that grief today is a family matter as much a s it is an individual one. Barbara Okun, Ph.D. Saying Goodbye', 'Children really brighten up a household. They never turn the lights off. Ralph Bus', '"No one would have crossed the ocean if he could have gotten off the ship in the storm." Charles Kettering', "Congratulations! today is your day. You're off to Great Places! You're off and away. Dr. Seuss, Oh, the Places You'll Go!", '"Appreciate those early influences and what they\'ve done for you." Willie Davis, Closing the Gap', 'Emotional empathy is what motivates us to help others. Brian Goldman, The Power of Kindness', "The true wealth of a nation lies not in it's gold or silver but in it's learning, wisdom and in the uprightness of its sons. Kahlil Gibran", 'Make the decision, make another. Remake one past, you cannot. Yoda', 'Be honest in your feelings, for they are the surest conduit to knowledge... Anoon Bondara']


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/get_quote')
def quote():
    return quotes[randint(0, len(quotes))]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
