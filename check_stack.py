from stack import Stack as st

har_dict = {'{': '}', '}': '{', '[':']', ']':'[', '(':')', ')':'('}

new_lines = [
    '(((([{}]))))',
    '[([])((([[[]]])))]',
    '{()}{{[()]}}', 
    '}{}', 
    '{{[(])]}}',
    '[[{())}]']

def check_balance(new_string):
    new_stack = st()
    for ch in new_string:
        if new_stack.isEmpty():
            new_stack.push(ch)
        else:
            if har_dict[ch] == new_stack.peek():
                new_stack.pop()
            else:
                new_stack.push(ch)
    if new_stack.size():
        return new_stack.peek()
    else:
        return 'OK'


def list_to_check(list_):
    res = ''
    for item in list_:
        if check_balance(item) == 'OK':
            res += f'{item} is balanced \n'
        else:
            res += f'{item} - some trouble here\n'
    return res


if __name__ == '__main__':
    print(list_to_check(new_lines))