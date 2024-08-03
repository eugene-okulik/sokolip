import argparse
import os


def search_text_in_log(file_path, search_text):
    results = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if search_text in line:
                start_line = line.find(search_text)
                words = line.split()
                start_word = max(0, words.index(search_text) - 5)
                end_word = min(len(words), words.index(search_text) + 6)
                context = ' '.join(words[start_word:end_word])
                results.append((start_line, context))
    return results

def process_logs(folder, search_text):
    for root, dir, files in os.walk(folder):
        for file in files:
            results = search_text_in_log(file, search_text)
            for line_number, context in results:
                print(f'Номер строки в которой обнаружен искомый текст: {line_number}')
                print(f'Название файла в котором обнаружен тскомый текст: {file}')
                print(f'Костекст ошибки: {context}')


parser = argparse.ArgumentParser()
parser.add_argument('folder', type=str, help='folder path')
parser.add_argument('-t', '--text', type=str, help='Text for search')
args = parser.parse_args()
process_logs(args.folder, args.text)