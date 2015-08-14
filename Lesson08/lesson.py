from riddler import get_joke


def tell_joke():
    print get_joke()


def main():
    while True:
        try:
            joke_question = raw_input("Do you want to hear a joke? ")
            if joke_question.lower() in ['y', 'yes', 'yep', 'sure', 'ok']:
                break
            else:
                print("But I really want to tell you one.")
        except EOFError:
            print "Awww shucks."

    tell_joke()


if __name__ == '__main__':
    main()


