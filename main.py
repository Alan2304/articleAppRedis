import redis as rd
from article import *

def createArticle():
    Article.createArticle()

def createArticleGroup():
    Article.createArticleGroup()

def voteArticle():
    Article.addVote()

def deleteArticle():
    Article.deleteArticle()

def readArticle():
    Article.readArticle()

def articleRanking():
    Article.articlesRanking()

def articlesFromGroup():
    Article.articlesFromGroup()

def main():
    while 1:
        print "1.- Create Articles Groups\n2.- Create a Article\n3.-Vote for an Article\n4.-Delete an Article\n5.-Read a Article\n6.-See Articles ranking\n7.- Get Articles from a group\n8.-Exit"
        option = input('Choose a option: ')
        if option == 8:
            print("Exit program")
            exit()

        switcher = {
            1: createArticleGroup,
            2: createArticle,
            3: voteArticle,
            4: deleteArticle,
            5: readArticle,
            6: articleRanking,
            7: articlesFromGroup
        }

        operation = switcher.get(option, lambda: "Invalid Operation")
        operation()

main()