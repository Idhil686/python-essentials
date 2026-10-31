print("Welcome to the grade checker")
name = input("Enter your name: ")

try:
    score = int(input("Enter your score: "))
except ValueError:
    print("Invalid input. Please enter a number between 0 and 100.")
else:
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        print(f"{name} scored {score} on the test")

        if score >= 90:
            print("Excellent work! You have mastered this material. ✨")
        elif score >= 80:
            print("Good job! You understand most of the concepts. 👍")
        elif score >= 70:
            print("You did okay. A little more practice would help. 📚")
        elif score >= 60:
            print("You need to study more to improve your understanding. 💪")
        elif score >= 50:
            print("You barely passed. Focus on the weak areas. ⚠️")
        else:
            print("You did not pass. Please meet with me to discuss a study plan. 🚨")

        if score >= 50:
            print("Status: PASSED 🎉")
        else:
            print("Status: FAILED")