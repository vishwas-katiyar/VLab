# 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


from functools import wraps
from itsdangerous import json
# from nltk.corpus import stopwords
from flask import send_file
from pdf2image import convert_from_path
import base64

from flask import send_file

from flask import Flask, abort, request,render_template
from flask_cors import CORS,cross_origin
from sample import clean_, clean_DFA_NFA,clean_Moore,clean_Mealy

# from automata.fa.dfa import DFA
from DFA import DFA
from NDFA import NDFA

from nfa_to_dfa import function_Nfa_Dfa
from Moore import Moore
from Mealy import Mealy
# from automata.fa.nfa import NFA
# import automata.base.exceptions as exceptions
# from automata.base.automaton import Automaton

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/api/Test',methods=['POST'])
# @check_login
@cross_origin()
def TEST():
    type=request.json['type']
    a=request.json['data']
    input_string=request.json['input_string']
    print(input_string)
    if type=='DFA':
        return TestDFA(a,input_string)
    if type=='NDFA':
        print('NDFA')
        return TestNDFA(a,input_string)
    if type=='NFA_DFA':
        return TestNFA_DFA(a,input_string)
    if type=='MOORE':
        return TestMoore(a,input_string)
    if type=='MEALY':
        return TestMealy(a,input_string)



def TestDFA(a,input_string):
    try:
    # if 1:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        dfa = DFA(
        states=states,
        alphabet=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        # z=map(dfa.is_string_valid,input_string)
        testData = []
        for i in input_string:
            testData.append(dfa.is_string_valid(i))
        # print(list(z))
        # print(testData)
        return {'res':testData}
    except:
        return {'msg':'Not a Valid DFA'}



def TestNDFA(a,input_string):
    try:
    # if 1:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        ndfa = NDFA(
        states=states,
        alphabet=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        testData = []
        for i in input_string:
            testData.append(ndfa.is_string_valid(i))
        # print(list(z))
        # print(testData)
        return {'res':testData}
    except:
        return {'msg':'Not a Valid NDFA'}

 
def TestNFA_DFA(a,input_string):
    try:
        print('here')
        a1,a2,a3,a4,a5,a6,a7,a8,a9=clean_DFA_NFA(a)
        res=function_Nfa_Dfa(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        # pip install pdf2image

        pages = convert_from_path('dfa.pdf', 500)

        for page in pages:
            page.save('nfa.jpg', 'JPEG')

        with open("nfa.jpg", "rb") as image_file:
            encoded_nfa = base64.b64encode(image_file.read())

        return {'res':res,'converted':'data:image/png;base64,'+encoded_nfa.decode('utf-8')}
    except:
        return {'msg':'Not a Valid DFA','res':None}
    



def TestMoore(a,input_string):
    try:
    # if 1:
        print('here2')

        states,input_alphabet,output_alphabet,transitions,initial_state,output_table=clean_Moore(a)

        # print(states,input_alphabet,output_alphabet,transitions,output_table,initial_state)

        moore=Moore(states,input_alphabet, output_alphabet, transitions, initial_state, output_table)
        print(moore)
        temp=[]
        for i in input_string:
            try:
                temp.append(moore.get_output_from_string(i))
            except:
                temp.append('Not a valid input.')
        return {'res':temp}

    except:
        return {'msg':'Not a Valid Moore','res':None}


def TestMealy(a,input_string):
    try:
    # if 1:
        print('here3')

        states,input_alphabet,output_alphabet,transitions,initial_state=clean_Mealy(a)

        mealy=Mealy(states,input_alphabet,output_alphabet,transitions,initial_state)
        print(mealy)
        temp=[]
        for i in input_string:
            try:
                temp.append(mealy.get_output_from_string(i))
            except:
                temp.append('Not avalid input.')
        return {'res':temp}

    except:
        return {'msg':'Not a Valid Mealy','res':None}

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


if __name__ == '__main__':
    app.run(port=5050, debug=True)
