from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route('/random')
def generate_random_number():
    random_number = random.randint(1, 100)

    # Write the random number to a file
    with open('/app/data/random_numbers.txt', 'a') as file:
        file.write(str(random_number) + '\n')

    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
