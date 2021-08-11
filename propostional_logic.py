import nltk
import re
v = """
 bertie => b
 olive => o
 cyril => c
 boy => {b}
 girl => {o}
 dog => {c}
 walk => {o, c}
 see => {(b, o), (c, b), (o, c)}
 """
val = nltk.parse_valuation(v)
print(val)



