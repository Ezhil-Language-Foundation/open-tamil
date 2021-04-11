#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import re
import tamil


# This file was originally part of  'TamilNLP' repackaged for Open-Tamil.
# [தமிழ் உரை சுருக்கம் செய்யும் நிரல்](https://github.com/AshokR/TamilNLP/wiki/Text-Summary-Extractor)
# Copyright © 2016 இரா. அசோகன்
# Licensed under the Apache License, Version 2.0 (the "License");
# This is a naive text summarization algorithm created by Shlomi Babluki
# Copyright (C) 2013 Shlomi Babluki
#
# http://thetokenizer.com/2013/04/28/build-your-own-summary-tool/
# https://gist.github.com/shlomibabluki/5473521
#
# Copyright (C) 2016 Muthu Annamalai


class SummaryTool(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):

        # split the sentence into words/tokens
        # s1 = set(sent1.split(" "))
        # s2 = set(sent2.split(" "))
        s1 = set(tamil.utf8.get_letters(sent1))
        s2 = set(tamil.utf8.get_letters(sent2))

        # If there is not intersection, just return 0
        # if (len(s1) + len(s2)) == 0:
        if len(s1.intersection(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2.0)

    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        # sentence = re.sub(r'\W+', '', sentence)       # [\u0B80-\u0BFF]
        sentence = re.sub(r"\s+", "", sentence)
        sentence = re.sub(r"\d+", "", sentence)
        # print sentence
        return sentence

    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_sentences_ranks(self, content):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                # Metric for intersection is symmetric so we calculate 1/2 only
                # For additional metrics see: ngram.Distance module in open-tamil
                # Ref https://github.com/Ezhil-Language-Foundation/open-tamil/blob/master/ngram/Distance.py
                if i >= j:
                    values[i][j] = values[j][i]
                    continue
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            kw = self.format_sentence(sentences[i])
            if len(kw) != 0:
                sentences_dic[kw] = score

        return sentences_dic

    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence

    # Build the summary
    def get_summary(self, title, content, sentences_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)
