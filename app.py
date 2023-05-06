from flask import Flask, jsonify, json, request

import sentencepiece as spm
app = Flask(__name__)
vocab_file = "vocabmodel/kowiki.model"
vocab = spm.SentencePieceProcessor()
vocab.load(vocab_file)


print(len(vocab))
@app.route("/", methods=['POST'])

def test():
    params = request.get_json()

    print("받은 Json 데이터 ", params)

    output = vocab.encode_as_ids(params["sentence"])

    response = {
        "result": output
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



"""
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
"""