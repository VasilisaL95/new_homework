calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    a = str(string)
    b = (len(a), a.upper(), a.lower())
    count_calls()
    return b


def is_contains(string, list_to_search):
    global result
    string = str(string)
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]) == string:
            result = False
            break
        else:
            result = False
        continue
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
