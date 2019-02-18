from RedisConfig import *

VOTE_SCORE = 432
class Article:

    @staticmethod
    def createArticleGroup():
        redis, isConnected = connect()
        if isConnected:
            groupStr = raw_input("Enter The group: ")
            if not redis.exists(groupStr):
                while 1:
                    articleId = raw_input("Enter the article id: ")
                    article = "article:" + articleId
                    redis.sadd('group:' + groupStr, article)
                    if(raw_input("Add another article to the" + groupStr + " group? y/n: ") == 'n'):
                        break
            else:
                print "The Group already exists"
            

    @staticmethod
    def createArticle():
        redis, isConnected = connect()
        if isConnected:
            articleId = str(redis.incr('article:'))
            title = raw_input("Enter the title: ")       
            description = raw_input("Enter the description: ")
            articleKey = "article:" + articleId
            redis.hmset(articleKey, {
                'title': title,
                'description': description,
                'votes': 1
            })
            redis.zadd("score:", {articleKey: VOTE_SCORE})
            print "Article " + articleId + " Added Succesfully"

    @staticmethod
    def readArticle():
        redis, isConnected = connect()
        if isConnected:
            articleId = raw_input("Enter the key for the article: ")
            article = 'article:' + articleId
            if redis.hexists(article, "title") and redis.hexists(article, "description") and redis.hexists(article, "votes"):
                print "Title: " + redis.hget(article, "title")
                print "Description: "  + redis.hget(article, "description")
                print "Votes: " + redis.hget(article, "votes")
            else:
                print "The specified Article doesn't exists"


    @staticmethod
    def deleteArticle():
        redis, isConnected = connect()
        if isConnected:
            articleId = raw_input("Enter the article id to delete: ")
            article = 'article:' + articleId
            if redis.hexists(article, "title") and redis.hexists(article, "description"):
                if (redis.hdel(article, "title") == 1) and (redis.hdel(article, "description") == 1) and (redis.hdel(article, "votes") == 1):
                    if redis.zrem('score:', article):
                        pass
                    redis.delete(article)
                    print "Article Deleted Succesfully"
                else:
                    print "Something went wrong"
            else:
                print "The specified Article doesn't exists"

    @staticmethod
    def articlesFromGroup():
        redis, isConnected = connect()
        if isConnected:
            groupStr = raw_input("Enter the group: ")
            group = "group:" + groupStr
            if redis.exists(group):
                for article in redis.smembers(group):
                    if redis.hexists(article, "title") and redis.hexists(article, "description") and redis.hexists(article, "votes"):
                        print "\n"
                        print "Title: " + redis.hget(article, "title")
                        print "Description: "  + redis.hget(article, "description")
                        print "-----------------------------------"
                        print "\n"
            else:
                print "The Group doesn't exists"

    @staticmethod
    def addVote():
        redis, isConnected = connect()
        if isConnected:
            articleId = raw_input("Enter the id of the article: ")
            article = "article:" + articleId
            if redis.hexists(article, "title") and redis.hexists(article, "description") and redis.hexists(article, "votes"):
                redis.zincrby('score:', float(VOTE_SCORE), article)
                redis.hincrby(article, 'votes', 1)
                print "Vote Addded"
            else:
                print "The Article specified doesn't exists"

    @staticmethod
    def articlesRanking():
        redis, isConnected = connect()
        if isConnected:
            articles = redis.zrevrange("score:", 0, -1)
            for article in articles:
                if redis.hexists(article, "title") and redis.hexists(article, "description") and redis.hexists(article, "votes"):
                    print "Title: " + redis.hget(article, "title")
                    print "Description: "  + redis.hget(article, "description")
                    print "Votes: " + redis.hget(article, "votes")
                    print "-----------------------------------" 
                else:
                    print "The Article specified doesn't exists"


    

        