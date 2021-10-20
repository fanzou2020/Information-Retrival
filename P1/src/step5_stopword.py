import json
import argparse
import glob  # filter files with regx pattern
import nltk
from nltk.corpus import stopwords

def stop_words_removal(tokens:list, stop_words):
    stop_words_set = set(stop_words)
    filtered_tokens = [word for word in tokens if word[0] not in stop_words_set]
    return filtered_tokens


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # '-o' or '--output' output to file
    parser.add_argument("-o", "--output", help="write output to files", type=str)

    parser.add_argument("-i", "--input", help="input from files", type=str)

    parser.add_argument("--sw", help="stop world file name", type=str)

    args = parser.parse_args()

    all_tokens = []  # [ [("a", 1),... ("b",1000)], [("d",1001),...("f",2000)] ]

    # read from files
    if args.input:
        input_files = glob.glob(args.input)
        input_files.sort()
        for file_name in input_files:
            with open(file_name, "r") as fi:
                all_tokens.append(json.load(fi))

    # read from stdin
    else:
        input_str = input()
        all_tokens = json.loads(input_str)

    # read stop words if applicable
    stop_words_list = []
    if args.sw:
        with open(args.sw, "r") as fs:
            lines = fs.readlines()
            for word in lines:
                stop_words_list.append(word.strip())
    else:
        stop_words_list = stopwords.words('english')

    # perform stop words removal
    result = []
    for tokens_in_one_file in all_tokens:
        result.append(stop_words_removal(tokens_in_one_file, stop_words_list))

    # output to file
    if args.output:
        for i, tokens_in_one_file in enumerate(result):
            output_file = args.output.replace("*", str(i))
            with open(output_file, "w") as fo:
                json.dump(tokens_in_one_file, fo)

    # output to stdout
    else:
        print(json.dumps(result))
