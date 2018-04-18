def get_user_input(prompt, num_tries=9999):
    print('===== GetUserInput =====')
    valid_input = False
    attempts = 0
    ret_val = ''
    while not valid_input:
        ret_val = input(prompt)
        attempts += 1
        if len(ret_val) > 0:
            valid_input = True
            if attempts >= num_tries:
                print('Too many attempts')
                ret_val = ''
                break

    return ret_val


def menu():
    print('===== Menu =====')
    user_input = get_user_input('What do you want to do?', 1)
    return user_input


def show_user_results(msg):
    print('===== ShowUserResults =====')
    print(msg)
    return 0
