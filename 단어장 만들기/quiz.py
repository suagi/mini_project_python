
with open('vocabulary.txt', 'r', encoding="UTF-8") as test:
    for t in test:
        correct_answer = "{}".format(t.strip().split(" : ")[0])
        my_answer = input("{}: ".format(t.strip().split(" : ")[1]))
        if my_answer == correct_answer:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(correct_answer))