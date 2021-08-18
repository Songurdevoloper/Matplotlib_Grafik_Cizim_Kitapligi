# Matplotlib Adding Grid Lines  --> Matplotlib Sutun Cizgileri Ekleme





# Add Grid Lines to a Plot -- Bir Grafige Sutun Cizgileri Ekle





"""


# Add Grid Lines to a Plot -- Bir Grafige Sutun Cizgileri Ekle
---------------------------------------------------------------

Pyplot ile, grid() grafige sutun çizgileri eklemek için işlevi kullanabilirsiniz .


"""



# Simdi bir ornekle peskistirelim bu sutun olayini!






# Ornek Grafiğe sutun çizgileri ekleyin:




import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.title("Sportif Istatistik Verileri")
plt.xlabel("Ortalama Nabiz")
plt.ylabel("Kalori Yakma")


plt.plot(x, y)

plt.grid()

plt.show()






# Simdi Sonuca dikkatlice bakin "ornek29.png" adli diagramda sutun olustugunu goreceksiniz bunu plt.grid() yaptik simdi
# bir takim degisikliklerde yapacagiz! Bakalim sutunlar icin neler yapabiliriz ...





# Hangi Sutun Çizgilerinin Görüntüleneceğini Belirtin




"""


Hangi Sutun Çizgilerinin Görüntüleneceğini Belirtin
---------------------------------------------------



Hangi sutun çizgilerinin görüntüleneceğini belirlemek axis yani eksen için grid() - sutun fonksiyondaki parametreyi kullanabilirsiniz .


Yasal değerler: 'x', 'y' ve 'her ikisi'dir. Varsayılan değer 'her ikisi'dir.
--------------- ******* -----************** ---------------- ***************


"""





# Simdi mesela x ekseninin eksenini goruntuleyelim grafik uzerinde yani biz x'in grafik uzerindeki gorunumune bakalim





# Örnek Yalnızca x ekseni için kılavuz çizgilerini görüntüle:


import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.title("Sportif Istatistik Verileri")
plt.xlabel("Ortalama Nabiz")
plt.ylabel("Kalori Yakma")


plt.plot(x, y)

plt.grid(axis='x')

plt.show()







# Simdi dikkatlice bakin lutfen "ornek30" adli diagramda sadece x'in eksenini goreceksinizdir.
# Farkettiyseniz y ekseni yok cunku biz sadece x icin eksen goruntusu istedik
# Mesela hic birsey yazmasaydik varsayilan neydi? Bence ikiside varsayilan degerdi. Sizce? sizcede oyle olsun!





# Neyse kafaniza yatsin diye simdide sadece y eksenini getirelim.
# Hadi ornege gelin gostereyim ne demek istdigimi!






# Yalnızca y ekseni için kılavuz çizgilerini göster:



import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.title("Sportif Istatistik Verileri")
plt.xlabel("Ortalama Nabiz")
plt.ylabel("Kalori Yakma")



plt.plot(x, y)

plt.grid(axis='y')

plt.show()





# Simdi "ornek31.png" adli diyagrami dikkatlice inceleyin bu sefer sadece y eksenini goruyoruz.
# Iste bu kadar yani x ve y eksenini ayri ayri inceleyebiliyoruz.
# Unutmayin varsayilan deger her ikisidir


# Simdi biraz diger ozelliklere bakalim!!







# Sutun için Çizgi Özelliklerini Ayarlayın




"""


Sutun için Çizgi Özelliklerini Ayarlayın
----------------------------------------




Ayrıca ızgaranın çizgi özelliklerini şu şekilde ayarlayabilirsiniz: 
-----------------*******************-----------------------------

Ingilizce
--------
grid(color = ' color ', linestyle = ' linestyle ', linewidth = number ).

Turkce
-------
sutun(renk = ' renk? ', cizgistili = ' cizgi stili? ', cizgigenisligi = numara ).



Unutma programi ingilizce yaziyoruz sadece anlayin diye turkcesini yazdim :)


"""



# Simdi ornekle bunu hemen aciklayayim takip edin beni!











# Ornek Sutunun çizgi özelliklerini ayarlayın:




import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
y = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310])


plt.title("Sportif Istatistik Verileri")
plt.xlabel("Ortalama Nabiz")
plt.ylabel("Kalori Yakma")



plt.plot(x, y)

plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()






# Simdi "ornek32.png" adli diagrama bakin
#| sutun rengi : yesil | cizgi stili : -- | cizgi genisligi : 0.5


# Anladiniz degilmi ne yaptigimizi! Bence evet cunku hersey turkcelestirildi...
# Ingilizceyi ogrenin veya ingilizcesini cunku programlama dili ingilizce !!






# Bu derste bitti hadi diger derste gorusuruz...
















