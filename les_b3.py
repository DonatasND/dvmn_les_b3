import smtplib
import os
from dotenv import load_dotenv

load_dotenv('data.env')

login = os.getenv("login")
password = os.getenv("password")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.getenv('login'), os.getenv('password'))

email_to = os.getenv("email_to")


link = "https://dvmn.org/profession-ref-program/donatas.nt/8cNZ4/"
fr_name = "Андрей"
my_name = "Донатас"

mail = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

mail = mail.replace("%website%", link)
mail = mail.replace("%friend_name%", fr_name)
mail = mail.replace("%my_name%", my_name)


letter = (f"""From: {email_to}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

""" + mail).encode("UTF-8")


server.sendmail(email_to, email_to, letter)
server.quit()