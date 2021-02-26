import random

with open('vocabulary.txt', 'r', encoding="UTF-8") as test:
    quiz_list = [t for t in test]
    quiz_volume = len(quiz_list)
    while True:
        index = quiz_list[random.randint(0, quiz_volume)]
        answer = index.strip().split(" : ")[0]
        quiz = input("{}: ".format(index.strip().split(" : ")[1]))
        if quiz == "q":
            print("Quiz를 종료합니다.")
            break
        elif quiz == answer:
            print("맞았습니다.")
        else:
            print("아쉽습니다 정답은 {}입니다".format(answer))