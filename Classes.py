def main():
    print('Enter the names of your classes this semester one at a time.')
    print('Press enter when done.')
    classes = []
    while True:
        class_name = input('Enter class name: ')
        if class_name == '':
            break
        else:
            classes.append(class_name)
    class_list = '\n'.join(classes)
    print(class_list)

main()