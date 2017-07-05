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

    gh = soup.find('form',id='docForm').find('input',id='xmlData').get('value')
    
    soup1 = BeautifulSoup(gh,'html.parser')
    
    #Значения полей для раздела 'Сведение о процедуре'
    a1 = soup1.find('purchasemaininfo').find('purchasecode').text
    a2 = soup1.find('purchasemaininfo').find('purchasetypename').text
    a3 = soup1.find('purchasemaininfo').find('purchasename').text
    a4 = None
    a5 = soup1.find('purchasemaininfo').find('regionidname').text
    a6 = None
    a7 = 'http://utp.sberbank-ast.ru/VIP'
    a8 = soup1.find('purchasemaininfo').find('purchasestatus').text

    #Массив значений полей для раздела 'Сведение о процедуре'
    mass1 = [a1,a2,a3,a4,a5,a6,a7,a8]
    
    #Значения полей для раздела 'Сведения об Организаторе'
    b1 = soup1.find('organizatorinfo').find('orgname').text
    b2 = soup1.find('organizatorinfo').find('orgfullname').text
    b3 = soup1.find('organizatorinfo').find('orginn').text
    b4 = soup1.find('organizatorinfo').find('orgkpp').text
    b5 = soup1.find('organizatorinfo').find('orgogrn').text
    b6 = soup1.find('organizatorinfo').find('orgaddressjur').text
    b7 = soup1.find('organizatorinfo').find('orgaddressfact').text
    b8 = soup1.find('organizatorinfo').find('orgemail').text
    b9 = soup1.find('organizatorinfo').find('orgphone').text
    b10 = soup1.find('organizatorinfo').find('orgcontactperson').text
    
    #Массив значений полей для раздела 'Сведения об Организаторе'
    mass2 = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]

    #Значения полей для раздела 'Сведения о заказчике'
    с1 = soup1.find('customerinfo').find('customernickname').text
    c2 = soup1.find('customerinfo').find('customerfullname').text
    c3 = soup1.find('customerinfo').find('customerinn').text
    c4 = soup1.find('customerinfo').find('customerkpp').text
    c5 = soup1.find('customerinfo').find('customeraddressjur').text
    c6 = soup1.find('customerinfo').find('customeraddressfact').text

    #Массив значений полей для раздела 'Сведения о заказчике'
    mass3 = [с1,c2,c3,c4,c5,c6]

    #Значения полей для раздела 'График проведения'
    d1 = soup1.find('purchaseplan').find('requeststartdate').text
    d2 = soup1.find('purchaseplan').find('requeststopdate').text
    d3 = soup1.find('purchaseplan').find('resultdate').text

    #Массив значений полей для раздела 'График проведения'
    mass4 = [d1,d2,d3]
    
    #Значения полей для раздела 'Сведения о лоте'
    e1 = soup1.find('bids').find('bidno').text
    e2 = soup1.find('bids').find('bidstatus').text
    e3 = soup1.find('bids').find('positionname').text
    e4 = None
    e5 = soup1.find('bids').find('currencyname').text
    e6 = soup1.find('bids').find('bidcoveramount').text
    e7 = soup1.find('bids').find('biddeposit').text
    e8 = soup.find('tbody', id = 'tblBidsbody' ).find('table', class_='block  read-only').find('tbody').find_all('td', class_='block-data')[8].text
    e9 = soup.find('tbody', id = 'tblBidsbody' ).find('table', class_='block  read-only').find('tbody').find_all('td', class_='block-data')[9].text
    e10 = soup1.find('bids').find('okpd2idname').text
    e11 = soup.find('tbody', id = 'tblBidsbody' ).find('table', class_='block  read-only').find('tbody').find_all('td', class_='block-data')[11].find('tr').text
    #Значения других полей раздела(Номер, Наименование, Количество, Начальная цена за единицу, Единица измерения)
    e_11 = soup1.find('bids').find('poscode').text
    e_12 = soup1.find('bids').find('positionname').text
    e_13 = soup1.find('bids').find('quantity').text
    e_14 = soup1.find('bids').find('positionunit').text
    #Массив значений полей для раздела 'Сведения о лоте'
    mass5 = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11]
    #Значения полей раздела 'Документы'(id для ссылок на скачивание документов)
    e12 = soup1.find('docsdiv').find('fileid').text
       
    h = soup.find('tbody')
    
    # цекл для получения описания раздела 'Сведение о процедуре'
    a = 0 
    for item in h.find_all('tr',class_='')[1:]:
         colm0 = item.find('td', class_='block-lable').text
         colm1 = mass1[0+a]
         print('    {}          [{}]'.format(colm0,colm1))
         a+=1   

    #Получение заголовка 'Сведения об организаторе' 
    title3 = soup.find('div', id='OrganizatorInfo_OrganizatorInfoDiv').find('th', class_='block-head').text
    print(title3)

    n1 = soup.find('div', class_='block-div', id='OrganizatorInfo_OrganizatorInfoDiv').find('tbody')
    
    # цекл для получения описания раздела 'Сведение об организаторе'
    b = 0
    for item1 in n1.find_all('tr')[1:]:
        colm2 = item1.find('td', class_='block-lable').text
        colm3 = mass2[0+b]
        print('    {} [{}] '.format(colm2,colm3)) 
        b+=1
     
    #Получение заголовка 'Сведения о заказчике'    
    title4 = soup.find('div', id='CustomerInfo_CustomerInfoDiv').find('th', class_='block-head').text
    print(title4)


    n2 = soup.find('div', class_='block-div', id='CustomerInfo_CustomerInfoDiv').find('tbody')

    # цекл для получения описания раздела 'Сведения о заказчике'
    c = 0
    for item2 in n2.find_all('tr')[1:]:
        colm4 = item2.find('td', class_='block-lable').text
        colm5 = mass3[0+c]
        print('    {} [{}]'.format(colm4, colm5))
        c+=1
        
    #Получение заголовка 'График проведения'   
    title5 = soup.find('div', id='PurchasePlan_PurchasePlanDiv').find('th', class_='block-head').text
    print(title5)

    n3 = soup.find('div', class_='block-div', id='PurchasePlan_PurchasePlanDiv').find('tbody')
    
    # цекл для получения описания раздела 'График проведения'
    d = 0
    for item3 in n3.find_all('tr'):
        colm5 = item3.find('td', class_='block-lable').text
        colm6 = mass4[0+d]
        print('    {} [{}]'.format(colm5, colm6))
        d+=1
        
    #Получение заголовка 'Лоты'
    title6 = soup.find('th', class_='block-tbl-th').text
    print(title6)

    #Получение подзаголовка 'Сведения о лоте'
    title6_1 = soup.find('tbody', id = 'tblBidsbody' ).find('th', class_='block-head').text
    print('   {}'.format(title6_1))
    
    
    n4 = soup.find('tbody', id = 'tblBidsbody' ).find('table', class_='block  read-only').find('tbody')
    
    # цекл для получения описания раздела 'Сведения о лоте'
    e = 0
    for item4 in n4.find_all('tr',class_='')[1:]:
       colm7 = item4.find('td', class_='block-lable')
       if colm7 is None :
           continue
       else:
          #colm8 = item4.find('td', class_='block-data').text
          colm8 = mass5[0+e]
          print('            {} [{}]'.format(colm7.text, colm8))
       e+=1  

    print('                            [               {} {} {} {}]'.format(e_11,e_12,e_13,e_14))
    #Получение заголовка 'Документы'
    title7 = soup.find('div', id='Docs_DocsDivDiv').find('th', class_='block-head').text
    print(title7)

    n5 = soup.find('div', class_='block-div', id='Docs_DocsDivDiv').find('table').find('tbody')
    
    # цекл для получения описания раздела 'Документы'
    for item5 in n5.find_all('tr'):
        colm9 = item5.find('td', class_='block-lable')
        colm10 = 'http://utp.sberbank-ast.ru/VIP/File/DownloadFile?fid='+ e12
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
    print('{}          {} '.format(title13, title14))
    
    #Цикл для получения значений полей разделов 'Дата события и 'Событие'
    for item6 in soup1.find('events'):
        colm11 = item6.find('eventdate').text
        colm12 = item6.find('eventcomment').text
        print('{}     {}'.format(colm11,colm12))
    
def main():
    parse(get_html('http://utp.sberbank-ast.ru/VIP/NBT/PurchaseView/48/0/0/245959'))
    
if __name__ == '__main__':
     main()
