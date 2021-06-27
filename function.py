def multiplyNumbers(num1, num2):
    return num1*num2
print(multiplyNumbers(1,2))

sentence = "My, name, is, Eric"
word = sentence.split(",")
print(word)

pocketMoney = int(input("Enter your pocket money: "))
#print("My pocket money is "+ pocketMoney)

if(pocketMoney >=500):
    print("your life is good!")
elif(pocketMoney >= 250):
    print("your life is average")
elif(pocketMoney < 250):
    print("your life is poor")