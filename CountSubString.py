def wower(input_string: str):
    counter = 0
    substring = "wow"
    for i in range(len(input_string)):
        if input_string[i:i+len(substring)] == substring:
            counter += 1
    return counter


assert wower("wowhatamanwowowpalehche") == 3
print(wower("wowhatamanwowowpalehche") == 3)
