

a={"nodes":[{"x":223,"y":107,"index":0,"text":"q0:1","isAcceptState":False,"isInitialState":True},{"x":427,"y":107,"index":1,"text":"q1:1","isAcceptState":False,"isInitialState":False},{"x":427,"y":321,"index":2,"text":"q2:0","isAcceptState":False,"isInitialState":False}],"links":[{"type":"Link","nodeA":0,"nodeB":1,"text":"a","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"Link","nodeA":1,"nodeB":2,"text":"a","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"SelfLink","node":2,"text":"a","anchorAngle":1.9513027039072617},{"type":"Link","nodeA":2,"nodeB":0,"text":"b","lineAngleAdjust":0,"parallelPart":0.5276536253680443,"perpendicularPart":16.88633151640753},{"type":"Link","nodeA":0,"nodeB":2,"text":"b","lineAngleAdjust":0,"parallelPart":0.4963248533118685,"perpendicularPart":27.21419412824141},{"type":"SelfLink","node":1,"text":"b","anchorAngle":-1.965587446494658}],"availableIndexes":[3,4]} 

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




# a={"nodes":[{"x":210,"y":261,"text":"q0","isAcceptState":False,"isInitialState":True},{"x":363,"y":265,"text":"q1","isAcceptState":False,"isInitialState":False},{"x":532,"y":267,"text":"q2","isAcceptState":True,"isInitialState":False}],"links":[{"type":"Link","nodeA":0,"nodeB":1,"text":"1","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"SelfLink","node":1,"text":"0","anchorAngle":-1.4352686128093959},{"type":"Link","nodeA":1,"nodeB":2,"text":"1","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0}]}

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
        
    input_symbol=set(input_symbol)
    return len(states),list(states),len(input_symbol),list(input_symbol),initial_state,len(final_states),list(final_states),len(transitions),transitions




def clean_Moore(a):
    states=[]
    input_alphabet=[]
    output_alphabet=[]
    transitions={}
    initial_state=''
    output_table={}


    node_number={}
    for n,i in enumerate(a['nodes']):
        node_number[n]=i['text']
        if i['isInitialState']:
            initial_state=i['text'].split(':')[0]
        output_alphabet.append(i['text'].split(':')[1])
        t=i['text'].split(':')
        states.append(t[0])
        output_table[t[0]]=t[1]

    transitions={}
    input_symbol=[]
    for n,i in enumerate(a['links']):
        # print(i)

        input_symbol.append(i['text'])
        if i['type']=='Link':
            if node_number[i['nodeA']].split(':')[0] in transitions:
                transitions[node_number[i['nodeA']].split(':')[0]][i['text']]=node_number[i['nodeB']].split(':')[0]
            else: 
                transitions[node_number[i['nodeA']].split(':')[0]]={i['text']:node_number[i['nodeB']].split(':')[0]}
        else:
            if node_number[i['node']].split(':')[0] in transitions:
                transitions[node_number[i['node']].split(':')[0]][i['text']]=node_number[i['node']].split(':')[0]
            else:
                transitions[node_number[i['node']].split(':')[0]]={i['text']:node_number[i['node']].split(':')[0]}

    input_symbol=set(input_symbol)
    return list(states),list(set(input_symbol)),list(set(output_alphabet)),transitions,initial_state,output_table


# print(clean_Moore(a))