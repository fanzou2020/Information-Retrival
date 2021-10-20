import os
import re
import argparse
import json


def read_articles(file_path):
    """
    Read articles in one file
    :param file_path: path of a file
    :return: list of Article objects
    """
    with open(file_path, "r", encoding="unicode_escape") as f:
        raw_content = f.read()
        articles = parse_article(raw_content)
    return articles


def parse_article(content):
    """
    :param content: raw content in one file
    :return: list of Article objects
    """
    re_parse_reuter = re.compile(r"(<REUTERS.*>[\s\S]*?</REUTERS>)")
    re_parse_id = re.compile(r"NEWID=\"([0-9]*)\"")
    re_parse_title = re.compile(r"<TITLE>([\s\S]*?)</TITLE>")
    re_parse_body = re.compile(r"<BODY>([\s\S]*?)</BODY>")

    articles = []
    reuter_items_in_one_file = re_parse_reuter.findall(content)
    for reuter_item in reuter_items_in_one_file:
        body_list = re_parse_body.findall(reuter_item)
        body = body_list[0] if body_list else r""

        title_list = re_parse_title.findall(reuter_item)
        title = title_list[0] if title_list else r""

        ID_list = re_parse_id.findall(reuter_item)
        ID = ID_list[0] if ID_list else r""

        article = {"ID": ID, "title": title, "body": body}
        articles.append(article)

    return articles


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # '-p' or '--path' given reuter folder path
    parser.add_argument("-p", "--path", help="data folder path", type=str)

    # '-n' or '--number' how many files to read
    parser.add_argument("-n", "--number", help="how many files to read", type=int)

    # '-o' or '--output' redirect output to file
    parser.add_argument("-o", "--output", help="output to file", type=str)

    args = parser.parse_args()
    if not args.path:
        print("Please specify a folder path to read files!")
        exit(1)
    if not args.number:
        print("Please use -n <number of files to read>")
        exit(1)

    file_names = list(filter(lambda x: x.endswith(".sgm"), os.listdir(args.path)))
    file_names.sort()

    # read data
    result = []  # final output, [ [A1,...,A1000], [A1001,...,A2000], ... ]
    for i in range(args.number):
        file_path = args.path + "/" + file_names[i]
        articles = read_articles(file_path)

        result.append(articles)

    # output data
    # output to files
    if args.output:
        for i, articles_in_one_file in enumerate(result):
            output_file = args.output.replace("*", str(i))
            with open(output_file, "w") as fo:
                json.dump(articles_in_one_file, fo)

    # output to stdout
    else:
        print(json.dumps(result))










