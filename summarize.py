
from unittest import result
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

from pysummarization.nlp_base import NlpBase
from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine

#mecab自体を上手く使えてない、同じエラーでやられてる
#文字数が長すぎるとNon-UTF-8 code starting with '\xe3'というエラーが起こってしまうので文章を分けて読み込む仕組みが必要


#要約を行う関数
def summa(document):

    # NLPのオブジェクト
    nlp_base = NlpBase()

    # トークナイザーを設定します。 これは、MeCabを使用した日本語のトークナイザーです
    nlp_base.tokenizable_doc = MeCabTokenizer()

    # 「類似性フィルター」のオブジェクト。 このオブジェクトによって観察される類似性は、Tf-Idfベクトルのいわゆるコサイン類似性です
    similarity_filter = TfIdfCosine()

    # NLPのオブジェクトを設定します
    similarity_filter.nlp_base = nlp_base

    # 類似性がこの値を超えると、文は切り捨てられます
    similarity_filter.similarity_limit = 0.5

    auto_abstractor = AutoAbstractor()

    # トークナイザーを設定します。 これは、MeCabを使用した日本語のトークナイザーです
    auto_abstractor.tokenizable_doc = MeCabTokenizer()

    # 文の切れ目で使われる文字を設定します。    
    auto_abstractor.delimiter_list = ['．', '。', '\n']

    # ドキュメントを抽象化およびフィルタリングするオブジェクト
    abstractable_doc = TopNRankAbstractor()

    # オブジェクトを委任し、要約を実行します
    # similarity_filter機能追加
    result_dict = auto_abstractor.summarize(document, abstractable_doc, similarity_filter)

    return result_dict["summarize_result"]
