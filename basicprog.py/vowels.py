
text = "Pavani"
vowelsss= "aeiouAEIOU"
sum=0
sum1=0
vowels = []
consonants = []
for i in text:
    if i.isalpha():  
        if i in vowelsss:
            vowels.append(i)
            sum+=1
        
        else:
            consonants.append(i)
            sum1+=1
    
print("Vowels:", vowels)
print(sum)
print("Consonants:", consonants)
print(sum1)