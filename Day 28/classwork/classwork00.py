"""მომხმარებელს შემოატანინეთ ქულა 0-100, თუ ქულა იქნება 90ზე მეტი დაბეჭდოს რომ შენ შეგიძლია აიღო სერთიფიკატი,
თუ ქულა იქნება 70-ზე მეტი დაბეჭდოს რომ გააუმჯობესე, სხვა შემთხვევაში დაბეჭდოს რომ არის ძალიან ცუდი 
შედეგი და ის ვერ აიღებს სერთიფიკატს"""

point = int(input("enter Your point: "))
if point > 90:
    print("you can get your certificate")
elif point > 70: 
    print("upgrade it!")            
else:
    print("very bad result")