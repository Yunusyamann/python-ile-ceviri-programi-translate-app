from tkinter import *  #gerekli kutuphaneleri import ediyoruz.
from tkinter import ttk, messagebox
from googletrans import Translator

translator = Translator()
#açılır pencere ayarları
pencere = Tk()
pencere.title("CEVİRİ ARACI")
pencere.minsize(600, 500)
pencere.maxsize(600, 500)
#çevirme için fonksiyonu yazıyoruz.
def translate():
    try:
        txt = text1.get(1.0, END)
        c1 = combo1.get()
        c2 = combo2.get()
        if txt:
            result = translator.translate(txt, src=c1, dest=c2)
            text2.delete(1.0, END)
            text2.insert(END, result.text)
    except Exception as e:
        messagebox.showerror("Error", "Çeviri yapılırken bir hata oluştu. Lütfen tekrar deneyin.")
#burayı kullanmasak da olur du ama program anlamadığım şekilde geç açılıyordu, bu şekilde liste yapınca sorun düzeldi.
language_options = [
    "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian", "Bengali",
    "Bosnian", "Bulgarian", "Catalan", "Cebuano", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)",
    "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto", "Estonian", "Filipino", "Finnish",
    "French", "Frisian", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian Creole", "Hausa", "Hawaiian",
    "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian", "Irish", "Italian", "Japanese",
    "Javanese", "Kannada", "Kazakh", "Khmer", "Korean", "Kurdish", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian",
    "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Mongolian",
    "Myanmar (Burmese)", "Nepali", "Norwegian", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian",
    "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho", "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian",
    "Somali", "Spanish", "Sundanese", "Swahili", "Swedish", "Tajik", "Tamil", "Telugu", "Thai", "Turkish",
    "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"
]
#1. seçim box ının ayarlarını yapıyoruz.
combo1 = ttk.Combobox(pencere, values=language_options, state='r')
combo1.place(x=100, y=20)
combo1.set("Dil seçiniz")

f1 = Frame(pencere, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)
#çevireceğimiz yazının olduğu kutucuktaki text ayarlarını yapıyoruz.
text1 = Text(f1, font="Roboto 14 ", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)
#2. seçim box ının ayarlarını yapıyoruz.
combo2 = ttk.Combobox(pencere, values=language_options, state='r')
combo2.place(x=300, y=20)
combo2.set("Dil seçiniz")

f2 = Frame(pencere, bg='black', bd='4')
f2.place(x=300, y=100, width=150, height=150)
#çevirilen yazının olduğu kutucuktaki text ayarlarını yapıyoruz.
text2 = Text(f2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)
# buton ayarları ve butona basıldığında verilen komutun nasıl işlediğini gösteriyoruz.
button = Button(pencere, text='ÇEVİR', font=('normal', 15), bg='yellow', command=translate)
button.place(x=230, y=300)

pencere.mainloop() # açılır pencereyi loop a alıyoruz.

