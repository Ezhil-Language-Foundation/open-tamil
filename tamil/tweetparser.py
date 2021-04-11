# This Python file uses the following encoding: utf-8
# (C) 2013-2016 Muthiah Annamalai
#
# This file is now part of open-tamil project
#
# N.B.: Originally written to demo the Python Twitter API for a lightning talk
# at the Boston Python group on 30th July, 2013.

import unicodedata
import re


class TweetParser:
    def __init__(self, timeline_owner, tweet):
        self.Owner = timeline_owner
        self.tweet = tweet
        self.RT = False
        self.tweet = tweet
        self.UserHandles = TweetParser.getUserHandles(tweet)
        self.Hashtags = TweetParser.getHashtags(tweet)
        self.URLs = TweetParser.getURLs(tweet)
        self.RT = TweetParser.getAttributeRT(tweet)
        self.MT = TweetParser.getAttributeMT(tweet)

        # additional intelligence
        if (self.RT
                and len(self.UserHandles) > 0):  # change the owner of tweet?
            self.Owner = self.UserHandles[0]

        return

    def __str__(self):
        return "owner %s, urls: %d, hashtags %d, user_handles %d, len_tweet %d, RT = %s, MT = %s" % (
            self.Owner, len(self.URLs), len(self.Hashtags),
            len(self.UserHandles), len(self.tweet), self.RT, self.MT)

    @staticmethod
    def getAttributeRT(tweet):
        """ see if tweet is a RT """
        return re.search(r'^RT', tweet.strip()) != None

    @staticmethod
    def getAttributeMT(tweet):
        """ see if tweet is a MT """
        return re.search(r'^MT', tweet.strip()) != None

    @staticmethod
    def getUserHandles(tweet):
        """ given a tweet we try and extract all user handles in order of occurrence"""
        return re.findall(r'(@[a-zA-Z0-9_]+)', tweet)

    @staticmethod
    def getHashtags(tweet):
        """ return all hashtags"""
        return re.findall(r'(#[\w\d]+)', tweet)

    @staticmethod
    def getURLs(tweet):
        """ URL : [http://]?[\w\.?/]+"""
        return re.findall(r'([http://]?[a-zA-Z\d\/]+[\.]+[a-zA-Z\d\/\.]+)',
                          tweet)


class TamilTweetParser(TweetParser):
    def __init__(self, timeline_owner, tweet):
        TweetParser.__init__(self, timeline_owner, tweet)
        self.TAWords = TamilTweetParser.getTamilWords(tweet)
        return

    def __str__(self):
        """ tack on the parent """
        return TweetParser.__str__(self) + ", TA words = %d " % len(
            self.TAWords)

    @staticmethod
    def isTamilPredicate(word):
        """ is Tamil word : boolean True/False"""
        for c in word:
            if unicodedata.name(c).split()[0] != u'TAMIL':
                return False
        return True

    @staticmethod
    def cleanupPunct(tweet):
        """ NonEnglishOrTamilOr """
        tweet = ''.join(
            map(
                lambda c: (unicodedata.name(c).split()[0] in
                           [u'TAMIL', u'LATIN']) and c or u' ', tweet))
        return tweet

    @staticmethod
    def getTamilWords(tweet):
        """" word needs to all be in the same tamil language """
        tweet = TamilTweetParser.cleanupPunct(tweet)
        nonETwords = filter(lambda x: len(x) > 0, re.split(r'\s+', tweet))
        # |"+|\'+|#+
        tamilWords = filter(TamilTweetParser.isTamilPredicate, nonETwords)
        return tamilWords
