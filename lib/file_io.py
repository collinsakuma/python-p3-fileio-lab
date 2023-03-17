def write_file(file_name, file_content):
    with open(file_name + '.txt', mode='w', encoding='utf-8') as file_name:
        file_name.write(file_content)

def append_file(file_name, append_content):
    with open(file_name + '.txt', mode='a', encoding='utf-8') as file_name:
        file_name.write(append_content)

def read_file(file_name):
    file_to_read = open(file_name + '.txt', encoding='utf-8')
    return file_to_read.read()

    ##### also works ######

    # with open(file_name + '.txt') as text_file:
    # return text_file.read()