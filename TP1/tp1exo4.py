nbminutes=float(input("Entrez le nombre de minutes:"))
jour=nbminutes//60*24
minutes=nbminutes%(60*24)%60
heure=nbminutes%(60*24)//60


print(jour , heure , minutes)





