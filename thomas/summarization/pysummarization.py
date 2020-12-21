# !pip install pysummarization

from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import sys

document = ""
f = open("test.txt", "r")
for x in f:
  document += x

print("read {0} bytes".format(len(document)))

# Object of automatic summarization.
auto_abstractor = AutoAbstractor()
# Set tokenizer.
auto_abstractor.tokenizable_doc = SimpleTokenizer()
# Set delimiter for making a list of sentence.
auto_abstractor.delimiter_list = [".", "\n"]
# Object of abstracting and filtering document.
abstractable_doc = TopNRankAbstractor()
abstractable_doc.set_top_n(2)
# Summarize document.
result_dict = auto_abstractor.summarize(document, abstractable_doc)

print("loremIpsum abstract:")

# Output result.
for sentence in result_dict["summarize_result"]:
    print(sentence.strip())