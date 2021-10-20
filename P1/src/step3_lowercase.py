import json
import argparse
import glob  # filter files with regx pattern


def make_lowercase(tokens: list):
    for index, token in enumerate(tokens):
        tokens[index] = (str.lower(token[0]), token[1])
    return tokens



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # '-o' or '--output' output to file
    parser.add_argument("-o", "--output", help="write output to files", type=str)

    parser.add_argument("-i", "--input", help="input from files", type=str)

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

    # perform lowercase
    result = []
    for tokens_in_one_file in all_tokens:
        result.append(make_lowercase(tokens_in_one_file))

    # output to file
    if args.output:
        for i, tokens_in_one_file in enumerate(result):
            output_file = args.output.replace("*", str(i))
            with open(output_file, "w") as fo:
                json.dump(tokens_in_one_file, fo)

    # output to stdout
    else:
        print(json.dumps(result))
