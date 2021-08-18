# Matplotlib Subplots  -->  Matplotlib Alt Grafikleri





# Display Multiple Plots -- Coklu Grafikleri Goruntule




"""


Display Multiple Plots -- Coklu Grafikleri Goruntule
----------------------------------------------------


subplots() İşlev ile tek bir şekilde birden fazla grafik çizebilirsiniz:


"""






# Ornek 2 tane grafik cizin




import matplotlib.pyplot as plt
import numpy as np


# Grafik 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)


# Grafik 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)



plt.show()






# Sonucumuz geldi simdi "ornek33.png" adli diagramlara dikkatlice bakin orada iki adet grafigimiz var
# Simdi subplot icerisindeki parametre degerlerimizi tartisacagiz asagida beni dikkatlice anlamaya calisin!
# Neyse hadi asagi gelin size anlatayim su subplot(bla, bla, bla) bla bla ne yaaa iste onu aciklayacam. Neden oradalar!







# subplots() Fonksiyonu





"""


subplots() Fonksiyonu
---------------------



subplots() Fonksiyon şekil düzenini açıklar üç argüman alır.
------------------------------------------------------------

Düzen, birinci ve ikinci argüman tarafından temsil edilen satırlar ve sütunlar halinde düzenlenir.
-------------------------------------------------------------------------------------------------

Üçüncü argüman, mevcut grafik indeksini temsil eder.
-------------------------------------------------


plt.subplot(1, 2, 1)
Şekil:  1 satır, 2 sütundan oluşmaktadır ve bu grafik ilk grafiktir.


plt.subplot(1, 2, 2)
Şekil: 1 satır, 2 sütundan oluşmaktadır ve bu grafik ikinci grafiktir




Yani
-----

Birinci parametre -- Satirlar
Ikinci Parametre -- Sutunlar
Ucuncu Parametre Grafik Indeksi




Yani, 2 satır ve 1 sütunlu bir şekil istiyorsak (yani iki grafiğin yan yana yerine üst üste görüntüleneceği 
anlamına gelir), sözdizimini şöyle yazabiliriz:


"""






# Üst üste 2 grafik çizin:





import matplotlib.pyplot as plt
import numpy as np



# Grafik 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x, y)



#Grafik 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x, y)



plt.show()





# Tek bir şekil üzerine istediğiniz kadar grafik çizebilirsiniz, sadece satır, sütun ve grafiğin indeksini
# tanımlayın.




# Simdi arkadaslar sonucumuz olan "ornek34.png" adli diagramda bulunan grafiklere dikkatlice bakin
# soyle bakin lutfen    plt.subplot(satir sayisi, sutun sayisi, grafik indeksi)

# Bence Anladiniz devam edelim. Anlamadiysaniz orneklere devam!!!









# Ornek 6 tane grafik cizin




import matplotlib.pyplot as plt
import numpy as np


# Grafik 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x, y)



# Grafik 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x, y)



# Grafik 3:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x, y)



# Grafik 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x, y)



# Grafik 5:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x, y)




# Grafik 6:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x, y)




plt.show()






# Bakin guzel bir sekilde anlattim simdi "" adli diyagramdaki grafiklere bakin farkettiyseniz sadece
# en sondaki parametre olan grafik indeks numarasi degisti her yeni grafik olusturdugumuzda bir indeks artiyor
# Yani grafikler sirasiyla 2 satir icinde ayri ayri bulunan 3 sutunun icine yerlesecek sekilde tek tek indeks
# numarasi arttirilarak ekleniyor!!



# Bence anlastik... Acik ve net anlattim. Bence anlayin ya :ddddd






# Simdi farkli bir sey daha yapalim ayri ayri bulunan grafiklere basliklar ekleyelim
# ayri ayri basliklar ekleyelim yani bakin normalde biliyorsunuz ama yinede yapalim :)))







# Başlık



"""


Başlık : 
--------


Şu title() fonksiyonuyla her grafige bir başlık ekleyebilirsiniz :
------------------------------------------------------------------


"""






# Ornek: Başlıkları ile beraber 2 grafik yapalim:




import matplotlib.pyplot as plt
import numpy as np



# Grafik 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")



# Grafik 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")




plt.show()





# Gordugunuz gibi "" adli diyagramdaki iki tane grafik var basliklarini istedigimiz gibi koyduk
# Bence bunu anladiniz islerin nasil dondugunu ozellikle satir sutun ve grafik indeksi hepsi basit!!



# Simdi ben size birsey daha gosterecegim super baslik duydunuz mu? iste mukemmel gorunecek...







# Super Title  --> Süper Başlık



"""


Super Title  --> Süper Başlık
-----------------------------


suptitle() işleviyle tüm şekle bir başlık ekleyebilirsiniz:


Yani iki tane grafik ogesi olan bir diagrama genel bir baslik atabiliriz



"""





# Örnek Tüm diyagram veya sekil için bir başlık ekleyin:




import matplotlib.pyplot as plt
import numpy as np



# Grafik 1:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")



# Grafik 2:

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")



plt.suptitle("MY SHOP")
plt.show()






# Arkadaslar gordunuz suptitle() ile ana baslik attik diyagramimiza yani artik genel olarakta baslik atabiliriz
# Burada cikan sonucumuz "" adli diagramimizi anlamaya calisin ve neyi nerede kullanicaginizi bilin
# mesela title() ile suptitle() arasindaki farki bilin
# 1-  Grafik sayisi cok ise grafiklere ayri ayri title() ile ozel basliklar verebilirsiniz
# 2-  Grafiklerin bulundugu diyagrama genel bir baslik vermek istiyorsaniz suptitle() kullanmaniz gerekecektir






# Bir sonraki derste gorusmek uzere :)))



