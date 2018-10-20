import re
import time


def select_single(line):
    """
    :param line:一行字符串内容
    :return: 非词组开头的行
    """
    # 返回ascii码开头的行数，即非汉字开头
    if ord(line[0]) <= 127:
        return line
    # 返回有内容，且第二个字符为空格的行数
    if len(line) >= 2:
        if re.search(r'\S', line[1]) is not None:
            pass
        else:
            return line
    return None


def main():
    """
    读取文件，写入文件
    """
    with open('wubi86.dict.yaml', 'r', encoding='utf-8') as f:
        for line in f:
            s = select_single(line)
            if s is not None:
                print(s)
                with open('wubi86_single.dict.yaml', 'a', encoding='utf-8') as file:
                    file.write(s)


if __name__ == '__main__':
    # print(len('	'))
    start = time.time()
    main()
    end = time.time()
    print(f'运行时间:{end-start}秒')