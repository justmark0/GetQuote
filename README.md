# GetQuote
SSD course lab assignment
Browse a random quote to give you encouragement and inspiration. 

### Screenshots & how to use
The button below greets you when you load the page
![button](https://github.com/justmark0/GetQuote/raw/main/demo/demo_image_1.jpg)

After pressing this button, you go to the page with the quote itself
![quote1](https://github.com/justmark0/GetQuote/raw/main/demo/demo_image_2.jpg)

Update page and receive one more quote!
![quote2](https://github.com/justmark0/GetQuote/raw/main/demo/demo_image_3.jpg)

### Demo
Simple gif demo of our project (a bit bugged, don't judge us)
![gif](https://github.com/justmark0/GetQuote/raw/main/demo/demo.gif)

### Installation guide
You need to have python3 installed. You can see how to install it on [python official site](https://www.python.org/)
Also you need to have pip installed. It reqularly installed automatically via python, but you can install 
Install pip the [official way](https://pip.pypa.io/en/stable/installing/):
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.8 get-pip.py
```
1. Clone repository
2. Go to root directory of the project `cd GetQuote`
3. **Optional** you can create virtual envinronment `python3 -m venv venv`
4. Install requirements via `pip install -r requirements.txt` 
5. Run the server via `python main.py`

### Frameworks and techonologies used
- Python [Flask](https://flask.palletsprojects.com/en/2.0.x/)
### Credits
The following are the profiles of those who contribute to our project. If you would like to read about the writers please feel free to visit their about page.
[Mark Nicholson](https://github.com/justmark0)
[Kseniya Kudasheva](https://github.com/molberte)
[Source site with quotes](https://www.wow4u.com/quotestopic/)

### Code examples
```
from flask import Flask, render_template
from random import randint
app = Flask(name)


quotes = ['here some quotes', 'many of them']


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/get_quote')
def quote():
    return quotes[randint(1, len(quotes))]


if name == 'main':
    app.run(debug=True, host='1.0.0.0', port=5000)
```

