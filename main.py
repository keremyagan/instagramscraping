import instaloader
import time
time_amount=0.5
def get_followers(L,username,password,account):
    profile = instaloader.Profile.from_username(L.context, account)
    # Print list of followees
    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        print(followee.username)
        time.sleep(time_amount)

def get_following(L,username,password,account):
    profile = instaloader.Profile.from_username(L.context, account)
    follow_list = []
    count = 0
    for followee in profile.get_followees():
        follow_list.append(followee.username)
        print(followee.username)
        time.sleep(time_amount)

def mega_data(L,username,password,account):
    profile = instaloader.Profile.from_username(L.context, account)  
    data=profile._metadata()
    biography=data["biography"]
    followers=data["edge_followed_by"]["count"]
    follow=data["edge_follow"]["count"]
    full_name=data["full_name"]
    username=data["username"]
    print(biography,followers,follow,full_name,username)
    time.sleep(time_amount)

def get_followers_list(L,username,password,accounts):
    for account in accounts:
        profile = instaloader.Profile.from_username(L.context, account)
        # Print list of followees
        follow_list = []
        count = 0
        for followee in profile.get_followers():
            follow_list.append(followee.username)
            print(followee.username)
            time.sleep(time_amount)

def get_following_list(L,username,password,accounts):
    for account in accounts:
        profile = instaloader.Profile.from_username(L.context, account)
        follow_list = []
        count = 0
        for followee in profile.get_followees():
            follow_list.append(followee.username)
            print(followee.username)
            time.sleep(time_amount)

def mega_data_list(L,username,password,accounts):
    for account in accounts:
        profile = instaloader.Profile.from_username(L.context, account)  
        data=profile._metadata()
        biography=data["biography"]
        followers=data["edge_followed_by"]["count"]
        follow=data["edge_follow"]["count"]
        full_name=data["full_name"]
        username=data["username"]
        print(biography,followers,follow,full_name,username)
        time.sleep(time_amount)



while True:
    islem=input("1-Giriş Yap\n2-Çıkış\nSeçiminiz:")
    if islem=="1" :
        username=input("Lütfen Kullanıcı Adını Giriniz:")
        password=input("Lütfen Parolayı Giriniz:")
        print("Lütfen Bekleyiniz...")
        while True:
            try:
                L = instaloader.Instaloader()
                username = username
                password = password
                L.login(username, password) 
                islem_2=input("1-Takip Edilen Bilgisini Al\n2-Takipçi Bilgisini Al\n3-Hesap Bilgisini Al\n4-Çıkış\nSeçiminiz:")
                if islem_2=="1":
                    secenek=input("1-Bir Kullanıcı\n2-Birden Fazla Kullanıcı\nSeçiminiz:")
                    if secenek=="1":
                        account=input("Lütfen Takipçi Bilgisi Alınacak Kişinin Kullanıcı Adını Giriniz:")
                        get_following(L,username,password,account)
                    elif secenek=="2":
                        account=input("Lütfen Kullanıcı Adlarını Aralarında Boşluk Bırakarak Giriniz:")
                        a=account.split()
                        get_following_list(L,username,password,a)
                        
                elif islem_2=="2":
                    secenek=input("1-Bir Kullanıcı\n2-Birden Fazla Kullanıcı\nSeçiminiz:")
                    if secenek=="1":
                        account=input("Lütfen Takipçi Bilgisi Alınacak Kişinin Kullanıcı Adını Giriniz:")
                        get_followers(L,username,password,account)
                    elif secenek=="2":
                        account=input("Lütfen Kullanıcı Adlarını Aralarında Boşluk Bırakarak Giriniz:")
                        a=account.split()
                        get_followers_list(L,username,password,a)           
                
                elif islem_2=="3":
                    secenek=input("1-Bir Kullanıcı\n2-Birden Fazla Kullanıcı\nSeçiminiz:")
                    if secenek=="1":
                        account=input("Lütfen Takipçi Bilgisi Alınacak Kişinin Kullanıcı Adını Giriniz:")
                        mega_data(L,username,password,account)
                    elif secenek=="2":
                        account=input("Lütfen Kullanıcı Adlarını Aralarında Boşluk Bırakarak Giriniz:")
                        a=account.split()
                        mega_data_list(L,username,password,a)             
                
                elif islem_2=="4":
                    print("Çıkış Yapıldı.")
                    break
                
                else:
                    print("Lütfen 1-4 Aralığında Değer Giriniz.")
                
            except Exception as err:
                print("Bağlantı Sağlanamadı.Lütfen Tekrar Deneyiniz.")
                print(err)
                break
                

    elif islem=="2":
        print("Çıkış Yapıldı.")
        break
    else:
        print("Lütfen 1 veya 2 Değerini Giriniz.")
