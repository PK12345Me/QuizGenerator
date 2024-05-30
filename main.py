from quest import *
#data={}
ans =[]
def main():
    question_data = questions()
    print(grade_quiz(prompt(question_data)))

def prompt(data):
    try:
        for x in range(len(data)):
            print(f"Q {x+1}: {data[x][0]}")
            for key, value in enumerate(data[x][1]):
                print(f"{key+1}: {value}")

            ans.append(int(input("Enter your answer: ")))
            #return ans
    except (TypeError, ValueError, KeyboardInterrupt) as e:
        print (e)
        return ans
    grade_quiz(ans)


def grade_quiz(ans):
    #print ("this is", ans)
    answers = ans
    # user provided key
    correct_answers = [3, 1, 1, 2, 3, 1, 1, 2, 2, 4]
    score = sum(1 for user_answer, correct_answer in zip(answers, correct_answers) if user_answer == correct_answer)
    user_answers = ans
    Wlist=[]
    for i in range(len(user_answers)):
        if user_answers[i] != correct_answers[i]:
            Wlist.append((i+1))
    else:
        print ("some error here")
    return (f" Your score is: {score} and the wrong answers list is {Wlist}")



if __name__=="__main__":
    main()
