
with open('vocabulary.txt', 'a', encoding='UTF-8') as eng_kor:
    while True:
        word = input('영어 단어를 입력하세요: ')
        if word =='q':
            break
        answer = input('뜻을 입력하세요: ')
        if answer == 'q':
            break

        eng_kor.write("{} : {}\n".format(word, answer))