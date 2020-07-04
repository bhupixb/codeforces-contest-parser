#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import os       # to create folder & files and copy input & output samples
import sys      # to obtain the name of contest from command line arg
import shutil   # to remove a folder and it's contents

BASE_URL = "https://codeforces.com/contest"

def extract_test_case(contestNum, problem_numb):
    # print(contestNum, problem_numb)
    problemPageUrl = f"{BASE_URL}/{contestNum}/problem/{problem_numb}"
    print(f"parsing {problem_numb}")
    page = requests.get(problemPageUrl)
    soup = BeautifulSoup(page.text, 'html.parser')
    sampleTests = soup.find(class_='sample-test')
    inputsElement = sampleTests.find_all(class_='input')
    inputList = [elem.find('pre').text for elem in inputsElement]
    outputsElement = sampleTests.find_all(class_='output')
    outputList = [elem.find('pre').text for elem in outputsElement]
    outputList = [item[1:] for item in outputList] #to remove \n at the start
    inputList = [item[1:] for item in inputList]
    # print(inputList, outputList)
    return(inputList,outputList)

def getProblemCount(contestNum):
    contestPageUrl = f"{BASE_URL}/{contestNum}"
    page = requests.get(contestPageUrl)
    if not page:
        print('url seems incorrect, maybe please try again')
        exit()

    soup = BeautifulSoup(page.content, 'html.parser')
    store = soup.find_all(class_ = 'problems')
    store = store[0]
    ok = store.find_all(class_ = 'id')

    problem_names = [] # a list to hold all the problem names
    for item in ok:
        p_name = item.find('a').text.strip() # .strip to remove leading or trailing spaces
        problem_names.append(p_name)

    return problem_names

def main(contestNumber, problem_num_specified):
    problem_names = []
    quesCount = 0
    if problem_num_specified:
        problem_names.append(problem_num_specified)
    else:
        problem_names = getProblemCount(contestNumber)
        quesCount = len(problem_names)
    current_dir = (os.getcwd())
    folderName = os.path.join(current_dir,contestNumber)
    print(f"total questions: {len(problem_names)},", end = ' ')
    for p in problem_names:
        print(p, end = ' ')
    print('')
    if not os.path.exists(folderName):        
        os.mkdir(folderName)

    for problem_num in problem_names:
        try:
            inputs, outputs = extract_test_case(contestNumber, problem_num)
            numOfInputs = len(inputs)
            problemFolder = os.path.join(current_dir, contestNumber, problem_num)
            if not os.path.exists(problemFolder):
                os.mkdir(problemFolder)
            for inp in range(numOfInputs):
                with open(f'{problemFolder}/in{inp}','w') as f:
                    f.write(inputs[inp])
                with open(f'{problemFolder}/out{inp}','w') as f:
                    f.write(outputs[inp])
        except:
            print(f"no inputs in {problem_num}")
    print(f"\nParsed successfully. Wish you all the best!!!")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        l = input('Enter contest name: ')
        l = l.split(' ')
        contest_number = l[0]
        problem_num = None
        if (len(l) > 1):
            problem_num = l[1]
        main(contest_number, problem_num)
    else:
        contest_number = sys.argv[1]
        problem_num = None
        if len(sys.argv) > 2:
            problem_num = sys.argv[2]
        main(contest_number, problem_num)
