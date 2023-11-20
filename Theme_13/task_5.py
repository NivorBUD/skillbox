with open('errors.txt', 'w') as error_file:
    errors = [line for line in open('log.txt', 'r') if 'ERROR' in line]
    for error in errors:
        error_file.write(error)
