import requests

dfa = 'http://127.0.0.1:5050/api/isDfaAccept_input'
uel = 'http://127.0.0.1:5050/api/Test'
nfa_accept = 'http://127.0.0.1:5050/api/isNfaAccept_input'
# nfa_read = 'http://127.0.0.1:5050/api/isNfaRead_input'

myobj = {'somekey': 'somevalue'}



# input('ppppppppppppppppppppppppppppppppppppp')
import json
# s=r''''''
j_a='''{"nodes":[{"x":84,"y":141,"text":"q0","isAcceptState":False,"isInitialState":True},{"x":325,"y":123,"text":"q1","isAcceptState":True,"isInitialState":False},{"x":243,"y":321,"text":"q2","isAcceptState":False,"isInitialState":False}],"links":[{"type":"Link","nodeA":0,"nodeB":1,"text":"a","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"SelfLink","node":1,"text":"a","anchorAngle":-0.9533603520021061},{"type":"Link","nodeA":1,"nodeB":2,"text":"","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"Link","nodeA":2,"nodeB":0,"text":"b","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0}]} '''
# a=json.loads(j_a)
# a={"initial_state":['a'],"nodes":[{"x":480,"y":287,"text":"b","isAcceptState":False},{"x":216,"y":338,"text":"a","isAcceptState":False},{"x":443,"y":421,"text":"c","isAcceptState":True}],"links":[{"type":"Link","nodeA":1,"nodeB":0,"text":"0","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"Link","nodeA":0,"nodeB":2,"text":"1","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"SelfLink","node":2,"text":"0","anchorAngle":0.7853981633974483},{"type":"SelfLink","node":2,"text":"1","anchorAngle":-0.13706617431018764}]}
# a["initial_state"]='a'

a={"nodes":[{"x":246,"y":159,"index":0,"text":"q0","isAcceptState":False,"isInitialState":True},{"x":410,"y":167,"index":1,"text":"q1","isAcceptState":False,"isInitialState":False},{"x":527,"y":257,"index":2,"text":"q2","isAcceptState":False,"isInitialState":False},{"x":338,"y":347,"index":3,"text":"q3","isAcceptState":False,"isInitialState":False}],"links":[{"type":"Link","nodeA":0,"nodeB":3,"text":"0:a","lineAngleAdjust":0,"parallelPart":0.3426771365960555,"perpendicularPart":71.838226769736},{"type":"Link","nodeA":0,"nodeB":1,"text":"1:b","lineAngleAdjust":3.141592653589793,"parallelPart":0.5152818991097922,"perpendicularPart":-51.183042675936775},{"type":"Link","nodeA":1,"nodeB":0,"text":"0:b","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"Link","nodeA":1,"nodeB":3,"text":"1:a","lineAngleAdjust":3.141592653589793,"parallelPart":0.3764367816091954,"perpendicularPart":-62.57932896566648},{"type":"SelfLink","node":2,"text":"0:b","anchorAngle":-1.9756881130799802},{"type":"SelfLink","node":2,"text":"1:a","anchorAngle":0},{"type":"Link","nodeA":3,"nodeB":1,"text":"0:a","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0},{"type":"Link","nodeA":3,"nodeB":0,"text":"1:b","lineAngleAdjust":0,"parallelPart":0.5,"perpendicularPart":0}],"availableIndexes":[4]}


# x = requests.post(dfa, json = {'dfa_data':a,'input_string':'1001'})
# x = requests.post(nfa, json = {'nfa_data':a,'input_string':'1001'})
# x = requests.post(nfa_accept, json = {'nfa_data':a,'input_string':'001'})
x = requests.post(uel, json = {'data':a,'input_string':['0100','ababba'],'type':'DFA'})

print(x.text)
# data=json.loads(x.text)
# print(data)
