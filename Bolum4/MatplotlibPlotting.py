# Matplotlib Plotting  -->  Matplotlib Cizim




# Gelelim biz gecen bolumde ne yaptik onu anlamaya degil mi?
# Hadi baslayalim sihirli kelimelerin bize neler yaptirdigina !!!






# x  ve  y noktalarının çizilmesi





"""



x ve y noktalarının çizilmesi
-----------------------------



plot() Fonksiyonu, bir diyagram noktalarına (markörler) çekmek için kullanılır.
-------------------------------------------------------------------------------

****

markörler nedr ?

Önemli ibareleri veya dikkati çekmek istenilen yerleri işaretlemeye yarayan kalem.

***




Varsayılan olarak, plot() işlev noktadan noktaya bir çizgi çizer.
----------------------------------------------------------------

İşlev, diyagramdaki noktaları belirtmek için parametreler alır.
---------------------------------------------************-----

Parametre 1, (x) ekseni üzerindeki noktaları içeren bir dizidir .
---------------------------------------------------------------

Parametre 2, (y) eksenindeki noktaları içeren bir dizidir .
---------------------------------------------------------




(1, 3)'ten (8, 10)'a bir çizgi çizmemiz gerekirse, çizim işlevine iki dizi [1, 8] ve [3, 10] geçirmemiz gerekir.
---------------------------------------------------------------------------------------------------------------



# HEMEN ORNEKLE PEKISTIRELIM!



"""




# Ornek (1, 3) konumundan (8, 10) konumuna bir diyagramda bir çizgi çizin:





import matplotlib.pyplot as plt
import numpy as np



xpoints = np.array([1, 8])
ypoints = np.array([3, 10])


plt.plot(xpoints, ypoints)
plt.show()






# Sonuç olarak programi calistirdigimizda "ornek2.png" adli bir diagram cikti.

# Dikkatlice bakarsaniz x noktalari yatay olarak 1 den 8 e uzuyor. y noktalari ise dikey olarak 3 ten 10 a yukseliyor




# Yanisi ne biliyor musun? Ben biliyorum sende bil!



# X-ekseni, yatay eksendir.
# Y-ekseni, dikey eksendir.









# Cizgisiz cizim var birde biliyor musun?
# Mesela cizgi ile degilde o noktalari a ile b ile veya o yani yuvarlak gibi birseylede belirleyebiliriz



"""


Çizgisiz Çizim
--------------


Yalnızca işaretçileri çizmek için, "halkalar" anlamına gelen "o" kısayol dizesi gösterim parametresini kullanabilirsiniz
----------------------------------  ********  --------------  ** -------------------------------------------------------


"""




# Takip et bak nasil yapiyorum





import matplotlib.pyplot as plt
import numpy as np



xpoints = np.array([1, 8])
ypoints = np.array([3, 10])


plt.plot(xpoints, ypoints, 'o')
plt.show()





# Sonuç olarak karsimiza cikan "ornek3.png" adli diagrama bakin cizgi yok sadece yuvarlak halka var
# (x)  yonunde yatay olarak 1, 8 -  (y)  yonunde ise dikey olarak  3, 10 pozisyonunda duruyorlar




# Sizce sizin bilgilenmenizden mutluluk duyan ben dururmuyum yerimde! Tabiki Nooo
# Bir sonraki bölümde işaretçiler hakkında daha fazla bilgi edineceksiniz.







# Coklu Puan


"""


Çoklu Noktalar
--------------


İstediğiniz kadar nokta çizebilirsiniz, sadece her iki eksende de aynı sayıda noktaya sahip olduğunuzdan emin olun.
-------------------------------------------------------------------------------------------------------------------


"""






# Örnek Bir diyagramda (1, 3) konumundan (2, 8) konumuna, ardından (6, 1) konumuna ve son olarak (8, 10) konumuna bir çizgi çizin:






import matplotlib.pyplot as plt
import numpy as np



xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])



plt.plot(xpoints, ypoints)
plt.show()





# Sonuçumuz geldi tamda istedigimiz gibi cizdik inceleyin "ornek4.png" hemde coklu bir sekilde diyagram gayet iyi sonuc veriyor.









# Varsayilan X-Noktalari










"""



Varsayılan X-Puanları
---------------------



Eğer x eksenindeki noktaları belirtmezsek, y noktalarının uzunluğuna bağlı olarak 0, 1, 2, 3, (vb.) varsayılan değerlerini alacaklardır.


Yani, yukarıdakiyle aynı örneği alırsak ve x noktalarını dışarıda bırakırsak, diyagram şöyle görünecektir:



"""









# Örnek x noktaları olmadan çizim:





import matplotlib.pyplot as plt
import numpy



ypoints = np.array([3, 8, 1, 10, 5, 7])



plt.plot(ypoints)
plt.show()







# Sonuca dikkatlice bakin "ornek5.png" adli diyagramda x noktasinin 12345 seklinde varsayilan olarak ilerledigini gorebilirsiniz


# X-noktası [0, 1, 2, 3, 4, 5] Yukarıdaki örnekte.



# Hadi diger derse gecelim :)