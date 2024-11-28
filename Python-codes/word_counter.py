def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().lower()  
    text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')  
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    with open(output_file, 'w') as file:
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")
    print(f"Word count has been written to {output_file}")


input_file = "input.txt"  
output_file = "word_count.txt"  
count_words(input_file, output_file)
