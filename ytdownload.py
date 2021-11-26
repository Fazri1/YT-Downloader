from pytube import YouTube

link = input("Masukkan link : ")
resolusi = input("Resolusi : ")
yt = YouTube(link)
yt.streams.filter(res=resolusi).first().download()

