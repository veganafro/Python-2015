#This program analyzes a set of parentheses and determines if they are balanced.

def balanced_parentheses(string):
    parentheses = []
    for items in string:
        if items == "(":
            parentheses.append(items)
        elif items == ")" and len(parentheses) > 0:
            parentheses.pop()
        else:
            return False
    if "(" in parentheses:
        return False
    else:
        return True

assert True == balanced_parentheses('(()()()())')
assert True == balanced_parentheses('(((())))')
assert True == balanced_parentheses('(()((())()))')

assert False == balanced_parentheses(')(')
assert False == balanced_parentheses('((((((())')
assert False == balanced_parentheses('()))')
assert False == balanced_parentheses('((((((())')
assert False == balanced_parentheses(')(()')
assert False == balanced_parentheses('())(')
