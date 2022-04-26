

def clean_(a):
    states=[]
    final_states=[]
    node_number={}
    for n,i in enumerate(a['nodes']):
        node_number[n]=i['text']
        if i['isAcceptState']:
            final_states.append(i['text'])
        if i['isInitialState']:
            initial_state=i['text']
        states.append(i['text'])

    transitions={}
    input_symbol=[]
    for n,i in enumerate(a['links']):
        if not i['text'] == '':
            input_symbol.append(i['text'])
        # print(i)
        if i['type']=='Link':
            if not node_number[i['nodeA']] in transitions: 
                transitions[node_number[i['nodeA']]]={i['text']:node_number[i['nodeB']]}
            else:
                transitions[node_number[i['nodeA']]][i['text']]=node_number[i['nodeB']]
        elif i['type']=='SelfLink':
            if not node_number[i['node']] in transitions: 
                transitions[node_number[i['node']]]={i['text']:node_number[i['node']]}
            else:
                transitions[node_number[i['node']]][i['text']]=node_number[i['node']]

    input_symbol=set(input_symbol)
    for state in states:
        if not state in transitions:
            transitions[state]={}
            for i in input_symbol:
                transitions[state][i]=state
    return list(states),list(input_symbol),transitions,initial_state,list(final_states)
# print(clean_(a))




a={"nodes":[{"x":210,"y":261,"text":"q0","isAcceptState":False,"isInitialState":True},{"x":363,"y":265,"text":"q1","isAcceptState":False,"isInitialState":False},{"x":532,"y":267,"text":"q2","isAcceptState":True,"isInitialState":False}],"links":[{"type":"Link","nodeA":0,"nodeB":1,"text":"1","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"SelfLink","node":1,"text":"0","anchorAngle":-1.4352686128093959},{"type":"Link","nodeA":1,"nodeB":2,"text":"1","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0}]}

def clean_NDFA(a):
    states=[]
    final_states=[]
    node_number={}
    for n,i in enumerate(a['nodes']):
        node_number[n]=i['text']
        if i['isAcceptState']:
            final_states.append(i['text'])
        if i['isInitialState']:
            initial_state=i['text']
        states.append(i['text'])

    transitions={}
    input_symbol=[]
    for n,i in enumerate(a['links']):


        if i['type']=='Link':
            if not node_number[i['nodeA']] in transitions:
                transitions[node_number[i['nodeA']]]={i['text']:[node_number[i['nodeB']]]}
            else:
                # print(node_number[i['nodeA']])
                # transitions[node_number[i['nodeA']]]={}
                if i['text'] in transitions[node_number[i['nodeA']]]: 
                    transitions[node_number[i['nodeA']]][i['text']].append(node_number[i['nodeB']])
                else:
                    transitions[node_number[i['nodeA']]][i['text']]=[node_number[i['nodeB']]]

        else:
            if not node_number[i['node']] in transitions:
                transitions[node_number[i['node']]]={i['text']:[node_number[i['node']]]}
            else:
                # print(node_number[i['nodeA']])
                node_number[i['node']]={}
                transitions[node_number[i['node']]][i['text']]=transitions[node_number[i['node']]][i['text']].append(i['node'])

    input_symbol=set(input_symbol)
    for state in states:
        if not state in transitions:
            transitions[state]={}
            for i in input_symbol:
                transitions[state][i]=state
    return list(states),list(input_symbol),transitions,initial_state,list(final_states)

# states,input_symbol,transitions,initial_state,final_states=clean_NDFA(a)
# print(transitions)



def clean_DFA_NFA(a):
    states=[]
    final_states=[]
    node_number={}
    for n,i in enumerate(a['nodes']):
        node_number[n]=i['text']
        if i['isAcceptState']:
            final_states.append(i['text'])
        if i['isInitialState']:
            initial_state=i['text']
        states.append(i['text'])

    transitions=[]
    input_symbol=[]
    for n,i in enumerate(a['links']):
        input_symbol.append(i['text'])
        if i['type']=='Link':
            transitions.append([node_number[i['nodeA']],i['text'],node_number[i['nodeB']]])
        else:
            transitions.append([node_number[i['node']],i['text'],node_number[i['node']]])
        # print(i)

        # if i['type']=='Link':
        #     if not node_number[i['nodeA']] in transitions:
        #         transitions[node_number[i['nodeA']]]={i['text']:[node_number[i['nodeB']]]}
        #     else:
        #         # print(node_number[i['nodeA']])
        #         # transitions[node_number[i['nodeA']]]={}
        #         if i['text'] in transitions[node_number[i['nodeA']]]: 
        #             transitions[node_number[i['nodeA']]][i['text']].append(node_number[i['nodeB']])
        #         else:
        #             transitions[node_number[i['nodeA']]][i['text']]=[node_number[i['nodeB']]]

        # else:
        #     if not node_number[i['node']] in transitions:
        #         transitions[node_number[i['node']]]={i['text']:[node_number[i['node']]]}
        #     else:
        #         # print(node_number[i['nodeA']])
        #         node_number[i['node']]={}
        #         transitions[node_number[i['node']]][i['text']]=transitions[node_number[i['node']]][i['text']].append(i['node'])

    # input_symbol=set(input_symbol)
    # for state in states:
    #     if not state in transitions:
    #         transitions[state]={}
    #         for i in input_symbol:
    #             transitions[state][i]=state
    input_symbol=set(input_symbol)
    return len(states),list(states),len(input_symbol),list(input_symbol),initial_state,len(final_states),list(final_states),len(transitions),transitions


# print(clean_DFA_NFA(a),end='\n')
# nfa = DFA_NFA(
# 	4, # number of states
# 	['A', 'B', 'C', 'D'], # array of states
# 	3, # number of alphabets
# 	['a', 'b', 'c'], # array of alphabets
# 	'A', # start state
# 	1, # number of final states
# 	['D'], # array of final states
# 	7, # number of transitions
# 	[['A', 'a', 'A'], ['A', 'e', 'B'], ['B', 'b', 'B'],
# 	['A', 'e', 'C'], ['C', 'c', 'C'], ['B', 'b', 'D'],
# 	['C', 'c', 'D']]

# 	# array of transitions with its element of type :
# 	# [from state, alphabet, to state]
# )



# {'q1', 'q0', 'q2'} 
# { 'a', 'b'} 
# {'q0': {'a': 'q1'}, 'q1': {'a': 'q1', '': 'q2'}, 'q2': {'b': 'q0'}}
#  q0
#   {'q1'}