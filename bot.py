import requests
from bs4 import BeautifulSoup
import telegram

r = requests.get("https://forum.donanimhaber.com/api2/GlobalApi/GetMorePopularSicakFirsatTopics?type=2&skip=0")
html = r.json()["Data"]["Html"]

source = BeautifulSoup(html, "lxml")
topics = source.find_all("a", attrs={"class":"satirikapla"})
result_str = ""
for topic in topics:
    title = topic.findChildren("div" , recursive=False)[0].text
    result_str += "title" + ": https://forum.donanimhaber.com" + topic["href"]+ "\n\n"

bot = telegram.Bot("bot_key")
bot.send_message(chat_id="chat_id", text=result_str)
