#!/usr/bin/env python

from .indic_tokenizer import IndicTokenizer
from .roman_tokenizer import RomanTokenizer
from .cyrillic_tokenizer import CyrillicTokenizer
from .armenian_tokenizer import ArmenianTokenizer


class Tokenizer():
    def __init__(self, lang='en', split_sen=False,
                 smt=False, from_file=False):
        self.from_file = from_file
        self.split_sen = split_sen
        if lang in 'hi ur bn as gu ml pa te ta kn or mr ne bo kok ks'.split():
            self.tok = IndicTokenizer(lang=lang, split_sen=split_sen,
                                      smt=smt)
        elif lang in 'be '.split():
            self.tok = CyrillicTokenizer(lang=lang, split_sen=split_sen,
                                      smt=smt)
        elif lang in 'hy  '.split():
            self.tok = ArmenianTokenizer(lang=lang, split_sen=split_sen,
                                      smt=smt)
        else:
            self.tok = RomanTokenizer(lang=lang, split_sen=split_sen,
                                      smt=smt)

    def tokenize(self, sentence):
        if self.from_file or not self.split_sen:
            return self.tok.tokenize(sentence)
        else:
            out_sents = []
            sentences = sentence.split('\n')
            for sent in sentences:
                tok_sent = self.tok.tokenize(sent)
                out_sents.extend(tok_sent)
            return out_sents
