def main():
    name = input('What is your name? ')
    month = input('What month were you born in? ')

    print('Hello %s!' % name)
    print('Your name has %d letters in it.' % len(name))
    if month.upper() == 'January':
        print('Happy Birthday Month')

main()