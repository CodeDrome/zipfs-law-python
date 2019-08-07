import zipfslaw


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Zipf's Law    |")
    print("-----------------\n")

    try:

        f = open("dracula.txt", "r")
        text = f.read()
        f.close()

        zipf_table = zipfslaw.generate_zipf_table(text, 135)

        zipfslaw.print_zipf_table(zipf_table)

    except IOError as e:

        print(e)


main()
