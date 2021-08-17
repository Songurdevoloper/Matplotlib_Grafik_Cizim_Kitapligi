# Matplotlib Pyplot     -->     Matplotlib Grafigi



# Baslamadan soylemek isterim ya plot ne abiiiii???
# Arsa yaziyor ne arsasi yaa!
# Sinirlenmeyin yada haklisiniz cok anlami var ama siz buna mantikli olarak grafik diyebilirsiniz
# Neden mi? Cunku Matplotlib Grafik cizim kitapligidir...





# Neyse Susuyorum ve direk konuya geciyoruz







# Pyplot




"""



Pyplot
-------


Matplotlib yardımcı programlarının çoğu pyplot alt modülün altında bulunur ve genellikle  plt  diğer ad altında içe aktarılır :
                                        ------                                            ---


Yani !!!



import matplotlib.pyplot as plt




Artık Pyplot paketi olarak adlandırılabilir plt.


"""





# Ama durun bir ornek yapacagim. anlasilmasi zor olsun istemiyorum! #
# Bu arada gordugunuz herseyi aciklayacagim korkmayin sakin olun!







# (0, 0) konumundan (6, 250) konumuna diyagramda bir çizgi çizin:






import matplotlib.pyplot as plt
import numpy as np



xpoints = np.array([0, 6])
ypoints = np.array([0, 250])



plt.plot(xpoints, ypoints)
plt.show()






# Calistirdiginizda cok mutlu olacaksiniz o yuzden sabret hocam :)

# Bu arada indirebilirsiniz programi calistidiktan sonra save diye bir buton var basin ve indirin istediginiz yere

# Ben size gostereyim grafigimizi  "ornek1.png" iste orada :)





# Sonraki bölümlerde çizim (çizim) hakkında daha fazla bilgi edineceksiniz.




