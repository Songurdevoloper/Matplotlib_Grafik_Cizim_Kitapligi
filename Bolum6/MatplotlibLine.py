# Matplotlib Line --> Matplotlib hatti veya cizgisi




# Linestyle --> Cizgi sitili



"""


çizgi stili
-----------


Çizilen satırın stilini değiştirmek için argüman anahtar sözcüğünü linestyle veya daha kısa anahtar sözcüğünü
------------------------------------------------------------------- ******** ---------------------------------
ls kullanabilirsiniz:
** -------------------



"""



# Simdi bir ornek yapalim degil mi? Ne demek istedigi anlayin yani






# Ornek Örnek Noktalı bir çizgi kullanın:



import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([4, 7, 2, 11])


plt.plot(ypoints, linestyle='dotted')
plt.show()



# Cikan sonuca bakarsaniz eger "ornek16.png" adli diagramda  linestyle(cizgi stili) = dottet(noktali) cizgi gorursunuz






# Simdi ise kesikli bir cizgi kullanacagiz bence isinize yarayabilir



import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 8, 5, 14])


plt.plot(ypoints, ls='dashed')
plt.show()




# Simdi calistirdiktan sonra gelen "ornek17.png" adli diagrama bakin
# Mesela linestyle yerine ls yazdim zaten ikiside ayni anlama geliyordu degil mi?
# Tamam anlasildim diye kabul ediyorum :)





# Simdi soyle birsey var eger ben cok tembel bir insanim diyorsaniz onada cozum var :d




# Shorter Syntax --> Kisa Sozdimi



"""


Shorter Syntax --> Kısa Sözdizimi
---------------------------------



Çizgi stili daha kısa bir söz dizimiyle yazılabilir:
----------------------------------------------------

linestyle -->  ls olarak yazılabilir .

dotted --> ':' olarak yazılabilir .

dashed --> '--' olarak yazılabilir.



Yani kisayol cok yeterki isteyin ama unutmayin!!!



Simdi yine ornek yapacagiz bunla alakali eliniz gozunuz alissin!
----------------------------------------------------------------


"""






# Örnek Daha kısa sözdizimi:



import matplotlib.pyplot as plt
import numpy as np



ypoints = np.array([2, 9, 5, 18])


plt.plot(ypoints, ls=':')
plt.show()




# Bak simdi "ornek18.png" adli diagrama ayni islemi sadece 4 parmak hareketiyle veya 4 tusla hallettik
# Simdi size cizgi stillerini gosterecegim bunlar size cok lazim olacak...







# Line Styles --> Cizgi Stilleri





"""


# Line Styles --> Cizgi Stilleri
--------------------------------


Bu stillerden herhangi birini seçebilirsiniz:
*********************************************



Style	                    Or

'solid' (default)	        '-'	
'dotted'	                ':'	
'dashed'	                '--'	
'dashdot'	                '-.'	
'None'	                     ''




Bence burayi anladik uzun hali ve kisa hali var iste hanimlar beyler bu kadar fazla dusunmeyin!!


"""




# Yeni seyler ogrenmeye devam simdi Cizgi Renklerine biraz bakalim ve ogrenelim nasil yapacagimizi!!





#Line Color --> Cizgi Rengi



"""


#Line Color --> Cizgi Rengi
---------------------------



Çizginin rengini ayarlamak için anahtar kelime argümanını color veya daha kısasını  c  kullanabilirsiniz:
--------------------------------------------------------- ***** ------------------ ***


Tamam bence mantigi anladik yani c veya color baska birsey yok tembeller icin color caliskanlar icin c !!

"""



# Simdi bir oenkle yolumuza devam edecegiz basamak basamak hayallerime dogru kosacagiz!





# Ornek Çizgi rengini kırmızıya ayarlayın:




import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([2, 9, 4, 13])


plt.plot(ypoints, color='r')
plt.show()




# Cok basit degil mi? Simdi c yazabilirdim ama bende bir sure siz alisana kadar tembel takilacagim
# Unutmayin pratik yolu varken hamballik yapmaya hic gerek yok ayni islem c='r' diye hemencik olabilirdi!!1
# Neyse "ornek19.png" adli diagrama bakin istedigimiz renk tam cizginin ustunde duruyor






# Bu arada Onaltılık renk değerlerini de kullanabilirsiniz :






# Ornek Güzel bir yeşil çizgi ile grafik:




import matplotlib.pyplot as plt
import numpy as np




ypoints = np.array([3, 9, 1, 10])



plt.plot(ypoints, c='#4CAF50')
plt.show()






# Simdi calistirdiktan sonra onumuze cikan "ornek20.png" adli diagrama bakin cok guzel bir renk iste tek
# yapmaniz gereken bu renkleri bulmak cok basit sadece rgb yazip 16 sistemde neye karsilik geldiklerini bulun
# hatta buklmayin otomatik gosteriyor zaten!!!




# Bu arada desteklenen 140 renk adından herhangi biride olabilir .




# Hatirlamaniz adina ornek veriyorum!




# Örnek "Hotpink" adlı renkle grafik:





import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([2, 5, 1, 8])


plt.plot(ypoints, c='hotpink')
plt.show()




# Iste geldi "ornek21.png" adli diagramimizdaki hotpink !!!!
# Hatirladin bence hatirlamadiysan geri don ve anlayarak gel bence!


# Simdik ne yapacagiz ne kaldi hmmm evet cizgi genisligi!!






# Line Width --> Cizgi Genisligi



"""


# Line Width --> Cizgi Genisligi
--------------------------------


Çizginin genişliğini değiştirmek için anahtar kelime argümanını   linewidth   veya daha kısa   lw  olanı kullanabilirsiniz.
----------------------------------------------------------------- ********* ----------------- ***** ---------------

Değer, nokta cinsinden kayan bir sayıdır:
-----------------------------------------




Hemen gel ornek vereyim hic kafan karismasin haydi haydii !!


"""





# 20,5 punto genişliğinde bir çizgi ile grafik:




import matplotlib.pyplot as plt
import numpy as np




ypoints = np.array([2, 8, 3, 10, 2])


plt.plot(ypoints, linewidth='20.5')
plt.show()




# Simdi Sonuca bakalim "" adli diagrama baktiginizda cizgi genisligi 20.5 punto olarak ayarlandi tamamdir ama
# unutma bak lw kisayolu var zaman coksa linewidth yazabilirsin. Neyse bu arada adim muhammed adimin bas harfini
# gorursun artik sekilli bir sekilde bu arada oyun oynamiyoruz hee sen x ve y noktalarina odaklan :d



# Simdi bak yeni birsey ogrenecegiz artik iki tane cizgimiz olacak onlarla ugrasacagiz !!






# Multiple Lines --> Coklu Cizgiler




"""



# Multiple Lines --> Coklu Cizgiler
-----------------------------------



Daha fazla plt.plot() işlev ekleyerek istediğiniz kadar satır çizebilirsiniz :
----------- ********* --------------------------------------------------------


Cok basit degil mi hanimlar beyler sunu yapiyoruz bak




y1 = bilmem bilmem nee
plt.plot(y1, bilmem bilmem ne)

simdi yapmamiz gereken tek sey 

y2 = bla bla bla 
plt.plot(y2, bla bla)



yani basit ya yeni bir y cizgisi ve plot yani grafik cizgisi olusturuyoruz
---------------------------------------------------------------------------


Ornek verecegim korkmayin basit bu konular!!


"""





# Ornek plt.plot() Her satır için bir fonksiyon belirterek iki satır çizin :



import matplotlib.pyplot as plt
import numpy as np


y1 = np.array([1, 5, 3, 6])
y2 = np.array([2, 6, 4, 8])


plt.plot(y1)
plt.plot(y2)

plt.show()





# Cikan sonucumuz "ornek23.png" adli diagramimizda iki tane cizgi var birde farkettiysen renk degisimi otomatik :)
# Arkadaslar bence cok basit ya degil mi?
# Lutfen konulari anlayarak gelin hersey basit kendinize eziyet etmeyin tamam mi?




"""


Bu arada;


Aynı plt.plot() fonksiyonda her çizgi için x ve y ekseni noktalarını ekleyerek birçok çizgi çizebilirsiniz .


(Yukarıdaki örneklerde sadece y eksenindeki noktaları belirledik, yani x eksenindeki noktalar varsayılan değerleri 
(0, 1, 2, 3) aldı.)


x ve y değerleri çiftler halinde gelir:



Gelin ornege anlayin bakalim!!


"""





# Simdi ornegi baslatmadan once sunu soyleyeyim bakin aslinda x her zaman var yani otomatik 1234 diye deger ekliyor
# O yuzden kafaniz karismasin bundan dolayi






# Ornek  Her iki çizgi için de x ve y noktası değerlerini belirterek iki çizgi çizin:



import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([0, 1, 2, 3])
y1 = np.array([1, 5, 3, 6])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([2, 6, 4, 8])


plt.plot(x1, y1, x2, y2)
plt.show()





# Simdi ciktiya yani "ornek24.png" adli diyagrama iyice bakin ornek23.png ile hicbir farki yok cunku x degeri eger biz deger
# vermessek her zaman varsayilandir yani 0, 1, 2, 3, 4 vs vs






# Bu bolumde bitti hadi Bolum7 ye gelin <3

