from flask import Flask, render_template
import random

app = Flask(__name__)

# Read file and extract links
links = []
with open("blind75.txt", "r") as file:
    for line in file:
        l = 0
        r = 0
        for i in range(len(line)):
            if line[i] == '(':
                l = i
            if line[i] == ')':
                r = i
        links.append(line[l + 1:r])

# Function to get a random index
def get_random_index(links):
    random_float = random.random()
    random_index = int(random_float * len(links))
    return random_index

# Route to display the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get a random link
@app.route('/get_link')
def get_link():
    random_index = get_random_index(links)
    random_element = links[random_index]
    return random_element

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
