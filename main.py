from flask import Flask, jsonify, render_template, request
from transformers import pipeline
import re

pipe = pipeline("text-generation", 
                model="./model", 
                max_length=256, 
                min_new_tokens=1, 
                num_beams=3,
                repetition_penalty=1.2,
                early_stopping=True,
                eos_token_id=198,
                temperature=0.9,
                device = 0)
app = Flask(__name__, )

@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

@app.route('/process', methods=['POST'])
def process(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    question = data['value']
    print(question)
    answer = pipe(f"{question}")[0]['generated_text']
    answer = re.sub(re.compile(r'[^.!?]*\?'), '', answer)
    print(answer)
    return jsonify(result=answer) # return the result to JavaScript 

if __name__ == '__main__':
    app.run(debug=False, port = '5000')

