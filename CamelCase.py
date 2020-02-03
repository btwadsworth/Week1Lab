# This program takesa sentence and converts it to camel case

def main():
    display_banner()
    invalid_chars = '@#$%^&*()_-+=[[}{;:"<>/`~|'
    while True:
        invalid = False
        sentence = input('Enter a sentence: ')  # Get input

        # Test for any numbers
        if any(char.isdigit() for char in sentence):
            print('Do not enter any numbers.')
        
        # Test for any invalid characters
        else:
            for char in invalid_chars:
                if char in sentence:
                    print('Invalid character: %s' % char)
                    invalid = True
                    break
        if not invalid:
            break
    
    words = sentence.split(' ')  # Split sentence into list
    new_words = [n.capitalize() for n in words]  # Capitalize the first letter of all items in list
    new_sentence = ''.join(new_words)  # Join all words together
    new_sentence = new_sentence[:1].lower() + new_sentence[1:]  # Make the first letter of the string lowercase
    print('Your sentence in camel case is: %s' % new_sentence)


def display_banner():
    """ Display program name in banner """
    msg = 'AWSOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

main()