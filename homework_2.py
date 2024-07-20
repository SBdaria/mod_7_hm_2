from pprint import pprint
def custom_write(file_name, strings):
    count_str = 1
    strings_positions = {}
    file = open(file_name, 'a+', encoding='utf-8')
    for i in strings:
        tup = count_str, file.tell()
        strings_positions[tup] = i
        file.write(i + '\n')
        count_str += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)