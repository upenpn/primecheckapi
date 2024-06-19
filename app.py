from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/is_prime', methods=['GET'])
def check_prime():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({"error": "Please provide a number"}), 400
    result = is_prime(number)
    return jsonify({"number": number, "is_prime": result})

if __name__ == '__main__':
    app.run(debug=True)
