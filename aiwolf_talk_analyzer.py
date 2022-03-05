#https://github.com/lark-parser/lark
#pip install lark
from lark import Lark, Transformer

grammar = open('aiwolf_talk_grammer.txt').read()
parser = Lark(grammar, start='sentence')

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
    
    #予約語と被るので、先頭にoperatorのoを付ける
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
    tree = parser.parse(talk)
    #print(tree.pretty())
    return TreeToDict().transform(tree)