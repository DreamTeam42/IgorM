from bs4 import BeautifulSoup
import requests


def get_html(url):
    return requests.get(url).text
    
    
def parse(html):
    
    soup = BeautifulSoup(html,'html.parser')
    
    #Получение заголовка структуры всего описания
    title1 = soup.find('h2').text
    print(title1)
    
    #Получение заголовка 'Сведение о процедуре'
    title2 = soup.find('th', class_='block-head').text
    print(title2)

    h = soup.find('tbody')

    # цекл для получения описания раздела 'Сведение о процедуре' 
    for item in h.find_all('tr',class_='')[1:]:
         colm0 = item.find('td', class_='block-lable').text
         colm1 = item.find('td', class_='block-data').text
         print('    {}  [{}]'.format(colm0, colm1))


    #Получение заголовка 'Сведения об организаторе' 
    title3 = soup.find('div', id='OrganizatorInfo_OrganizatorInfoDiv').find('th', class_='block-head').text
    print(title3)

    n1 = soup.find('div', class_='block-div', id='OrganizatorInfo_OrganizatorInfoDiv').find('tbody')
    
    # цекл для получения описания раздела 'Сведение об организаторе'
    for item1 in n1.find_all('tr')[1:]:
        colm2 = item1.find('td', class_='block-lable').text
        colm3 = item1.find('td', class_='block-data').text
        print('    {} [{}]'.format(colm2, colm3))

        

    #Получение заголовка 'Сведения о заказчике'    
    title4 = soup.find('div', id='CustomerInfo_CustomerInfoDiv').find('th', class_='block-head').text
    print(title4)


    n2 = soup.find('div', class_='block-div', id='CustomerInfo_CustomerInfoDiv').find('tbody')

    # цекл для получения описания раздела 'Сведения о заказчике'
    for item2 in n2.find_all('tr')[1:]:
        colm4 = item2.find('td', class_='block-lable').text
        colm5 = item2.find('td', class_='block-data').text
        print('    {} [{}]'.format(colm4, colm5))

    #Получение заголовка 'График проведения'   
    title5 = soup.find('div', id='PurchasePlan_PurchasePlanDiv').find('th', class_='block-head').text
    print(title5)

    n3 = soup.find('div', class_='block-div', id='PurchasePlan_PurchasePlanDiv').find('tbody')
    
    # цекл для получения описания раздела 'График проведения'
    for item3 in n3.find_all('tr'):
        colm5 = item3.find('td', class_='block-lable').text
        colm6 = item3.find('td', class_='block-data').text
        print('    {} [{}]'.format(colm5, colm6))

    #Получение заголовка 'Лоты'
    title6 = soup.find('th', class_='block-tbl-th').text
    print(title6)

    #Получение подзаголовка 'Сведения о лоте'
    title6_1 = soup.find('tbody', id = 'tblBidsbody' ).find('th', class_='block-head').text
    print('   {}'.format(title6_1))
    
    
    n4 = soup.find('tbody', id = 'tblBidsbody' ).find('table', class_='block  read-only').find('tbody')
    
    # цекл для получения описания раздела 'Сведения о лоте'
    for item4 in n4.find_all('tr',class_='')[1:]:
       colm7 = item4.find('td', class_='block-lable')
       if colm7 is None :
           continue
       else:
          colm8 = item4.find('td', class_='block-data').text 
          print('            {} [{}]'.format(colm7.text, colm8))

    
    #Получение заголовка 'Документы'
    title7 = soup.find('div', id='Docs_DocsDivDiv').find('th', class_='block-head').text
    print(title7)

    n5 = soup.find('div', class_='block-div', id='Docs_DocsDivDiv').find('table').find('tbody')
    
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
