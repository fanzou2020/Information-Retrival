import nltk
import json
import argparse
import glob  # filter files with regx pattern


def tokenizer(articles: list):
    """
    :param articles: list of articles
    :return: list of tokens
    """
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    tokens = []
    for article in articles:
        tokens_in_one_article = tokenizer.tokenize(article["body"])
        for token in tokens_in_one_article:
            tokens.append((token, article["ID"]))
    return tokens


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # '-o' or '--output' output to file
    parser.add_argument("-o", "--output", help="write output to files", type=str)

    parser.add_argument("-i", "--input", help="input from files", type=str)

    args = parser.parse_args()

    all_articles = []  # list of list, each inner list contains articles from one sgm file

    # read from files
    if args.input:
        input_files = glob.glob(args.input)
        input_files.sort()
        for file_name in input_files:
            with open(file_name, "r") as fi:
                all_articles.append(json.load(fi))

    # read from stdin
    else:
        input_str = input()
        all_articles = json.loads(input_str)

    # perform tokenization
    result = []  # [ [("a",1)..., ("b", 2)...], [ ... ]  ]
    for articles_in_one_file in all_articles:
        tokens = tokenizer(articles_in_one_file)
        result.append(tokens)

    # output to file
    if args.output:
        for i, tokens_in_one_file in enumerate(result):
            output_file = args.output.replace("*", str(i))
            with open(output_file, "w") as fo:
                json.dump(tokens_in_one_file, fo)

    # output to stdout
    else:
        print(json.dumps(result))

