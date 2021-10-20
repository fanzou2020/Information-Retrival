import nltk
import json
import argparse
import sys


def tokenizer(articles:list):
    """
    tokenize
    :param articles
    :return: list of tuple (token, file_id)
    """
    tokens = []
    for i, article in enumerate(articles):
        file_id = i+1
        tokens_in_one_article = nltk.word_tokenize(article)
        for token in tokens_in_one_article:
            tokens.append((token, file_id))
    return tokens


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # '-o' or '--output' output to a file
    parser.add_argument("-o", "--output", help="write output to a file", type=str)

    # '-i' or '--input' input from file
    parser.add_argument("-i", "--input", help="input from a file", type=str)

    args = parser.parse_args()

    articles = []

    if args.input:
        with open(args.input, "r") as f:
            articles = json.load(f)
    else:
        all_str = input()
        articles = json.loads(all_str)

    tokens = tokenizer(articles)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(tokens, f)
    else:
        str_print = json.dumps(tokens)
        print(str_print)

