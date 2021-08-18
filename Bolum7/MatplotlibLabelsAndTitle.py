# Matplotlib Labels and Title  -->  Matplotlib Etiketleri ve Başlığı






# Bir Grafik için Etiketler Oluşturun



"""


Bir Grafik için Etiketler Oluşturun
------------------------------------



Pyplot ile x ve y ekseni için bir etiket ayarlamak için  xlabel()  ve  ylabel()  işlevlerini kullanabilirsiniz .
-------------------------------------------------------- ******* ----- ******** -------------------------------



Neymis xlabel() ve ylabel()     --> x etiketi ve y etiketi  Anlastik mi?



Hadi ornege gecelim!!



"""






# Ornek  x ve y eksenine etiketler ekleyin:



import matplotlib.pyplot as plt
import numpy as np



x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.plot(x, y)


plt.xlabel("Ortalama Nabız")
plt.ylabel("Kalori Yakma")


plt.show()




# Simdi burada "" adli diagrama dikkatlice baktiginizda


# x yonunde asagida bulunan ortalama nabizi
# y yonunde bulunan sol tarafta kalori yakmayi goreceksiniz


# Bence yavas yavas yeteneklerimiz artiyor bu alanda!








# Simdide Grafik basligi yapalim genel bir adi olsun degil mi?





"""



Bir Grafik için Başlık Oluşturun
------------------------------


Pyplot ile, title()  grafik için bir başlık ayarlamak için işlevi kullanabilirsiniz .
----------- ******* -------------------------------------------------------------



"""





# Ornek  x ve y ekseni için bir grafik başlığı ve etiketler ekleyin:





import matplotlib.pyplot as plt
import numpy as np



x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.plot(x, y)


plt.title("Sportif istatistik Verileri")
plt.xlabel("Ortalama Nabiz")
plt.ylabel("Kalori Yakma")


plt.show()





# Simdi dikkatlice "ornek26.png" adli diagrama bakin


# x yonunde asagida bulunan ortalama nabizi
# y yonunde bulunan sol tarafta kalori yakmayi
# Diagramin en ustunde baslik kisminda Sportif istatistik Verilerini goreceksiniz








# Simdide ne yapalim  biraz yazi tipi ozelliklerini inceleyelim...



"""


Başlık ve Etiketler için Yazı Tipi Özelliklerini Ayarlayın
-----------------------------------------------------------


Başlık ve etiketler için yazı tipi özelliklerini ayarlamak için xlabel(), ylabel() ve title() içindeki 
--------------------------------------------------------------- ********--********----*******---------
fontdict parametresini kullanabilirsiniz.
******** -------------------------------



Simdi asagida bir ornek yapacagijm takip edin!

"""





# Örnek Başlık ve etiketler için yazı tipi özelliklerini ayarlayın:




import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.title("Sportif Istatistik Verileri", fontdict=font1)
plt.xlabel("Ortalama Nabiz", fontdict=font2)
plt.ylabel("Kalori Yakma", fontdict=font2)


plt.plot(x, y)
plt.show()





# Sonuc geldi evet simdi "ornek27.png" ad li diagrama bakin baslik ve etiketleri cok iyi bir sekilde duzenledik


"""

# xlabel("Etiket x bolgesi icin", fontdict= yazi tipi)
# ylabel("Etiket y bolgesi icin", fontdict= yazi tipi)
# title("Baslik", fontdict= yazi tipi)


"""


# Simdi arkadaslar boyle bir islemi yapmak icin ilk etapta yazi stillerini, renklerini ve boyutlarini onceden
# degiskenler icinde tanimlamaliyiz! Yani nasil biraz onceki gibi!



"""

Turkce Tanim

font1 --> Birinci yazi tipi = yazi tipi --> serif -- renk --> mavi -- boyut --> 20
font2 --> Ikinci yazi tipi = yazi tipi --> serif -- renk --> Koyu kirmizi -- boyut --> 15



Ingilizce Tanim

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


Ama unutmayin programlama dili ingilizce turkcesini yazmayin :d


"""





# Evet burayida cozduk... Devam edelim hanimlar beyler






# Başlığı Konumlandırma




"""


Başlığı Konumlandır
-------------------



Başlığı konumlandırmak için title() içindeki loc parametresini kullanabilirsiniz.
--------------------------- ****** --------- *** -------------------------------

Yasal değerler: 'left', 'right' ve 'center'. Varsayılan değer 'center' 
---------------- ****---****** ---- ******   ----------------  *******


"""




# Simdi ne yapmamiz gerek biliyorsunuz title icinde bir islem yapacagiz. sag sol veya orta ama varsayilan deger orta unutmayin







# Örnek Başlığı sola konumlandırın:




import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.title("Sportif Istatistik Verileri", loc='left')
plt.xlabel("Ortalama Nabiz")
plt.ylabel("Kalori Yakma")


plt.plot(x, y)
plt.show()






# Sonucumuz geldi "ornek28.png" adli diagramda basligimizin sol tarafa gectigini goreceksinizdir.
# Ayrica unutmayin loc kisaltilmis halidir normalde bunun anlami location = yer ' dir







# Bu bolumude hallettik yine iyisin :))

















