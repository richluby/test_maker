#!/usr/bin/python

import os
import random

while os.path.isfile('test_q.txt') == True:
    questions = []
    with open('test_q.txt','r') as f:
        for line in f:
            if line.startswith('["'):
                s = line.lstrip('\"\'["').rstrip('\n\"]\'\"').split('", \'')
            elif line.startswith('[\''):
                s = line.lstrip('\"\'["').rstrip('\n\"]\'\"').split('\', \'')
            questions.append(s)
        break
else:
    questions = [['What is the color of the sky?','blue'],['What is the answer to the universe?','42']]

def random_distractors(answer):
    randQuesL = []
    randAnswL = [answer]
    newL = []
    index = 0
    numQuestions = len(questions)
    while index < numQuestions:
        randQuesL.append(questions[index][1])
        index += 1

    while len(randAnswL) < 4 and len(randAnswL) != numQuestions:
        # handle the case when there are fewer than four questions
        a = random.choice(randQuesL)
        randS = set(randAnswL)
        randS.add(a)
        randAnswL = list(randS)

    index = 0

    while index < 4 and index != numQuestions:
        dist = random.choice(randAnswL)
        randS = set(randAnswL)
        randS.remove(dist)
        randAnswL = list(randS)
        multiSel = chr(65 + index)
        print '{} {}'.format(multiSel,dist)
        if multiSel == 'A':
            A = dist
        elif multiSel == 'B':
            B = dist
        elif multiSel == 'C':
            C = dist
        else:
            D = dist
        index += 1

    usersInput = raw_input('>>> ')
    if userInput == 'A':
        return A
    if userInput == 'B':
        return B
    if userInput == 'C':
        return C
    if userInput == 'D':
        return D

def check_question(question_and_answer):
    question = question_and_answer[0]
    answer = question_and_answer[1]
    print 'Question', question + '\n'
    given_answer = random_distractors(answer)
    if answer == given_answer:
        print 'Correct'
        return True
    else:
        print 'Incorrect, correct was:"', answer
        return False

def add_question():
    q = 0
    while len(questions) == 0 or q < len(questions):
        choice = raw_input('Would you like to input a question? (y or n): ')
        if choice == 'y':
            new_question = []
            ask_question = raw_input('Please add question: ')
            new_question.append(ask_question)
            give_answer = raw_input('Please provide answer: ')
            new_question.append(give_answer)
            questions.append(new_question)
            q += 1
            get_questions(questions)
            continue
        if choice == 'n':
            break

def remove_question():
    q = 0
    index = 1
    blank = ' '
    while q < len(questions):
        a = 0
        print "{} Q:".format(index) , questions[q][a]
        a = 1
        if index < 10:
            print "{} A:".format(blank) , questions[q][a]
        else:
            print "{}  A:".format(blank) , questions[q][a]
        print "\n"
        q += 1
        index += 1
    choice = int(raw_input("Input the number of the Q:A you wish to delete or input 0 to exit: "))
    q = 0
    index = 1
    while q < len(questions):
        if choice != 0:
            if index == choice:
                print 'The Q:A %r' % questions[q] + ' has been deleted.'
                del questions[q]
                if os.path.isfile('test_q.txt') == True:
                    with open('test_q.txt','w') as f:
                        for line in questions:
                            f.write('%s\n'%line)
                        print 'File Updated'
                        break
            index += 1
            q += 1
        else:
            main()

def showQuestions():
    q = 0
    index = 1
    blank = ' '
    while q < len(questions):
        a = 0
        print "{} Q:".format(index) , questions[q][a]
        a = 1
        if index < 10:
            print "{} A:".format(blank) , questions[q][a]
        else:
            print "{}  A:".format(blank) , questions[q][a]
        print "\n"
        q += 1
        index += 1

def run_test(questions):
    if len(questions) == 0:
        print 'No questions were given.'
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_question(questions[index]):
            right += 1
        index += 1
        print 'You got', right * 100 / len(questions),'% right out of', len(questions)

def get_questions(x):
    if os.path.isfile('test_q.txt') == True:
        n = 0
        with open('test_q.txt','w') as f:
            for line in x:
                f.write('%s\n'%line)
        print 'File Updated'
    elif os.path.isfile('test_q.txt') == False:
        n = 0
        print 'File started'
        with open('test_q.txt','w') as f:
            for line in questions:
                f.write('%s\n'%line)

def menu():
    print '-' * 25
    print 'Menu: '
    print '1 - Take the test'
    print '2 - View a list of questions and answers'
    print '3 - View the menu'
    print '4 - Add Question'
    print '5 - Remove Question'
    print '6 - Quit'
    print '-' * 25

def main():
##    random_distractors('blue')
    choice = '3'
    while choice != '6':
        if choice == '1':
            run_test(questions)
            menu()
        elif choice == '2':
            showQuestions()
            menu()
        elif choice == '3':
            menu()
        elif choice == '4':
            add_question()
            menu()
        elif choice == '5':
            remove_question()
        print '\n'
        choice = raw_input('Choose your option from the menu above: ')
        print '\n'

if __name__ == '__main__':
    main()
