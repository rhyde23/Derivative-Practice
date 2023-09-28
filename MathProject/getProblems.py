import random, itertools

exponents = ['', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def get_coefficient(x) :
    if x == 1 :
        return ''
    else :
        return str(x)


def combineLikeTerms(terms) :
    like_terms = [[], [], [], [], [], [], [], [], [], []]
    for term in terms :
        if len(term) == 1 :
            like_terms[0].append(term[0])
        else :
            like_terms[term[1]].append(term[0])
    new_terms = [[sum(like_terms[0])]]
    for index in range(len(like_terms[1:])) :
        if like_terms[index+1] != [] :
            new_terms.append([sum(like_terms[index+1]), index+1])
    return [nt for nt in new_terms[::-1] if nt[0] != 0]

def buildString(terms) :
    s = ""
    for e in range(len(terms)) :
        if terms[e][0] < 0 :
            s = s + '-'
        else :
            s = s + '+'
        if len(terms[e]) == 2 :
            s = s + get_coefficient(abs(terms[e][0]))+"x"+exponents[terms[e][1]-1]
        else :
            s = s + str(abs(terms[e][0]))
    if s[0] == '+' :
        s = s[1:]
    s = s.replace('-', ' - ').replace('+', ' + ')
    if s[:3] == ' - ' :
        s = s[3:]
        s = '-'+s
    if s[-1] == ' ' :
        s = s[:-1]
    return s

def generateRandom(lower, upper) :
    while True :
        n = random.randint(lower, upper)
        if n != 0 :
            return n
        
def randomizeEquation() :
    half_chance = random.randint(1, 100)
    num = 0
    if half_chance < 50 :
        num = generateRandom(-10, 10)
    terms = []
    choices = [1, 2]
    for i in range(random.randint(1, 2)) :
        c = random.choice(choices)
        choices.remove(c)
        terms.append([generateRandom(-3, 3), c])
    if num != 0 :
        terms = terms + [[num]]
    random.shuffle(terms)
    return terms

def randomizeProblem() :
    randChoice = random.randint(1, 3)
    if randChoice == 1 :
        return [randChoice, combineLikeTerms(randomizeEquation())]
    else :
        return [randChoice, combineLikeTerms(randomizeEquation()), combineLikeTerms(randomizeEquation())]

def getDerivative(terms) :
    new_terms = []
    for inde in range(len(terms)) :
        if len(terms[inde]) != 1 :
            second_term = terms[inde][1]-1
            if second_term == 0 :
                new_terms.append([terms[inde][0]*terms[inde][1]])
            else :
                new_terms.append([terms[inde][0]*terms[inde][1], second_term])
    return new_terms

def multiplyTwoTerms(t1, t2) :
    one_coe, two_coe = t1[0], t2[0]
    if len(t1) == 1 :
        one_exp = 0
    else :
        one_exp = t1[1]
    if len(t2) == 1 :
        two_exp = 0
    else :
        two_exp = t2[1]
    total_coe = one_coe*two_coe
    total_exp = one_exp+two_exp
    if total_exp == 0 :
        return [total_coe]
    return [total_coe, total_exp]


def multiplyExpressions(terms1, terms2) :
    new_set_of_terms = []
    for term1 in terms1 :
        for term2 in terms2 :
            new_set_of_terms.append(multiplyTwoTerms(term1, term2))
    return combineLikeTerms(new_set_of_terms)

def changeToNegative(tee) :
    if len(tee) == 1 :
        return [-tee[0]]
    return [-tee[0], tee[1]]

def solveForDertivative(full_problem) :
    if full_problem[0] == 1 :
        return combineLikeTerms(getDerivative(full_problem[1]))
    elif full_problem[0] == 2 :
        return combineLikeTerms(multiplyExpressions(full_problem[1], getDerivative(full_problem[2]))+multiplyExpressions(full_problem[2], getDerivative(full_problem[1])))
    elif full_problem[0] == 3 :
        return combineLikeTerms(multiplyExpressions(full_problem[2], getDerivative(full_problem[1]))+[changeToNegative(t) for t in multiplyExpressions(full_problem[1], getDerivative(full_problem[2]))]), multiplyExpressions(full_problem[2], full_problem[2])
 
def splitUpString(string) :
    first_neg = string[0] == "-"
    if first_neg :
        string = string[1:]
    found_all = [cha for cha in string if cha in ["+", "-"]]
    ter = []
    for spli in string.split("+") :
        ter = ter + spli.split("-")
    new_ter = []
    for tei, te in enumerate(ter) :
        if "x" in te :
            x_spli = te.split("x")
            try :
                inte = int(x_spli[0])
            except :
                inte = 1
            multi = 1
            if tei != 0 :
                if found_all[tei-1] == '-' :
                    multi = -1
            new_ter.append([multi*inte, exponents.index(x_spli[1])+1])
        else :
            multi = 1
            if tei != 0 :
                if found_all[tei-1] == '-' :
                    multi = -1
            new_ter.append([multi*int(te)])
    if first_neg :
        new_ter[0][0] = -new_ter[0][0]
    return new_ter


"""
for t in range(10) :
    problem = randomizeProblem()
    if problem[0] == 2 :
        print("func1: ", buildString(problem[1]))
        print()
        print("func2: ", buildString(problem[2]))
        print()
        print("solved: ", buildString(solveForDertivative(problem)))
        quit()
"""

"""
print()
print()
print()
fake_terms = [[683], [2, 5], [5, 1], [-6, 5]]
ter = combineLikeTerms(fake_terms)
print(buildString(ter))
print()
ter_de = getDerivative(ter)
print(buildString(ter_de))
"""

"""
prob1 = randomizeProblem()
prob2 = randomizeProblem()
print(buildString(prob1[1]))
print()
print(buildString(prob2[1]))
print()
print(buildString(multiplyExpressions(prob1[1], prob2[1])))
"""

