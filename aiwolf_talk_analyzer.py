#https://github.com/lark-parser/lark
#pip install lark
from lark import Lark, Transformer

#japanese
#http://aiwolf.org/control-panel/wp-content/uploads/2019/02/protocol_2019_3_6m.pdf
#english
#http://aiwolf.org/control-panel/wp-content/uploads/2019/05/protocol_3_6.pdf
class TreeToDict(Transformer):    
    #species
    def species(self,attr):
        return str(attr[0].data)
    #role
    def role(self,attr):
        return str(attr[0].data)

    #target,subject
    def target(self,attr):
        return attr[0]
    def subject(self,attr):
        return attr[0]

    def agent(self,attr):
        return attr[0]
    def any(self):
        return "any"
    def unspec(self):
        return "unspec"

    #sentence
    def estimate(self,attr):
        return {"word":"estimate","subject":attr[0],"target":attr[1],"role":attr[2]}
    def comingout(self,attr):
        return {"word":"comingout","subject":attr[0],"target":attr[1],"role":attr[2]}
    
    def divination(self,attr):
        return {"word":"divination","subject":attr[0],"target":attr[1]}
    def guard(self,attr):
        return {"word":"guard","subject":attr[0],"target":attr[1]}
    def vote(self,attr):
        return {"word":"vote","subject":attr[0],"target":attr[1]}
    def attack(self,attr):
        return {"word":"attack","subject":attr[0],"target":attr[1]}
    
    def divined(self,attr):
        return {"word":"divined","subject":attr[0],"target":attr[1],"species":attr[2]}
    def identified(self,attr):
        return {"word":"identified","subject":attr[0],"target":attr[1],"species":attr[2]}
    def guarded(self,attr):
        return {"word":"guarded","subject":attr[0],"target":attr[1],"species":attr[2]}
    def voted(self,attr):
        return {"word":"voted","subject":attr[0],"target":attr[1],"species":attr[2]}
    def attacked(self,attr):
        return {"word":"attacked","subject":attr[0],"target":attr[1],"species":attr[2]}
    
    def agree(self,attr):
        return {"word":"agree","subject":attr[0],"int":attr[1]}
    def disagree(self,attr):
        return {"word":"disagree","subject":attr[0],"int":attr[1]}
    
    def over(self):
        return {"word":"over"}
    def skip(self):
        return {"word":"skip"}

    #operator
    def request(self,attr):
        return {"word":"request","subject":attr[0],"target":attr[1],"sentence":attr[2]}
    def inquire(self,attr):
        return {"word":"inquire","subject":attr[0],"target":attr[1],"sentence":attr[2]}

    def because(self,attr):
        return {"word":"because","subject":attr[0],"sentence1":attr[2],"sentence2":attr[3]}

    def day(self,attr):
        return {"word":"day","subject":attr[0],"day":attr[1],"sentence":attr[2]}
    
    #????????????????????????????????????operator???o????????????
    def o_not(self,attr):
        return {"word":"not","subject":attr[0],"sentence":attr[1]}
    def o_and(self,attr):
        return {"word":"and","subject":attr[0],"sentences":attr[1:]}
    def o_or(self,attr):
        return {"word":"or","subject":attr[0],"sentences":attr[1:]}
    def o_xor(self,attr):
        return {"word":"xor","subject":attr[0],"sentences":attr[1:]}
    
    def int(self,attr):
        return int(attr[0])


def talk2dict(talk):
    tree = talk2Tree(talk)
    #print(tree.pretty())
    return tree2dict(tree)

def talk2Tree(talk):
    parser=Lark(grammar, start='sentence')
    return parser.parse(talk)

def tree2dict(tree):
    return TreeToDict().transform(tree)

grammar=r"""
//sentence
?sentence:estimate|comingout|divination|guard|vote|attack|divined|identified|guarded|voted|attacked|agree|disagree|over|skip|request|inquire|because|day|o_not|o_and|o_or|o_xor

//1 word
//species
species:human|werewolf

human:"HUMAN"
werewolf:"WEREWOLF"

//role
role: villager|seer|medium|bodyguard|possessed|werewolf

villager:"VILLAGER"
seer:"SEER"
medium:"MEDIUM"
bodyguard:"BODYGUARD"
possessed:"POSSESSED"

//target,subject
target:agent|any
subject:agent|any|unspec

agent:"Agent[" ["0"] int "]"
any:"ANY"
unspec:"UNSPEC"


//2 sentence
estimate:[subject] "ESTIMATE" target role
comingout:[subject] "COMINGOUT" target role

divination:[subject] "DIVINATION" target
guard:[subject] "GUARD" target
vote:[subject] "VOTE" target
attack:[subject] "ATTACK" target

divined:[subject] "DIVINED" target [species]
identified:[subject] "IDENTIFIED" target [species]
guarded:[subject] "GUARDED" target [species]
voted:[subject] "VOTED" target [species]
attacked:[subject] "ATTACKED" target [species]

agree:[subject] "AGREE" int
disagree:[subject] "DISAGREE" int

over:"OVER"
skip:"SKIP"


//3 operator
request:[subject] "REQUEST" target "(" sentence ")"
inquire:[subject] "INQUIRE" target "(" sentence ")"

because:[subject] "BECAUSE" "(" sentence ")" "(" sentence ")"

day:[subject] "DAY" int "(" sentence ")"

//Prefix with o_ because it covers a reserved word. o means operator.
o_not:[subject] "NOT" ( "(" sentence ")" )
o_and:[subject] "AND" ( "(" sentence ")" )+
o_or:[subject] "OR" ( "(" sentence ")" )+
o_xor:[subject] "XOR" ( "(" sentence ")" )+


int: INT
%import common.INT
%import common.WS
%ignore WS
"""