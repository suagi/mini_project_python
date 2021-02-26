
with open('vocabulary.txt', 'r', encoding="UTF-8") as test:
    for t in test:
        answer = "{}".format(t.strip().split(" : ")[0])
        quiz = input("{}: ".format(t.strip().split(" : ")[1]))
        if quiz == answer:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(answer))