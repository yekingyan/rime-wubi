import re


INPUT_FILE_PATH = "wubi86.dict.yaml.backup"
OUTPUT_FILE_PATH = "wubi86.dict.yaml"
CUT_WORD = "工	a	99454797	aa"


def get_trim_line():
    stay_line = []
    with open(INPUT_FILE_PATH, encoding="utf8") as f:
        trim_working = False
        for line in f:
            if re.match(CUT_WORD, line):
                trim_working = True
            if not trim_working:
                stay_line.append(line)
            else:
                line_list = line.split("	")
                word = line_list[0]
                code = line_list[1]
                if word.startswith("#") or len(word) == 1 or code.startswith("z"):
                    stay_line.append(line)

        return stay_line


def main():
    stay_line = get_trim_line()
    with open(OUTPUT_FILE_PATH, "w+", encoding="utf8") as f:
        for line in stay_line:
            f.writelines(line)


if __name__ == '__main__':
    main()
    # get_trim_line()
