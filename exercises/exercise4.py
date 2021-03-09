def find_adults(file_path):
    with open(file_path, 'r') as fd:
        for line in fd.readlines():
            if line == "" or line == "\n":
                continue
            split_line = line.split()
            if int(split_line[2]) > 20:
                print(split_line[1])


if __name__ == "__main__":
    find_adults('names.txt')
