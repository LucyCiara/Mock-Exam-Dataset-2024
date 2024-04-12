from ast import literal_eval
string = "1, 2, 3"
print(f"listifying '1, 2, 3': {list(string)}")
string = "[1, 2, 3]"
print(f"listifying '[1, 2, 3]': {list(string)}")

print()
print(f"using a secure form of eval on a harmless variable: {eval(string, {}, {})}")
badString = "string"
print(f"using insecure form of eval on harmful variable: {eval(badString)}")
try:
    print(f"using secure form of eval on harmful variable: {eval(badString, {}, {})}")
except:
    print("using secure form of eval on harmful variable (doesn't work)")

# eval("sum([1, 2, 3])", {"__builtins__": {}}, {}) er litt sikkrere igjen, men ikke helt

print()
print(f"literal_eval på grei string: {literal_eval("[1, 2, 3]")}")
try:
    print(f"literal_eval på ugrei string: {literal_eval("sum([1, 2, 3])")}")
except:
    print("literal_eval på ugrei string (går ikke)")
