import os
import re
import argparse
import json


def read_raw_file(path):
    file_names = os.listdir(path)
    file_names.sort()
    file_contents = []
    for file in file_names:
        if file.endswith(".sgm"):
            with open(path + '/' + file, 'r', encoding='unicode_escape') as f:
                content = f.read()
                file_contents.append(content)
    return file_contents


def read_articles(file_contents, include_title):
    re_read_reuter = re.compile(r"<REUTERS.*>([\s\S]*?)</REUTERS>")
    re_read_title = re.compile(r"<TITLE>([\s\S]*?)</TITLE>")
    re_read_body = re.compile(r"<BODY>([\s\S]*?)</BODY>")

    articles = []
    for content in file_contents:
        reuter_items_in_one_file = re_read_reuter.findall(content)
        for reuter_item in reuter_items_in_one_file:
            body_list = re_read_body.findall(reuter_item)
            body = body_list[0] if body_list else r""

            if include_title:
                title_list = re_read_title.findall(reuter_item)
                title = title_list[0] if title_list else r""
                articles.append(title + "\n" + body)
            else:
                articles.append(body)
    return articles


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # '-p' or '--path' given reuter folder path
    parser.add_argument("-p", "--path", help="data folder path", type=str)

    # '-o' or '--output' output to a file
    parser.add_argument("-o", "--output", help="write output to a file", type=str)

    # '-t' or '--title' include title
    parser.add_argument("-t", "--title", help="add this option to include title", action="store_true")

    args = parser.parse_args()

    include_title = True if args.title else False

    all_articles = read_articles(read_raw_file("P1/reuters21578"), include_title)

    if args.output:
        # output to file
        with open(args.output, 'w') as output_file:
            json.dump(all_articles, output_file)
    else:
        # output to stdout
        std_output = json.dumps(all_articles)
        print(std_output)
