import re
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def url_finder(href):
    return href and re.compile('status').search(href)

def solution_finder(href):
    return href and re.compile('viewsolution').search(href)

def title_finder(href):
    return href and re.compile('problems').search(href)

def solution_getter(submission_ext,title):

    code_url = Request("https://www.codechef.com" + submission_ext, headers={'User-Agent': 'Mozilla/5.0'})
    source_code = urlopen(code_url).read()
    soup = BeautifulSoup(source_code, "html.parser")
    tag = soup.ol
    #print(tag)

    file = open(title + '.txt', 'w')
    file.write(title)
    file.write('\n\n')

    for submission in tag.findAll('li'):
        file.write(submission.text)
        file.write('\n')
        #print(submission.text)

    file.close()


def submission_crawler(submission_ext):

    solution_url = Request("https://www.codechef.com" + submission_ext, headers={'User-Agent': 'Mozilla/5.0'})
    source_code = urlopen(solution_url).read()
    soup = BeautifulSoup(source_code, "html.parser")
    tag = soup.body
    #file = open('sub_links.txt','w')

    x = 0
    for submission in tag.findAll(href=title_finder):
        x += 1
        # file.write(submission.text)
        # file.write('\n')
        if x is 10:
            print(submission.text)
            title = submission.text
            break



    for solution in tag.findAll(href=solution_finder):
        #solution_getter(solution.get('href'))
        solution_ext =  solution.get('href')
        #print(solution_ext)
        solution_getter(solution_ext, title)



def codechef_crawler(username):

    account_url = Request("https://www.codechef.com/users/" + username, headers={'User-Agent': 'Mozilla/5.0'})
    source_code = urlopen(account_url).read()
    soup = BeautifulSoup(source_code,"html.parser")
    tag = soup.body

    for submission in tag.findAll(href=url_finder):
        #print(submission.get('href'))
        submission_crawler(submission.get('href'))


#def crawler(username):
#   account_url = "https://www.codechef.com" + username
#    source_code = requests.get(account_url)
#    plain_text = source_code.text
#    soup = BeautifulSoup(plain_text, "html.parser")
#    tag = soup.body





#crawler('/viewsolution/9833640')
#submission_crawler('/status/TEST,shubhanshusv')
#solution_getter('/viewsolution/9833640')
a = input()
codechef_crawler(a)


