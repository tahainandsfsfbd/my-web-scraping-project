
#QUİZ GAME 

print("Welcome to my computer quiz...")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes" : # eğer cevap "yes" değilse programdan çıkış yapılır.
    quit()

print("Okay! Let us play!")

score = 0

answer1 = input("What does CPU stand for? ")
if answer1.lower().strip() == "central processing unit" :  # cevap doğruysa "score" değişkenine 1 eklenir.
    print("Correct!")                                      # strip() ile cevabın başında veya sonunda boşluk varsa kaldırıldı.
else: 
    print("Incorrect!")

answer2 = input("What does GPU stand for? ")
if answer2.lower().strip() == "graphics processing unit" : # cevap doğruysa "score" değişkenine 1 eklenir.
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")

answer3 = input("What does RAM stand for? ")
if answer3.lower().strip() == "random access memory" : # cevap doğruysa "score" değişkenine 1 eklenir.
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")

answer4 = input("What does PSU stand for? ")
if answer4.lower().strip() == "power supply" : # cevap doğruysa "score" değişkenine 1 eklenir.
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {score/4*100}%. ")