import random 
print('Xin chào bạn! Bạn có thể cho mình biết tên được không?')
name = input()
print('Chào ' + name + '! Mình có một trò chơi này tên là đoán số, cùng chơi nào!')
print('Bạn sẽ có tất cả 7 lần để đoán số trong khoảng từ 1 đến 20, cố đoán đúng nhé ^^')
print('Bắt đầu trò chơi nào!')
randomNumber = random.randint(1, 20)

for guessTaken in range(1, 8):
    print('Mời bạn đoán: ')
    guessNumber = int(input()) #input int để người chơi không nhập gì ngoài số
    if guessNumber < randomNumber:
        print('Bạn đoán thấp quá! Thử đoán cao hơn xem')
    elif guessNumber > randomNumber:
        print('Bạn đoán cao quá! Thử đoán thấp hơn xem')
    else:
        break #break nếu người chơi đoán đúng hoặc hết số lần đoán

if guessNumber == randomNumber:
    print('Bạn đoán đúng rồi! Chúc mừng bạn! Bạn chỉ mất ' + str(guessTaken) + ' lần để đoán đúng')
else:
    print('Chúc may mắn lần sau nha! Bạn tốn ' + str(guessTaken) + ' lần mà vẫn đoán sai :))' + 'Con số bạn cần đoán là: ' + str(randomNumber))
