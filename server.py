from functools import wraps
from itsdangerous import json
# from nltk.corpus import stopwords
from flask import send_file

from flask import Flask, abort, request,render_template
from flask_cors import CORS
from sample import clean_

from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import automata.base.exceptions as exceptions
from automata.base.automaton import Automaton

app = Flask(__name__)
CORS(app)

@app.route('/api/isDFA')
# @check_login
def isDFA():
    a=request.json['dfa_data']
    try:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        print(states,input_symbol,transitions,initial_state,final_states)
        dfa = DFA(
        states=states,
        input_symbols=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        # print(dfa.accepts_input('00'))
        return str(dfa.validate())
    except:
        return 'Not a Valid DFA'

@app.route('/api/isDfaAccept_input',methods=['POST'])
def isDfaAccept_input():
    # print('PPPPPPPPPPPPPPP',request.data)
    a=request.json['dfa_data']
    input_string=request.json['input_string']
    # print(request.form)
    # print(request.get_json(force=True))
    try:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        print(states,input_symbol,transitions,initial_state,final_states)
        dfa = DFA(
        states=states,
        input_symbols=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        # print()
        return str(dfa.accepts_input(input_string))
    except:
        return 'Not a Valid DFA'

@app.route('/api/isDfaRead_input',methods=['POST'])
def isDfaRead_input():
    a=request.json['dfa_data']
    input_string=request.json['input_string']
    try:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        print(states,input_symbol,transitions,initial_state,final_states)
        dfa = DFA(
        states=states,
        input_symbols=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        # print()
        return str(dfa.read_input(input_string))
    except:
        return 'Not a Valid DFA'



@app.route('/api/isNfa',methods=['POST'])
def isNFA():
    a=request.json['nfa_data']
    try:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        print(states,input_symbol,transitions,initial_state,final_states)
        nfa = NFA(
        states=states,
        input_symbols=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        print('NFAA')
        return str(nfa.validate())
    except:
        return 'Not a Valid NFA'



@app.route('/api/isNfaAccept_input',methods=['POST'])
def isNfaAccept_input():
    print('###########3')

    # print('PPPPPPPPPPPPPPP',request.data)
    a=request.json['nfa_data']
    input_string=request.json['input_string']
    # print(request.form)
    # print(request.get_json(force=True))
    try:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        # print(states,input_symbol,transitions,initial_state,final_states)
        nfa = NFA(
        states=states,
        input_symbols=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        print('###########3')
        return str(nfa.accepts_input(input_string))
    except:
        return 'Not a Valid NFA'


@app.route('/api/isNfaRead_input',methods=['POST'])
def isNfaRead_input():
    # print('PPPPPPPPPPPPPPP',request.data)
    print('###########3')

    a=request.json['nfa_data']
    input_string=request.json['input_string']
    # print(request.form)
    # print(request.get_json(force=True))
    try:

    # if True:
        states,input_symbol,transitions,initial_state,final_states=clean_(a)
        print(states,input_symbol,transitions,initial_state,final_states)
        nfa = NFA(
        states=states,
        input_symbols=input_symbol,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )
        print('###########3')
        return str(nfa.read_input(input_string))
    except exceptions.RejectionException:
        return 'RejectionException'
    except :
        return 'Not A valid NFA'


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
