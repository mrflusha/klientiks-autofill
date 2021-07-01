import time
import random

from selenium import webdriver

names_list=["Василий","Антон","Даздраперма","Инна","Валера", "Генадий","Валентин","Алексей",
"Инакентий","Авдей","Авксентий","Агафон","Акакий","Александр","Алексей","Альберт",
"Альвиан","Анатолий","Андрей","Аникита","Антон","Антонин","Анфим","Аристарх","Аркадий",
"Арсений","Артём" ,"Артемий","Артур","Архипп","Афанасий","Богдан","Борис","Вавила","Вадим",
"Валентин","Валерий","Валерьян","Варлам","Варсонофий","Варфоломей" ,"Василий","Венедикт",
"Вениамин" ,"Викентий" ,"Виктор" ,"Виссарион","Виталий","Владимир" ,"Владислав","Владлен",
"Влас","Всеволод","Вячеслав","Гавриил","Галактион","Геласий","Геннадий","Георгий","Герасим",
"Герман","Германн","Глеб","Гордей","Григорий","Данакт","Даниил" ,"Демид" ,"Демьян","Денис",
"Дмитрий","Добрыня","Донат" ,"Дорофей","Евгений","Евграф","Евдоким","Евсей","Евстафий","Егор",
"Емельян","Еремей","Ермолай","Ерофей","Ефим","Ефрем","Ждан","Зиновий","Иакинф","Иван",
"Игнатий","Игорь","Илья","Иннокентий","Ираклий" ,"Ириней","Исидор","Иуда" ,"Иулиан",
"Капитон","Ким" ,"Кир" ,"Кирилл" ,"Климент","Кондрат" ,"Конон","Константин","Корнилий",
"Кузьма","Куприян","Лаврентий","Лев" ,"Леонид","Леонтий","Логгин","Лука" ,"Лукий",
"Лукьян","Магистриан","Макар","Максим","Марк" ,"Мартын","Матвей","Мелентий","Мина" ,
"Мирон","Мирослав" ,"Митрофан","Михаил","Мстислав","Назар" ,"Нестор","Никанор","Никита","Никифор",
"Никодим" ,"Николай","Никон","Олег","Онисим","Онуфрий","Павел","Паисий","Панкратий",
"Пантелеймон","Парфений","Пафнутий","Пахомий","Пётр","Платон" ,"Поликарп" ,"Порфирий","Потап",
"Пров","Прокопий","Протасий","Прохор","Разумник","Родион","Родослав","Роман" ,
"Ростислав","Руслан","Савва","Савелий","Самуил" ,"Святополк","Святослав","Севастьян","Семён",
"Серафим","Сергей","Сила" ,"Сильвестр" ,"Созон","Софрон","Спиридон","Станислав",
"Степан","Тарас","Тимофей","Тимур","Тит","Тихон","Трифон","Трофим","Урбан" ,
"Фаддей","Фёдор","Федосей","Федот","Феликс","Феоктист","Филат","Филимон","Филипп",
"Фирс","Фока","Фома","Фотий","Фрол","Харитон","Хрисанф","Христофор","Эдуард","Эраст","Юлиан","Юрий"]



secondnames_list=["Гнида","Перефеев","Иванов","Васильев","Семёнов","Хачуян","Бородин","Иллаой", "Ларионов","Орн","Джугашвили","Ульянов"]






patron_list = ["Александрович","Алексеевич","Анатольевич","Андреевич","Антонович","Аркадьевич","Арсеньевич","Артемович","Афанасьевич",
"Богданович","Борисович","Вадимович","Валентинович","Валериевич","Васильевич","Викторович","Витальевич",
"Владимирович","Всеволодович","Вячеславович","Гаврилович","Геннадиевич","Георгиевич","Глебович","Григорьевич",
"Давыдович","Данилович","Денисович","Дмитриевич","Евгеньевич","Егорович","Емельянович","Ефимович","Иванович","Игоревич",
"Ильич","Иосифович","Кириллович","Константинович","Корнеевич","Леонидович","Львович","Макарович","Максимович",
"Маркович","Матвеевич","Митрофанович","Михайлович"]

login = ""
password = ""

def get_name():
	name = random.randrange(0, len(names_list))
	print(name,names_list[name])
	return names_list[name]
def get_family():
	family = random.randrange(0, len(secondnames_list))
	return secondnames_list[family]
def get_patron(	):
	patron = random.randrange(0, len(patron_list))
	return patron_list[patron]
def get_date():
	date = random.randrange(1,28)
	mouth = random.randrange(1,12)
	if date < 10:
		date = str(0)+str(date)
	if mouth < 10:
		mouth = str(0)+str(mouth)
	date = str(date)+str(mouth)
	return date

def get_phone():
	phone = random.randrange(9000000000,9999999999);
	return phone



driver = webdriver.Chrome('')  # Optional argument, if not specified will search path.

driver.get('https://klientiks.ru/login');

time.sleep(5) # Let the user actually see something!

log_box = driver.find_element_by_id('label-phone')
time.sleep(5) # Let the user actually see something!
pw_box = driver.find_element_by_id('label-password')
button = driver.find_element_by_css_selector("[data-id='submit']")

log_box.send_keys(login)
pw_box.send_keys(password)
button.click()

time.sleep(5)
#add_client = driver.find_element_by_css_selector("[class='b-bread_button_span']")
#menu = driver.find_element_by_css_selector("[class='b-header_clients jsClientsButton RedirectExternal']")
def get_values(i,arr):

	driver.get("https://klientiks.ru/clientix/client/default")
	time.sleep(5)
	add_client_w = driver.find_element_by_css_selector("[class='b-bread_button_span']")
	add_client_w.click()
	time.sleep(5)
	#menu.click() # Let the user actually see something!
	score = driver.find_element_by_id('label-number')
	#add_client_w = driver.find_element_by_css_selector("[class='element_field element-text_field']")
	score.click()
	score.clear()
	time.sleep(5)
	key = str(arr[i])
	score.send_keys(key)
	label_first_name = driver.find_element_by_id('label-first_name')
	label_second_name = driver.find_element_by_id('label-second_name')
	label_patron_name = driver.find_element_by_id('label-patron_name')
	label_phone = driver.find_element_by_id('label-phone')
	save_button = driver.find_element_by_css_selector("[class='b-bread_button _icon _icon_client-save _act jsSaveButtonCreate']")

	name = get_name()
	second_name = get_family()
	patron = get_patron()
	phone = get_phone()


	label_first_name.send_keys(name)
	label_second_name.send_keys(second_name)
	label_patron_name.send_keys(patron)
	label_phone.send_keys(str(phone))
	driver.execute_script("window.scrollTo(0, 2000);")
	time.sleep(5)
	label_birth_date = driver.find_element_by_id('label-birth_date')
	date = get_date()
	label_birth_date.send_keys(date)
	save_button.click()


	
arr = ["1"]
for i in range(1,3):
	arr.append(i)
	get_values(i,arr)
	time.sleep(5)
for i in range(3,51):
	arr.append(arr[i-1]+arr[i-2])
	get_values(i,arr)
	time.sleep(5)
	len(arr)




time.sleep(15)

driver.quit()