# import urllib.request
from bs4 import BeautifulSoup
import requests

def get_html(url):
    return requests.get(url).text
    # response = urllib.request.urlopen(url)
    # return response.read()

def parse(html):
    
    soup = BeautifulSoup(html,'html.parser')
    #Получение заголовка структуры всего описания
    title1 = soup.find('h2')
    print(title1.text)
    
    #Получение заголовка 'Сведение о процедуре'
    title2 = soup.find('th', class_='block-head')
    print(title2.text)

    h = soup.find('tbody')
    nb = h.find_all('tr')[1:]

    # цекл для получения описания раздела 'Сведение о процедуре' 
    for item in h.find_all('tr')[1:]:
       colm0 = item.find('td', class_='block-lable')
       colm1 = item.find('td', class_='block-data')
       print(colm0.text)
       print(colm1.text)


    #Получение заголовка 'Сведения об организаторе' 
    div1 = soup.find('div', id='OrganizatorInfo_OrganizatorInfoDiv')
    title3 = div1.find('th', class_='block-head')
    print(title3.text)

    n1 = soup.find('div', class_='block-div', id='OrganizatorInfo_OrganizatorInfoDiv')
    j1 = n1.find('tbody')
    m1 = j1.find_all('tr')[1:]

    # цекл для получения описания раздела 'Сведение об организаторе'
    for item1 in j1.find_all('tr')[1:]:
        colm2 = item1.find('td', class_='block-lable')
        colm3 = item1.find('td', class_='block-data')
        print(colm2.text)
        print(colm3.text)

        

    #Получение заголовка 'Сведения о заказчике'    
    div = soup.find('div', id='CustomerInfo_CustomerInfoDiv')
    title4 = div.find('th', class_='block-head')
    print(title4.text)


    n2 = soup.find('div', class_='block-div', id='CustomerInfo_CustomerInfoDiv')
    j2 = n2.find('tbody')
    m2 = j2.find_all('tr')[1:]

    # цекл для получения описания раздела 'Сведения о заказчике'
    for item2 in j2.find_all('tr')[1:]:
        colm4 = item2.find('td', class_='block-lable')
        colm5 = item2.find('td', class_='block-data')
        print(colm4.text)
        print(colm5.text)

    #Получение заголовка 'График проведения'   
    div2 = soup.find('div', id='PurchasePlan_PurchasePlanDiv')
    title5 = div2.find('th', class_='block-head')
    print(title5.text)

    n3 = soup.find('div', class_='block-div', id='PurchasePlan_PurchasePlanDiv')
    j3 = n3.find('tbody')
    m3 = j3.find_all('tr')
    
    # цекл для получения описания раздела 'График проведения'
    for item3 in j3.find_all('tr'):
        colm5 = item3.find('td', class_='block-lable')
        colm6 = item3.find('td', class_='block-data')
        print(colm5.text)
        print(colm6.text)

    #Получение заголовка 'Лоты'
    div3 = soup.find('th', class_='block-tbl-th')
    print(div3.text)

    #Получение подзаголовка 'Сведения о лоте'
    div4 = soup.find('div', class_='block-div', id='BidsInfo_BidInfoDiv_3174804')
    title6 = div4.find('th', class_='block-head')
    print(title6.text)
    
    # цекл для получения описания раздела 'Сведения о лоте'
    n4 = soup.find('div', class_='block-div',id='BidsInfo_BidInfoDiv_3174804')
    j4 = n4.find('tbody')
    m4 = j4.find_all('tr')[1:]
    for item4 in j4.find_all('tr')[1:]:
       colm7 = item4.find('td', class_='block-lable')
       if colm7 is None:
           continue
       else:
        print(colm7.text)
       colm8 = item4.find('td', class_='block-data')
       print(colm8.text)

    
    #Получение заголовка 'Документы'
    div5 = soup.find('div', id='Docs_DocsDivDiv')
    title7 = div5.find('th', class_='block-head')
    print(title7.text)

    n5 = soup.find('div', class_='block-div', id='Docs_DocsDivDiv')
    j5 = n5.find('table')
    m5 = j5.find('tbody')
    k5 = m5.find_all('tr')
    
    # цекл для получения описания раздела 'Документы'
    for item5 in m5.find_all('tr'):
        colm9 = item5.find('td', class_='block-lable')
        colm10 = item5.find('span', id='Docs_flDocsFileName')
        if colm9 is None:
         continue
        else:
         print(colm9.text)
         print(colm10.text)
         
    #Заголовки 'Дата поступления запросов','Тема запроса','Текст запроса','Дата разъяснения','Разъяснение'
    title8 = soup.find('thead',id='tblExplanationRequestshead')
    print(title8.text)
    
    #Заголовки 'Посмотреть', 'Наименование протокола', 'Дата подписания протокола на площадке', 'Статус протокола'
    title9 = soup.find('thead', id='tblProtocolInfohead')
    print(title9.text)
    
    #Заголовки 'Дата события' , 'Событие'
    title10 = soup.find('tr',id='hTableEvents_Eventsrow')
    print(title10.text)
    #Описание заголовков 'Дата события' и 'Событие'
    val1=soup.find('tbody',id='tblEventsbody')
    print(val1.text)
    
def main():
    parse(get_html('http://utp.sberbank-ast.ru/VIP/NBT/PurchaseView/48/0/0/245959'))
    
if __name__ == '__main__':
     main()
