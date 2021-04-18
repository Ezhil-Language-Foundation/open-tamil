# This Python file uses the following encoding: utf-8
# !/bin/env python3
# (C) 2020-2021, எழில் மொழி அறக்கட்டளை
# இந்த நிரல் ஓப்பன்-தமிழ் நிரல் தொகுப்பில் சேர்ந்ததாகும்.

# உரைவழி தமிழ் எண்களினை கொண்ட கணிதவியல்
# உள்ளீடை கணக்கிடும் ஒரு கருவி.
import operator
import re
import tamil
from tamil.numeral import tamilstr2num
from tamil.numeral import num2tamilstr, num2tamilstr_american
import ast

class SimpleCalculator(ast.NodeVisitor):
    """
    SimpleCalculator - replacement for eval() method to compute expressions involving
    +,-,/,* operators on constants.
    """
    def __init__(self,*args,**kwargs):
        super(SimpleCalculator,self).__init__(*args,**kwargs)
        self.result = 0.0

    def eval(self,obj):
        self.result = self.visit(obj.body[0])
        return self.result.n

    def visit_Expr(self, node: ast.Expr):
        return self.visit(node.value)

    def visit_BinOp(self, node: ast.BinOp):
        lhs = self.visit(node.left).n
        rhs = self.visit(node.right).n
        if isinstance(node.op,ast.Sub):
            return ast.Num(lhs - rhs)
        if isinstance(node.op,ast.Add):
            return ast.Num(lhs + rhs)
        if isinstance(node.op, ast.Mult):
            return ast.Num(lhs * rhs)
        if isinstance(node.op, ast.Div):
            return ast.Num(lhs / rhs)
        raise ValueError("Unsupported operation {0}".format(node.op))

    def visit_Num(self, node: ast.Num):
        return node

def அச்சிடு(_): print(_)

def கணி(expr):
    tree = ast.parse(expr,"__temp__.py")
    calculator = SimpleCalculator()
    return calculator.eval(tree)


செயல்சார்புகள்_குறியீடுகள் = ('+', '-', '*', '/', '(', ')')
செயல்சார்புகள் = {"கூட்டல்": ('+', operator.add), "கழித்தல்": ('-', operator.sub),
                  "பெருக்கல்": ('*', operator.mul), "வகுத்தல்": ('/', operator.truediv)}
அதிக_பட்சம் = 1001
வழுநீகால்_இயக்கம் = True


def கணக்கிடு(_தொடர்):
    """"
    @_தொடர் : Tamil sentence with number to be parsed and evaluated. Supported operators are +, -, /, * spelled out as
     கூட்டல், கழித்தல், பெருக்கல் and வகுத்தல்
    @return @விடை result variable of the computation
    """
    தமிழ்_உரை_தொடர் = re.sub('\s+', ' ', _தொடர்)
    # செயல்சார்புகளை குறியீடுகளாக மாற்றவும்
    for பெயர், குறியீடு in செயல்சார்புகள்.items():
        தமிழ்_உரை_தொடர் = தமிழ்_உரை_தொடர்.replace(பெயர், குறியீடு[0])
    இடைநிலை0 = list()
    இடைநிலை1 = list()
    for துண்டு in தமிழ்_உரை_தொடர்.split(' '):
        if துண்டு in செயல்சார்புகள்_குறியீடுகள்:
            if துண்டு in ('(', ')',) and len(இடைநிலை1) == 0:
                இடைநிலை0.append(துண்டு)
            else:
                மதிப்பு = tamil.numeral.tamilstr2num(இடைநிலை1)
                இடைநிலை0.append('%g' % மதிப்பு)
                இடைநிலை0.append(துண்டு)
                இடைநிலை1 = list()
        else:
            இடைநிலை1.append(துண்டு)
    # கடைசி செயல்சார்பின் எண் என்ன? விட்டுப்போகாமல் பாருங்கள்.
    if len(இடைநிலை1) > 0:
        மதிப்பு = tamilstr2num(இடைநிலை1)
        இடைநிலை0.append('%g' % மதிப்பு)
    # மீளமைப்பு செய்துகொள்ளுங்கள் ...
    தமிழ்_உரை_தொடர் = ' '.join(இடைநிலை0)
    if வழுநீகால்_இயக்கம்:
        அச்சிடு(தமிழ்_உரை_தொடர்)
    விடை = கணி(தமிழ்_உரை_தொடர்)
    # இருவகைகளில் எழுதிப்பார்க்கவும்.
    அச்சிடு(num2tamilstr(விடை))
    அச்சிடு(num2tamilstr_american(விடை))
    return விடை

if __name__ == "__main__":
    assert 2 == கணக்கிடு("ஒன்று கூட்டல் ஒன்று")
    assert 21 == கணக்கிடு("ஒன்று கூட்டல் இரண்டு பெருக்கல் பத்து")
    assert 950 == கணக்கிடு("ஓர் ஆயிரம் கழித்தல் ஐந்து பெருக்கல் ( ஒன்பது கூட்டல் ஒன்று )")
    assert 1e6 == கணக்கிடு("ஒரு இலட்சம்  பெருக்கல் பத்து")
