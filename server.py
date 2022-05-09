from functools import wraps
from itsdangerous import json
# from nltk.corpus import stopwords
from flask import send_file

from flask import Flask, abort, request,render_template
from flask_cors import CORS,cross_origin
from sample import clean_, clean_DFA_NFA

# from automata.fa.dfa import DFA
from DFA import DFA
from NDFA import NDFA

from nfa_to_dfa import function_Nfa_Dfa
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
    if type=='DFA_NFA':
        return TestDFA_NFA(a,input_string)



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
        print(testData)
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
        # print(ndfa.is_string_valid(input_string))
        # print(transitions)
        # print (ndfa.convert_to_dfa())

        return {'response':str(ndfa.is_string_valid(input_string))}

    except:
        return 'Not a Valid NDFA'


def TestDFA_NFA(a,input_string):
    print('here')
    a1,a2,a3,a4,a5,a6,a7,a8,a9=clean_DFA_NFA(a)
    res=function_Nfa_Dfa(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    return res

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
