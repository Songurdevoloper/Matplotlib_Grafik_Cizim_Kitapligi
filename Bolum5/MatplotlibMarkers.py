# Matplotlib Markers --> Matplotlib Isaretleyiciler






"""


işaretçiler
-----------


marker - Her noktayı belirli bir işaretleyiciyle vurgulamak için anahtar kelime bağımsız değişkenini kullanabilirsiniz :
------------------------------------------------------------------------------------------------------------------------


"""






# Ornek  Her noktayı bir daire ile işaretleyin:




import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])


plt.plot(ypoints, marker='o')
plt.show()







# Sonuc olarak "ornek6.png" adli diagrami inceleyin farkedeceksiniz marker yani isaretci cizgilerin bulusma noktalarini "o" isareti ile kapladi









# Ornek; Her noktayi bir yildizla isaretleyin!



import matplotlib.pyplot as plt
import numpy as np



ypoints = np.array([3, 8, 1, 10])



plt.plot(ypoints, marker='*')
plt.show()




# Sonuc "Ornek7.png" adli diagramda birlesim noktalarinin yildiz ile dolduruldugunu gorebilirsiniz iste marker gorevi budur








# Simdi birde marker yani isaretci referanslarina bakalim ne dersiniz?






"""


marker referance(İşaretçi Referansı)
------------------


Bu işaretçilerden herhangi birini seçebilirsiniz:
------------------------------------------------



Marker	        Description
'o'	            Circle	
'*'	            Star	
'.'	            Point	
','	            Pixel	
'x'	            X	
'X'	            X (filled)	
'+'	            Plus	
'P'	            Plus (filled)	
's'	            Square	
'D'	            Diamond	
'd'	            Diamond (thin)	
'p'	            Pentagon	
'H'	            Hexagon	
'h'	            Hexagon	
'v'	            Triangle Down	
'^'	            Triangle Up	
'<'	            Triangle Left	
'>'	            Triangle Right	
'1'	            Tri Down	
'2'	            Tri Up	
'3'	            Tri Left	
'4'	            Tri Right	
'|'	            Vline	
'_'	            Hline	



"""




# Arkadaslar bunlarin hepsini deneyebilirsiniz. Tek tek ornek yapmak isterdim ama cok zaman alacak!







# Simdi azcik dizileri bicimlendirelim






"""


Format Strings- Dizeleri Biçimlendir fmt
------------------------------------ ***


İşaretçiyi belirtmek için kısayol dizesi notasyonu parametresini de kullanabilirsiniz .
--------------------------------------------------------------------------------------

Bu parametre aynı zamanda fmt olarak da adlandırılır ve şu söz dizimi ile yazılır:
------------------------- *** ---------------------------------------------------


marker|line|color
****************


"""





# Hemen anlasilir bir ornek yapalim degil mi!





# Örnek Her noktayı bir daire ile işaretleyin:



import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])


plt.plot(ypoints, 'o:r')
plt.show()




# Sonuc olarak Simdi "ornek8.png" adli diagrama iyice bakin cizgi kirmizi oldu ve noktalarda kirmizi ayrica o gibi bir birlestirme noktasi var
# simdi soyeleyeyim bicimlendirme soyle oldu   'o:r' --> ( o -> birlesim noktasi ) ( : --> isareti bicimlendirme ) ve son olarak ( r --> kirimizi yani red anlamina geliyor)
# Yani demek istedigim sudur 'o:r' kirmizi renkte cizgi ve o ile birlesim noktasi anlamina geliyor





# İşaret değeri, yukarıdaki İşaret Referansından herhangi biri olabilir.
# Satır değeri aşağıdakilerden biri olabilir:





# Simdi Line referance  yani Hat referansina bakalim oda lazim bize ilerde zevklerimiz farkli sonucta




"""


Line Referance - Hat Referansı
-------------------------------


Line Syntax	        Description

'-'	                Solid line	
':'	                Dotted line	
'--'	            Dashed line	
'-.'	            Dashed/dotted line



Bunlari tek tek deneyebilirsiniz tek yapmaniz gereken birlesim noktasini belirledikten sonra 
o: yada o- veya o-- veyahutta o-. gibi Hat referanslari ile zevklerinizi sekillendirebilirsiniz son olarakta isterseniz

renk ekleyin nasil mesela soyle     o:b - o birlesimli ve mavi renkli :



# Not: fmt parametresinde satır değerini dışarıda bırakırsanız , hiçbir satır çizilmez.


"""




# Simdi gecelim renklere detayli olarak hadi bakim takip edin beni!!!






# Color Referance - Renk Referansi




# Kısa renk değeri aşağıdakilerden biri olabilir:



"""



Color Referance = Renk Referansı
---------------------------------


Color Syntax	    Description

'r'	                Red	
'g'	                Green	
'b'	                Blue	
'c'	                Cyan	
'm'	                Magenta	
'y'	                Yellow	
'k'	                Black	
'w'	                White	




Bunlari tek tek deneyebilirsiniz arkadaslar


"""





# Size bir oenek yaptim alin inceleyin bakalim anlamismisiniz konuyu hayal edin nasil birsey cikacagini




import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 3, 8, 10])


plt.plot(ypoints, 'o-.m')
plt.show()





# Sonuc "ornek9.png" adli diagramdan inceleyebilirsiniz gerisi sizde gayret edin hayal edin.






# Simdi Isaret boyutlarina bakalim yani nasil biraz degisiklikler yapali uzerinde degil mi?
# Hadi Baslayalim!!





"""


Marker Size - İşaret Boyutu
---------------------------


İşaretçilerin boyutunu ayarlamak için anahtar kelime bağımsız değişkenini markersize veya daha kısa sürümünü 
--------------------------------------------------------------------------**********-------------------------
ms kullanabilirsiniz:
** ----------------


"""





# Örnek İşaretçilerin boyutunu 20'ye ayarlayın:



import  matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])


plt.plot(ypoints, '1-.k', ms=20)
plt.show()




# Sonucumuz "ornek10.png" adli diagramda simdi burada ne oldu ne yaptik hatirlayin herseyi hadi!
# Sirasiyla  '1' -> Tri Down(üç aşağı) demekti.  |   -. isareti  --> Dashed/dotted line(Kesikli Noktali Cizgi demektir)
# Daha sonra    k isareti --> 'k'	Black(Siyah) anlamina geliyordu ve son olarak   ms isareti  --> markersize(işaretleyici boyutu) 20 dedik
# Hersey bu kadar sonuca bakin yani diagrama hersey kafaniza daha net oturacaktir!!!






# Simdi isaret rengine bakalim mi? yani kenar rengi diyelim isaretledik isaretledigimiz yere birde kenar rengi
# uygulamak istiyoruz. gelin gostereyim!





# Marker Color  - Isaret Rengi




"""


Marker Color  - İşaret Rengi
----------------------------


İşaretçilerin kenarının rengini ayarlamak için anahtar kelime argümanını markeredgecolor  veya daha kısa olanı kullanabilirsiniz:
------------------------------------------------------------------------ ***************-----------------------------------------
yani mec ayni anlama geliyor
---- *** -------------------


"""




# Simdi bir ornekle pekistirelim bu markeredgecolor yada turkish anlami olan kenar rengi olayini unutma kisa hali *mec*





# Ornek KENAR rengini kırmızıya ayarlayın:



import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 4, 2, 7])


plt.plot(ypoints, 'o-.', ms=20,  mec='r' )
plt.show()




# Simdi sonuca bakalim yani "ornek11.png" adli diagrama bakalim yukardaki kodlara bakarak anliyormusunuz ne yaptigimi




# Anlamanaiz gerek mesela sirasiyla neler yaptik bakalim mi?



# ypoints ekledik noktalarimiz oradaki listede ardindan o-. isareti ile noktalarin o cizgilerin ise bir cizgi bir nokta halinde
# ilerlemesi gerektigini belirttik daha sonra ms=20 yani marker size veya isaret boyutu dedik 20 olarak belirledik
# son olarakta markeredgecolor yani kenar isareti rengi onuda 'r' yani kirmizi olarak belirledik hepsi bu kadar!!









# Simdi isaretcilerin kenarinin icindeki rengi ayarlayacagiz



# İşaretçilerin kenarının içindeki rengi ayarlamak için anahtar kelime argümanını *markerfacecolor* isaret yuz rengi yani
# veya daha kısa *mfc* olanı kullanabilirsiniz:





# Ornek YÜZ rengini kırmızıya ayarlayın:








import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 5, 2, 6])

plt.plot(ypoints, marker='o', ms=20, mfc='r')
plt.show()





# Sonuc ne cikti evet tam istedigimiz gibi ic renk kirmizi oyle degil mi ornegi inceleyin bakin istedigimiz gibi hersey
# ornek diagram burada "ornek12.png" inceleyin




# Simdi her ikisi yani markerfacecolor(mfc) ve markeredgecolor(mec) yani isaret on yuzu rengi ve kenar rengi icin bakalim ne yapabiliriz








# Tüm işaretçiyi renklendirmek için hem *mec* hem de *mfc* bağımsız değişkenlerini kullanın:


# Örnek Hem kenarın hem de yüzün rengini kırmızıya ayarlayın:




import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 5, 2, 7])


plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
plt.show()






# Sonucumuz cikti simdi dikkatlice bakarsaniz mec ve mfc icin red yani kirmizi dedik yani kenar rengi artik varsayilan mavi degil
# Simdi "ornek13.png" adli diagrami inceleyebilirsiniz ic renk ve kenar rengi kirmizi olarak gorunecektir.







# Bu arada arkadaslar onaltilik renk degerleride kullanabilirsiniz
# Nasil ya diyeceksiniz mesela ozel renkler kirmizi gibi mavi gibi anarenk olmayan renkler mesela acik yesil
# Hadi deneyelim ornekle bunu






# Örnek Her noktayı güzel bir yeşil renkle işaretleyin:



import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 8, 2, 9])


plt.plot(ypoints, marker='o', ms=20, mec='#1ecca1', mfc='#1ecca1')
plt.show()




# Evet Sonuc geldi calistirin ve gorun yani bu rengin adini tahmin edin bakalim


# rgb(30, 204, 161)
# hsl(165, 74%, 46%)
# R= 1e G= cc B= a1



# boyle duruyor bunu ayarlayabilirsiniz siz rgb uzerinde sadece bulun istediginiz onaltilik rengi



# Neyse sonucumuz burda dedik ama diagrami gostermedik onuda gorun "ornek14.png" adli diagrama bakin istediklerimizi yaptik ve orada



# Bu renklerin disinda desteklenen 140 renk adından herhangi biri . html renkleri  yani yazin html color diye gorursunuz




# Ornek yapalim simdi hadi gelin asagiya






# Ornek Her noktayı "hotpink" adlı renkle işaretleyin: ---- !!!neydi bu hotpink html renkleri tamammi unutma bunu



import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 8, 2, 11])


plt.plot(ypoints, marker='o', ms=20, mec='hotpink', mfc='hotpink')
plt.show()






# Gordugunuz gibi sonucumuz geldi "ornek15.png" adli diadgrama bakin hotpink html rengi orada ayrica bir suru renk var 140 tane gidin ve baska bir renkle deneyin bunu
# Aklinizi kullanin surekli merakla bakin farkli renkler farkli seyler kesfedin iste ne bileyim yani :)))







# Bu derste bitti hadi simdi Bolum 6 yani yeni derse gecelim :)
