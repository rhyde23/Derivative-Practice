#New Stab

import pygame, getProblems
from pygame import mixer

pygame.init()

window_size = 700
screen = pygame.display.set_mode((window_size, window_size))

pygame.display.set_caption("Practice Derivatives")

background = pygame.image.load("/Users/RHyde23/Desktop/MathProject/backgroundScreen.png")
background = pygame.transform.scale(background.convert(), (window_size, window_size))

red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 175, 0)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.font.init()
button_font = pygame.font.SysFont("Arial", 25)
button_font_smaller = pygame.font.SysFont("Arial", 13)

buttons = []


key_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "x", "+", "-", "2", "3", "4", "5", "6", "7", "8", "9", "/", "BACKSPACE", "<", ">"]
translators = {'²':"2", '³':"3", '⁴':"4", '⁵':"5", '⁶':"6", '⁷':"7", '⁸':"8", '⁹':"9"}
done = []
space_x = 20
current_x, current_y = 0, 500
current_added = 0

standard_width, standard_height = None, None

coefficients_texts = {}
coefficient_texts_widths = {}
coefficient_texts_strings = {}
coefficients_texts_greens = {}
coefficients_texts_reds = {}

exponents_texts = {}
exponents_texts_widths = {}
exponents_texts_strings = {}
exponents_texts_greens = {}
exponents_texts_reds = {}

current_texts = []
current_texts_greens = []
current_texts_reds = []
current_total_width_skips = []
current_string = ""

cursor_left = 0
cursor_left_gb = 0
cursor_left_gb_speed = 10
cursor_left_gb_change = cursor_left_gb_speed

message_value = 0

def resetMessage() :
    if message_value == 0 :
        message_text = button_font.render(message_string, False, black)
    elif message_value == 1 :
        message_text = button_font.render(message_string, False, green)
    else :
        message_text = button_font.render(message_string, False, red)
    message_width = message_text.get_width()
    message_x = int((window_size-message_width)/2)
    return message_text, message_width, message_x

for k_option in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "+", "-", "/", "(", ")", "*"] :
    text_generated = button_font.render(k_option, False, black)
    coefficients_texts[k_option] = text_generated
    coefficients_texts_greens[k_option] = button_font.render(k_option, False, green)
    coefficients_texts_reds[k_option] = button_font.render(k_option, False, red)
    coefficient_texts_widths[k_option] = text_generated.get_width()
    coefficient_texts_strings[k_option] = k_option

for kti, k_option2 in enumerate(["2", "3", "4", "5", "6", "7", "8", "9"]) :
    text_generated = button_font_smaller.render(k_option2, False, black)
    exponents_texts[k_option2] = text_generated
    exponents_texts_greens[k_option2] = button_font_smaller.render(k_option2, False, green)
    exponents_texts_reds[k_option2] = button_font_smaller.render(k_option2, False, red)
    exponents_texts_widths[k_option2] = text_generated.get_width()
    exponents_texts_strings[k_option2] = ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'][kti]

for en, key_option in enumerate(key_options) :
    if len(key_option) <= 2 :
        button_width, button_height = standard_width, standard_height
    else :
        button_width, button_height = 0, 0
    if not key_option in done :
        button_text = button_font.render(key_option, False, black)
        button_text_width, button_text_height = button_text.get_size()
        if standard_width == None :
            button_width, button_height = button_text_width+40, button_text_height+20
            standard_width, standard_height = button_width, button_height
    else :
        button_text = button_font_smaller.render("^"+key_option, False, black)
        button_text_width, button_text_height = button_text.get_size()

    if button_width == 0 :
        button_width, button_height = button_text_width+40, button_text_height+20

    current_x += space_x
    if current_x + button_width > window_size-20 :
        current_y = current_y + standard_height+20
        current_x = space_x
    
    buttons.append([current_x, current_y, button_width, button_height, white, (128,128,128), button_text, button_text_width, button_text_height])
    current_x += button_width
    
    done.append(key_option)

def display_button(button, x, y) :
    over = x >= button[0] and x <= button[0]+button[2] and y >= button[1] and y <= button[1]+button[3]
    text_ind = 6
    if over :
        color = button[5]
        if len(button) == 10 :
            text_ind = 9
    else :
        color = button[4]
    pygame.draw.rect(screen, color, button[:4])
    screen.blit(button[text_ind], (button[0]+int((button[2]-button[7])/2), button[1]+int((button[3]-button[8])/2)))
    return over

def display(current_string, current_texts, current_texts_greens, current_texts_reds, current_total_width_skips) :
    color = (cursor_left_gb, cursor_left_gb, cursor_left_gb)
    su = sum(current_total_width_skips)+(current_string.count("+")*16)+(current_string.count("-")*16)+(current_string.count("/")*48)
    disp_x = int((window_size-su)/2)
    disp_y = 362
    d = (len(current_string)-1-cursor_left)
    added = 0
    if d == -1 :
        pygame.draw.rect(screen, color, [disp_x, disp_y, 2, 25])
    for c_ind, current_text in enumerate(current_texts) :
        if message_value == 0 :
            screen.blit(current_text, (disp_x, disp_y))
        elif message_value == 1 :
            screen.blit(current_texts_greens[c_ind], (disp_x, disp_y))
        else :
            screen.blit(current_texts_reds[c_ind], (disp_x, disp_y))
        disp_x += current_total_width_skips[c_ind]
        if c_ind == d :
            pygame.draw.rect(screen, color, [disp_x, disp_y, 2, 25])
        try :
            if current_string[c_ind+1] in ["+", "-"] :
                disp_x += 8
                added += 8
            elif current_string[c_ind+1] == "/" :
                disp_x += 24
                added += 24
        except :
            pass
        if current_string[c_ind] in ["+", "-"] :
            disp_x += 8
            added += 8
        elif current_string[c_ind] == "/" :
            disp_x += 24
            added += 24
    return added


def validateTerm(term) :
    if term == "" :
        return False
    term_splitted = term.split("x")
    if term_splitted[0] != "" :
        try :
            x = int(term_splitted[0])
        except :
            return False
    if len(term_splitted) == 2 :
        for char in term_splitted[1] :
            if not char in ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'] :
                return False
    elif len(term_splitted) > 2 :
        return False
    return True

def validateString(s) :
    all_in = True
    for ch in s :
        if not ch in ["-", "+", "/"] :
            all_in = False
            break
    if all_in :
        return True, 0
    if s.count("/") > 1 :
        return False, 2
    spl = list(s)
    if spl[0] == "-" and spl[1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x"] :
        del spl[0]
    if "/" in spl :
        div_bar_ind = spl.index("/")
        try :
            if spl[div_bar_ind+1] == "-" and spl[div_bar_ind+2] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x"] :
                del spl[div_bar_ind+1]
        except :
            pass
    s = ''.join(spl)
    terms_splitted = s.split("+")
    all_terms = []
    for term_splitted in terms_splitted :
        all_terms = all_terms + term_splitted.split("-")
    all_terms2 = []
    for term_splitted in all_terms :
        all_terms2 = all_terms2 + term_splitted.split("/")
    for term in all_terms2 :
        func = validateTerm(term)
        if not validateTerm(term) :
            return False, 2
    return True, 1

def evaluateOne(char1, char2, ft) :
    if char1 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
        if char2 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x"] :
            return 0, False 
        if char2 in ["+", "-"] :
            return 8, False
        if char2 in ["*", "/"] :
            return 24, False
    if char1 == "x" :
        if char2 in ["+", "-"] :
            return 8, False
        if char2 in ["*", "/"] :
            return 24, False
        if char2 in ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'] :
            return 0, False
    if char1 in ["+", "-"] :
        if char1 == "-" and ft :
            return 0, True
        if char2 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x"] :
            return 8, False
    if char1 in ["*", "/"] :
        if char2 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x"] :
            return 24, False
        if char2 == "-" :
            return 24, False
    if char1 in ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'] :
        if char2 in ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'] :
            return 0, False
        if char2 in ["+", "-"] :
            return 8, False
        if char2 in ["*", "/"] :
            return 24, False
    
def generateQuestionText(question_string1, question_string2="", question_type=0, red=False) :
    question_string1 = question_string1.replace(" ", "")
    question_string2 = question_string2.replace(" ", "")
    if question_string2 == "" :
        question_string = question_string1
    else :
        if question_type == 2 :
            question_string = question_string1+"*"+question_string2
        else :
            question_string = question_string1+"/"+question_string2
    spaces = []
    first_term = True
    got_minus = False
    for i in range(len(question_string)-1) :
        funced = evaluateOne(question_string[i], question_string[i+1], first_term)
        if funced[1] :
            first_term = False
        spaces.append(funced[0])
        if question_string[i] in ["*", "/"] :
            first_term = True
            got_minus = False
        if question_string[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "+"] :
            first_term = False
        if question_string[i] == "-" and first_term :
            if not got_minus :
                got_minus = True
                first_term = True
            else :
                first_term = False
                
            
    question_texts = []
    question_xs = []
    qxs = 0
    for char_i in range(len(question_string)) :
        if question_string[char_i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "+", "-", "/", "*"] :
            question_xs.append(qxs)
            if red :
                question_texts.append(coefficients_texts_reds[question_string[char_i]])
            else :
                question_texts.append(coefficients_texts[question_string[char_i]])
            wi = coefficient_texts_widths[question_string[char_i]]
            qxs += wi
            try :
                qxs += spaces[char_i]
            except :
                pass
        else :
            question_xs.append(qxs)
            if red :
                question_texts.append(exponents_texts_reds[translators[question_string[char_i]]])
            else :
                question_texts.append(exponents_texts[translators[question_string[char_i]]])
            wi = exponents_texts_widths[translators[question_string[char_i]]]
            qxs += wi
            try :
                qxs += spaces[char_i]
            except :
                pass
    add_on = int((window_size-((question_xs[-1]+wi)-question_xs[0]))/2)
    return question_texts, [qx+add_on for qx in question_xs]

def getNewQuestionStuff() :
    while True :
        try :
            current_question = getProblems.randomizeProblem()
            if current_question[0] == 1 :
                question_texts, question_xs = generateQuestionText(getProblems.buildString(current_question[1]))
            else :
                question_texts, question_xs = generateQuestionText(getProblems.buildString(current_question[1]), question_string2=getProblems.buildString(current_question[2]), question_type=current_question[0])
                
            if current_question[0] == 3 :
                der = getProblems.solveForDertivative(current_question)
                current_answer_string = getProblems.buildString(der[0])+"/"+getProblems.buildString(der[1])
            else :
                current_answer_string = getProblems.buildString(getProblems.solveForDertivative(current_question))
            current_answer_string = current_answer_string.replace(" ", "")
            break
        except :
            pass
    #print(current_answer_string)
    return current_question, question_texts, question_xs, current_answer_string

current_question, question_texts, question_xs, current_answer_string = getNewQuestionStuff()

message_string = "Enter the derivative of the function."
message1_text = button_font.render("Enter the derivative.", False, black)
message1_width = message1_text.get_width()
message_x1 = int((window_size-message1_width)/2)

message2_text = button_font.render("Submit the derivative.", False, green)
message2_text2 = button_font.render("Submit the derivative.", False, white)
message2_width = message2_text.get_width()
message_x2 = int((window_size-message2_width)/2)

message3_text = button_font.render("Not a valid derivative.", False, red)
message3_width = message3_text.get_width()
message_x3 = int((window_size-message3_width)/2)

message4_text = button_font.render("Score: ", False, black)
message4_width = message4_text.get_width()
message_x4 = int((window_size-message4_width)/2)

message5_text = button_font.render("• For Quotient Rule problems, do not factor out anything.", False, black)
message5_width = message5_text.get_width()
message_x5 = int((window_size-message5_width)/2)

message6_text = button_font.render("• For Quotient Rule problems, \"/\" means the fraction bar.", False, black)
message6_width = message6_text.get_width()
message_x6 = int((window_size-message6_width)/2)

message7_text = button_font.render("Find the derivative of the expression:", False, black)
message7_width = message7_text.get_width()
message_x7 = int((window_size-message7_width)/2)

message8_text = button_font.render("Score: 0", False, black)
message8_width = message8_text.get_width()
message_x8 = int((window_size-message8_width)/2)

message9_text = button_font.render("Correct!", False, dark_green)
message9_width = message9_text.get_width()
message_x9 = int((window_size-message9_width)/2)

message10_text = button_font.render("The correct derivative was: ", False, red)
message10_width = message10_text.get_width()
message_x10 = int((window_size-message10_width)/2)

ten_question_texts, ten_question_texts_x = generateQuestionText(current_answer_string, red=True)
tq_state = 0

sco = 0

s1 = pygame.Surface((window_size-40,300))
s1.set_alpha(200)
s1.fill((255,255,255))

def update_eight(sco) :
    message8_text = button_font.render("Score: "+str(sco), False, black)
    message8_width = message8_text.get_width()
    message_x8 = int((window_size-message8_width)/2)
    return message8_text, message8_width, message_x8

top_messages = [message1_text, message2_text, message3_text]
top_messages_x = [message_x1, message_x2, message_x3]

sub = [int((window_size-350)/2), 425, 350, 50]
submit_button = [int((window_size-350)/2), 425, 350, 50, white, green, message2_text, message2_width, message2_text.get_height(), message2_text2]

over_submit = False


while True :
    screen.fill(white)
    screen.blit(background, (0, 0))
    x,y = pygame.mouse.get_pos()
    overs = None
    for button_ind, button in enumerate(buttons) :
        if display_button(button, x, y) :
            overs = button_ind
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            if over_submit :
                if current_string[-1] in ["+", "-", "/", "*"] :
                    current_string = current_string[:-1]
                if "*" in current_string :
                    two_parts = current_string.split("*")
                    splitter = "*"
                elif "/" in current_string :
                    two_parts = current_string.split("/")
                    splitter = "/"
                else :
                    two_parts = [current_string]
                if len(two_parts) == 1 :
                    current_string = getProblems.buildString(getProblems.combineLikeTerms(getProblems.splitUpString(two_parts[0])))
                else :
                    current_string = getProblems.buildString(getProblems.combineLikeTerms(getProblems.splitUpString(two_parts[0])))+splitter+getProblems.buildString(getProblems.combineLikeTerms(getProblems.splitUpString(two_parts[1])))
                current_string = current_string.replace(" ", "")
                if current_string == current_answer_string :
                    sco += 1
                    message8_text, message8_width, message_x8 = update_eight(sco)
                    tq_state = 2
                    mixer.music.load("correct.mp3")
                    mixer.music.play()
                else :
                    tq_state = 1
                    ten_question_texts, ten_question_texts_x = generateQuestionText(current_answer_string, red=True)
                    mixer.music.load("incorrect.mp3")
                    mixer.music.play()
                current_question, question_texts, question_xs, current_answer_string = getNewQuestionStuff()
                current_texts = []
                current_texts_greens = []
                current_texts_reds = []
                current_total_width_skips = []
                current_string = ""
                message_value = 0
                
            if overs != None :
                if overs <= 12 or overs == 21 :
                    if overs == 21 :
                        koo = "/"
                    else :
                        koo = key_options[overs] 
                    if sum(current_total_width_skips)+coefficient_texts_widths[koo]+current_added <= (window_size-40) :
                        new_c = coefficient_texts_strings[koo]
                        current_add_index = len(current_string)-cursor_left
                        splitted = list(current_string)
                        splitted.insert(current_add_index, new_c)
                        current_string = ''.join(splitted)
                        f = validateString(current_string)[1]
                        message_value = f
                        current_texts.insert(current_add_index, coefficients_texts[koo])
                        current_texts_greens.insert(current_add_index, coefficients_texts_greens[koo])
                        current_texts_reds.insert(current_add_index, coefficients_texts_reds[koo])
                        current_total_width_skips.insert(current_add_index, coefficient_texts_widths[koo])
                elif overs <= 20 :
                    if sum(current_total_width_skips)+exponents_texts_widths[key_options[overs]]+current_added <= (window_size-40) :
                        new_c = exponents_texts_strings[key_options[overs]]
                        current_add_index = len(current_string)-cursor_left
                        splitted = list(current_string)
                        splitted.insert(current_add_index, new_c)
                        current_string = ''.join(splitted)
                        f = validateString(current_string)[1]
                        message_value = f
                        current_texts.insert(current_add_index, exponents_texts[key_options[overs]])
                        current_texts_greens.insert(current_add_index, exponents_texts_greens[key_options[overs]])
                        current_texts_reds.insert(current_add_index, exponents_texts_reds[key_options[overs]])
                        current_total_width_skips.insert(current_add_index, exponents_texts_widths[key_options[overs]])
                elif overs in [23, 24] :
                    if overs == 23 :
                        cursor_left += 1
                        if cursor_left > len(current_string) :
                            cursor_left = len(current_string)
                    else :
                        cursor_left -= 1
                        if cursor_left < 0 :
                            cursor_left = 0
                elif overs == 22 :
                    if current_string != "" :
                        current_del_index = len(current_string)-(cursor_left+1)
                        if current_del_index >= 0 :
                            delete_splitted = list(current_string)
                            del delete_splitted[current_del_index]
                            current_string = ''.join(delete_splitted)
                            f = validateString(current_string)[1]
                            message_value = f
                            del current_texts[current_del_index]
                            del current_texts_greens[current_del_index]
                            del current_texts_reds[current_del_index]
                            del current_total_width_skips[current_del_index]
    pygame.draw.rect(screen, white, [20, 350, window_size-40, 50])
    if message_value == 1 :
        over_submit = display_button(submit_button, x, y)
    else :
        pygame.draw.rect(screen, white, sub)
        screen.blit(top_messages[message_value], (top_messages_x[message_value], 435))
        over_submit = False
    current_added = display(current_string, current_texts, current_texts_greens, current_texts_reds, current_total_width_skips)
    cursor_left_gb += cursor_left_gb_change
    if cursor_left_gb >= 255 :
        cursor_left_gb = 255
        cursor_left_gb_change = -cursor_left_gb_speed
    elif cursor_left_gb <= 0 :
        cursor_left_gb = 0
        cursor_left_gb_change = cursor_left_gb_speed
    screen.blit(s1, (20, 20))
    screen.blit(message7_text, (message_x7, 30))
    for indd in range(len(question_texts)) :
        screen.blit(question_texts[indd], (question_xs[indd], 70))
    if tq_state == 1 :
        for indd2 in range(len(ten_question_texts)) :
            screen.blit(ten_question_texts[indd2], (ten_question_texts_x[indd2], 280))
        screen.blit(message10_text, (message_x10, 240))
    elif tq_state == 2 :
        screen.blit(message9_text, (message_x9, 240))
    screen.blit(message6_text, (message_x6, 120))
    screen.blit(message5_text, (message_x5, 160))
    screen.blit(message8_text, (message_x8, 200))
    pygame.display.update()

