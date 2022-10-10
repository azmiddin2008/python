import random
while True:
    tanlov = ["tosh", "qaychi", "qogoz"]
    
    computer = random.choice(tanlov)
    pleyer = None
    
    while pleyer not in tanlov:
        pleyer = input("tosh, qaychi, qogoz:  ").lower()
        
    if pleyer == computer:
        print("computer " + computer)
        print("pleyer: " + pleyer)
        print("Durang natija qayd etildi!")
    
    elif pleyer == 'tosh':
        if computer == 'qogoz':
            print("computer📃: " + computer)
            print("pleyer🥊: " + pleyer)
            print("Afsuski siz yutkazdingiz!")
        if computer == 'qaychi':
            print("computer✂: " + computer)
            print("pleyer🥊:  " + pleyer)
            print("Tabriklaymiz. Siz yutdingiz!")
    
    elif pleyer == 'qogoz':
        if computer == "tosh":
            print("computer🥊: " + computer)
            print("pleyer📃: " + pleyer)
            print("Tabriklaymiz. Siz yutdingiz!")
        if computer == 'qogoz':
            print("computer✂: " + computer)
            print("pleyer📃: " + pleyer)
            print("Afsuski siz yutkazdingiz!")
    elif pleyer == 'qaychi':
        if computer == 'tosh':
            print("computer🥊: " + computer)
            print("pleyer✂: " + pleyer)
            print("Afsuski siz yutkazdingiz!")
        if computer == 'qogoz':
            print("computer📃: " + computer)
            print("pleyer✂: " + pleyer)
            print("Tabriklaymiz. Siz yutdingiz!")
        
    qayta_urinish = input("Qayta oynaysizmi?: ").lower()
    
    if qayta_urinish != 'ha':
        break
    
    
print("Oynaganingiz uchun rahmat! ")
  
    