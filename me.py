#API_TASK_123 ამ  ფუნქციაში შესრულებულია ქვიზის 1 2 3 კითხვები! გასაშვებად გამოიძახეთ API_TASK_123()
def API_TASK_123():

    import requests
    import json

    """
    #სანამ პროგრამას გაუშვებ ამოირჩიე რომელი ჯიშის წარმომადგენელი ძაღლის ხილვა გსურს
    #და პროგრამა ავტომატურად ჩამოტვირთავს საიტიდან დაამახსოვრებს jpg ფორმატში!
    #(husky, mix, beagle, cairn, pitbull, caucasian ovcharka ა.შ) ან ნებისმიერი ჯიშის დასახელება
    """

    dog_breed = input("გთხოვთ შეიყვანეთ ზემოთ ჩამოთვლილი ძაღლის ჯიში: ")
    r = requests.get(f"https://dog.ceo/api/breed/{dog_breed}/images/random")
    print(r.status_code)
    print(r.headers)

    res = r.json()


    url_photo = res["message"]
    print(url_photo)

    get_photo = requests.get(url_photo)

    with open(f'{dog_breed}.jpg', 'wb') as f:
        f.write(get_photo.content)
        print('სურათი წარმატები შეინახა!')

    number_of_facts = input("შეიყვანეთ რაოდენობა რამდენი ფაქტის მოსმენა გსრუთ ძაღლებზე: ")
    dog_facts = requests.get(f'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number={number_of_facts}')
    # print(dog_facts.text)
    res = json.loads(dog_facts.text)
    # print(json.dumps(res , indent=4))

    with open("dogfacts.json", 'w') as file:
        json.dump(res, file, indent=4)



# def API_TASK_123():




#ამ ფუნქციაში შესრულებული ქვიზის 4 დავალება გასაშვებად გამოიძახეთ db_tast_4()
def db_tast_4():
    import requests
    import json
    import sqlite3


    #ბეჭდავს json ფორმატიტ კოვიდის ინფორმაციას მსოფლიოში არსებული სიტუაციიდან გამომდინარე.
    r = requests.get("https://api.covid19api.com/summary")
    print(r)
    res = json.dumps(r.json(), indent=4)
    # print(res)



    #ქმნის დეითა ბეის covid19.sqlite შემდეგ ვქმნით თეიბლს და აიპიას მეშვეობით მოგვაქვს კოვიდის ინფორმაცია
    #https://documenter.getpostman.com საიტიდან შემდეგ ვახარისხებთ და შეგვაქ ინფორმაცია ჩვენივნე შექმნილ თეიბლში.

    connect = sqlite3.connect('covid19.sqlite')
    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS COVID19info
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COUNTRY VARCHAR(50),
    CountryCode VARCHAR(10),
    Slug VARCHAR (20),
    TotalConfirmed INTEGER,
    TotalDeaths INTEGER,
    TotalRecovered INTEGER,
    Date DATE);
    ''')





    for i in range(len(r.json()['Countries'])):
        country = (r.json()['Countries'][i]['Country'])
        CountryCode = (r.json()['Countries'][i]['CountryCode'])
        Slug = (r.json()['Countries'][i]['Slug'])
        TotalConfirmed = (r.json()['Countries'][i]['TotalConfirmed'])
        TotalDeaths = (r.json()['Countries'][i]['TotalDeaths'])
        TotalRecovered = (r.json()['Countries'][i]['TotalRecovered'])
        date_time = (r.json()['Countries'][i]['Date'])
        tup = (country, CountryCode, Slug, TotalConfirmed, TotalDeaths, TotalRecovered, date_time)
        cursor.execute('''INSERT INTO COVID19info (COUNTRY, CountryCode, Slug, TotalConfirmed, TotalDeaths, TotalRecovered, Date) values (?, ?, ?, ?, ?, ?, ?)''', tup)
        connect.commit()




    connect.close()



# def db_tast_4():



