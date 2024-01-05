print("Welcome to My Computer Science Quiz")
playing=input("Do you want to play? ")

if playing.lower()!="yes" :
    quit()
print("Okay ! let's start the quiz :)")
Score=0

answer=input("SDLC stands for? ")
if answer.lower()== 'software development life cycle':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")

answer=input("The Fifth Generation Computer works on …? ")
if answer.lower()== 'artifical intelligence':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")


answer=input("The ‘P’ in CPU stands for …? ")
if answer.lower()== 'process':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")



answer=input(".......is also known as “Information Highway?”? ")
if answer.lower()== 'internet':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")


answer=input("In python , how to define function? ")
if answer.lower()== 'def':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")


answer=input("GPU stands for? ")
if answer.lower()== 'graphic process unit':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")


answer=input("HTTP stands for? ")
if answer.lower()== 'hyper text transfer protocol':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")


answer=input("The .com used frequently in website url can be expressed as …? ")
if answer.lower()== 'commerical':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")


answer=input(" One word for class?? ")
if answer.lower()== 'blueprint':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")



answer=input("OS stands for? ")
if answer.lower()== 'operating system':
    print("Great Job ! ")
    Score+=1
else:
    print("Incorrect ! ")

print("You got " + str(Score) + " question correct ")




