from bs4 import BeautifulSoup
import requests
import re

def get_html(url):
    return requests.get(url).text
    
    
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
       colm0 = item.find('td', class_='block-lable').text
       colm1 = item.find('td', class_='block-data').text
       print('    {} [{}]'.format(colm0, colm1))


    #Получение заголовка 'Сведения об организаторе' 
    div1 = soup.find('div', id='OrganizatorInfo_OrganizatorInfoDiv')
    title3 = div1.find('th', class_='block-head')
    print(title3.text)

    n1 = soup.find('div', class_='block-div', id='OrganizatorInfo_OrganizatorInfoDiv').find('tbody')
    j1 = n1.find_all('tr')[1:]
    

    # цекл для получения описания раздела 'Сведение об организаторе'
    for item1 in n1.find_all('tr')[1:]:
        colm2 = item1.find('td', class_='block-lable').text
        colm3 = item1.find('td', class_='block-data').text
        print('    {} [{}]'.format(colm2, colm3))

        

    #Получение заголовка 'Сведения о заказчике'    
    div = soup.find('div', id='CustomerInfo_CustomerInfoDiv')
    title4 = div.find('th', class_='block-head')
    print(title4.text)


    n2 = soup.find('div', class_='block-div', id='CustomerInfo_CustomerInfoDiv').find('tbody')
    m2 = n2.find_all('tr')[1:]

    # цекл для получения описания раздела 'Сведения о заказчике'
    for item2 in n2.find_all('tr')[1:]:
        colm4 = item2.find('td', class_='block-lable').text
        colm5 = item2.find('td', class_='block-data').text
        print('    {} [{}]'.format(colm4, colm5))

    #Получение заголовка 'График проведения'   
    div2 = soup.find('div', id='PurchasePlan_PurchasePlanDiv')
    title5 = div2.find('th', class_='block-head')
    print(title5.text)

    n3 = soup.find('div', class_='block-div', id='PurchasePlan_PurchasePlanDiv').find('tbody')
    m3 = n3.find_all('tr')
    
    # цекл для получения описания раздела 'График проведения'
    for item3 in n3.find_all('tr'):
        colm5 = item3.find('td', class_='block-lable').text
        colm6 = item3.find('td', class_='block-data').text
        print('    {} [{}]'.format(colm5, colm6))

    #Получение заголовка 'Лоты'
    div3 = soup.find('th', class_='block-tbl-th')
    print(div3.text)

    #Получение подзаголовка 'Сведения о лоте'
    div4 = soup.find('div', class_='block-div', id='BidsInfo_BidInfoDiv_3174804')
    title6 = div4.find('th', class_='block-head').text
    print('   {}'.format(title6))
    
    
    n4 = soup.find('div', class_='block-div',id='BidsInfo_BidInfoDiv_3174804').find('tbody')
    m4 = n4.find_all('tr')[1:]
    
    # цекл для получения описания раздела 'Сведения о лоте'
    for item4 in n4.find_all('tr')[1:]:
       colm7 = item4.find('td', class_='block-lable')
       if colm7 is None:
           continue
       else:
       #print(colm7.text)
          colm8 = item4.find('td', class_='block-data').text 
          print('            {} [{}]'.format(colm7.text, colm8))

    
    #Получение заголовка 'Документы'
    div5 = soup.find('div', id='Docs_DocsDivDiv')
    title7 = div5.find('th', class_='block-head')
    print(title7.text)

    n5 = soup.find('div', class_='block-div', id='Docs_DocsDivDiv').find('table').find('tbody')
    m5 = n5.find_all('tr')
    
    # цекл для получения описания раздела 'Документы'
    for item5 in n5.find_all('tr'):
        colm9 = item5.find('td', class_='block-lable')
        colm10 = item5.find('span', id='Docs_flDocsFileName').text
        if colm9 is None:
         continue
        else:
         print('    {} [{}]'.format(colm9.text, colm10))
         
    #Заголовки 'Дата поступления запросов','Тема запроса','Текст запроса','Дата разъяснения','Разъяснение'
    title8 = soup.find('thead',id='tblExplanationRequestshead')
    print(title8.text)

    
    
    #Заголовки 'Посмотреть', 'Наименование протокола', 'Дата подписания протокола на площадке', 'Статус протокола'
    title9 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolView').text
    title10 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolName').text
    title11 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolDate').text
    title12 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolStatus').text
    print('{} {} {} {} '.format(title9, title10, title11, title12))
    
    #Заголовки 'Дата события' , 'Событие'
    title13 = soup.find('tr',id='hTableEvents_Eventsrow').find('th',id='Events_thEventDate').text
    title14 = soup.find('tr',id='hTableEvents_Eventsrow').find('th',id='Events_thEventComment').text
    print('{} {} '.format(title13, title14))
    
    #Описание заголовков 'Дата события' и 'Событие'
    val1=soup.find('tbody',id='tblEventsbody')
    print(val1.text)

    
def main():
    parse(get_html('http://utp.sberbank-ast.ru/VIP/NBT/PurchaseView/48/0/0/245959'))
    
if __name__ == '__main__':
     main()
