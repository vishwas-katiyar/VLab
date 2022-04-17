

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
                transitions[node_number[i['nodeA']]]={i['text']:{node_number[i['nodeB']]}}
            else:
                transitions[node_number[i['nodeA']]][i['text']]={node_number[i['nodeB']]}
        elif i['type']=='SelfLink':
            if not node_number[i['node']] in transitions: 
                transitions[node_number[i['node']]]={i['text']:{node_number[i['node']]}}
            else:
                transitions[node_number[i['node']]][i['text']]={node_number[i['node']]}

    input_symbol=set(input_symbol)
    for state in states:
        if not state in transitions:
            transitions[state]={}
            for i in input_symbol:
                transitions[state][i]=state
    return set(states),set(input_symbol),transitions,initial_state,set(final_states)
# print(clean_(a))




# {'q1', 'q0', 'q2'} 
# {'', 'a', 'b'} 
# {'q0': {'a': 'q1'}, 'q1': {'a': 'q1', '': 'q2'}, 'q2': {'b': 'q0'}}
#  q0
#   {'q1'}