from bs4 import BeautifulSoup
import requests
import json

def get_html(url):

    return requests.get(url).text

def parse(html):

    soup = BeautifulSoup(html,'html.parser')
    gh = soup.find('form',id='docForm').find('input',id='xmlData').get('value')
    soup1 = BeautifulSoup(gh,'html.parser')
     
    infoArr = []
    info = {}
    index = 0   
                   
    #Получение заголовка структуры всего описания
    title1 = soup.find('h2').text
    info[index] = title1
    index+=1
    print(title1)

    #Получение заголовка 'Сведение о процедуре'
    title2 = soup.find('th', class_='block-head').text
    info[index]= title2
    index+=1
    print(title2)

    #Значения полей для раздела 'Сведение о процедуре'
    a1 = soup1.find('purchasemaininfo').find('purchasetypename').text   
    a2 = soup1.find('purchasemaininfo').find('purchasecode').text
    a3 = soup1.find('purchasemaininfo').find('purchasename').text
    a4 = soup1.find('purchasemaininfo').find('purchaseamount')
    if a4 is None:
      a4 = None
    else:
      a4 = soup1.find('purchasemaininfo').find('purchaseamount').text
    a5 = soup1.find('purchasemaininfo').find('regionidname').text
    a6 = None
    a7 = 'Да/Нет'
    a8 = 'http://utp.sberbank-ast.ru/VIP'
    a9 = soup1.find('purchasemaininfo').find('purchasestatus').text
    
    #Массив значений полей для раздела 'Сведение о процедуре'
    mass1 = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a9]

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

    #Значения полей для раздела 'Сведения о лоте'
    e1 = soup1.find('bids').find('bidno').text
    e2 = soup1.find('bids').find('bidstatus').text
    e3 = soup1.find('bids').find('positionname').text
    e4 = soup1.find('bids').find('bidpricenotreq')
    if e4!=None:
        e4 = soup1.find('bids').find('bidpricenotreq').text
    else:
      e4=None 
    e5 = soup1.find('bids').find('currencyname').text
    e6 = soup1.find('bids').find('bidcoveramount').text
    e7 = soup1.find('bids').find('biddeposit').text
    e8 = soup.find('div',class_='block-tbl-div').find('tbody', id = 'tblBidsbody' ).find('table', class_='block read-only').find_all('td',class_='block-data')[7].text
    e9 = soup1.find('auctionstepminpercent').text                                        
    e10 = soup1.find('auctionstepmaxpercent').text                                                                              
    e11 = soup1.find('firstofferperiod').text 
    e12 = soup1.find('offerperiod').text
    e13 = 'Да/Нет'
    e14 = soup.find('div',class_='block-tbl-div').find('tbody', id = 'tblBidsbody' ).find('table', class_='block read-only').find_all('td', class_='block-data')[13].text
    e15 = soup.find('div',class_='block-tbl-div').find('tbody', id = 'tblBidsbody' ).find('table', class_='block read-only').find_all('td', class_='block-data')[14].text
    e16 = soup.find('div',class_='block-tbl-div').find('tbody', id = 'tblBidsbody' ).find('table', class_='block read-only').find_all('td', class_='block-data')[15].find('thead').text
    #Массив значений полей для раздела 'Сведения о лоте'
    mass5 = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]

    #Значения полей для раздела 'График проведения'
    d1 = soup1.find('purchaseplan').find('requeststartdate').text
    d2 = soup1.find('purchaseplan').find('requeststopdate').text
    d3 = soup1.find('purchaseplan').find('resultdate')
    d4 = soup1.find('purchaseplan').find('auctiondate')
    if d3 is None:
        d3 = soup1.find('purchaseplan').find('requestreviewdate').text
        #Массив значений полей для раздела 'График проведения'
        mass4 = [d1,d2,d3]
    else:
        d3 = soup1.find('purchaseplan').find('resultdate').text
        #Массив значений полей для раздела 'График проведения'
        mass4 = [d1,d2,d3]
    if d4!= None:
       d4 = soup1.find('purchaseplan').find('auctiondate').text
       #Массив значений полей для раздела 'График проведения'
       mass4 = [d1,d2,d3]
       mass4.append(d4)
                      
    #Значения других полей раздела(Номер, Наименование, Количество, Начальная цена за единицу, Единица измерения)
    e_11 = soup1.find('bids').find('poscode').text
    e_12 = soup1.find('bids').find('positionname').text
    e_13 = soup1.find('bids').find('quantity').text
    e_14 = soup1.find('bids').find('maxprice').text
    e_15 = soup1.find('bids').find('positionunit').text
    e_16 = soup1.find('posauctionstepmin').text
    e_17 = soup1.find('posauctionstepmax').text
    e_18 = soup1.find('astepminpercent').text
    e_19 = soup1.find('astepmaxpercent').text
    #Значения полей раздела 'Документы'(id для ссылок на скачивание документов)
    e13 = soup1.find('docsdiv').find_all('fileid')
    #Массив для id
    mass6 = list()
    #Цикл для занесения всех id в отдельный массив
    q = 0
    for v in e13:
       t = v.text
       mass6.append(t)
       q+=1

    h = soup.find('div',class_='block-div').find('tbody')

    # цекл для получения описания раздела 'Сведение о процедуре'
    a = 0
    for item in h.find_all('tr',class_=''):
         colm0 = item.find('td', class_='block-lable').text
         colm1 = mass1[0+a]
         print('    {}          [{}]'.format(colm0,colm1))
         info[index] = ('    {}          [{}]'.format(colm0,colm1))
         index+=1
         a+=1

    #Получение заголовка 'Сведения об организаторе'
    title3 = soup.find('div', id='OrganizatorInfo_OrganizatorInfoDiv').find('th', class_='block-head').text
    info[index] = title3
    index+=1
    print(title3)

    n1 = soup.find('div', class_='block-div', id='OrganizatorInfo_OrganizatorInfoDiv').find('tbody')

    # цекл для получения описания раздела 'Сведение об организаторе'
    b = 0
    for item1 in n1.find_all('tr')[1:]:
        colm2 = item1.find('td', class_='block-lable').text
        colm3 = mass2[0+b]
        print('    {} [{}] '.format(colm2,colm3))
        info[index] = ('    {} [{}] '.format(colm2,colm3))
        index+=1
        b+=1

    #Получение заголовка 'Сведения о заказчике'
    title4 = soup.find('div', id='CustomerInfo_CustomerInfoDiv').find('th', class_='block-head').text
    info[index] = title4
    index+=1
    print(title4)


    n2 = soup.find('div', class_='block-div', id='CustomerInfo_CustomerInfoDiv').find('tbody')

    # цекл для получения описания раздела 'Сведения о заказчике'
    c = 0
    for item2 in n2.find_all('tr')[1:]:
        colm4 = item2.find('td', class_='block-lable').text
        colm5 = mass3[0+c]
        print('    {} [{}]'.format(colm4, colm5))
        info[index]  = ('    {} [{}]'.format(colm4, colm5))
        index+=1
        c+=1

    #Получение заголовка 'График проведения'
    title5 = soup.find('div', id='PurchasePlan_PurchasePlanDiv').find('th', class_='block-head').text
    info[index] = title5
    index+=1
    print(title5)

    n3 = soup.find('div', class_='block-div', id='PurchasePlan_PurchasePlanDiv').find('tbody')

    # цекл для получения описания раздела 'График проведения'
    d = 0
    for item3 in n3.find_all('tr'):
        colm5 = item3.find('td', class_='block-lable').text
        colm6 = mass4[0+d]
        print('    {} [{}]'.format(colm5, colm6))
        info[index] = ('    {} [{}]'.format(colm5, colm6))
        index+=1
        d+=1

    #Получение заголовка 'Лоты'
    title6 = soup.find('th', class_='block-tbl-th').text
    info[index] = title6
    index+=1
    print(title6)

    #Получение подзаголовка 'Сведения о лоте'
    title6_1 = soup.find('tbody', id = 'tblBidsbody' ).find('th', class_='block-head').text
    info[index] = ('   {}'.format(title6_1))
    index+=1
    print('   {}'.format(title6_1))


    n4 = soup.find('tbody', id = 'tblBidsbody' ).find('table', class_='block read-only').find('tbody')

    # цекл для получения описания раздела 'Сведения о лоте'
    e = 0
    colm_7 = soup1.find('regions')
    for item4 in n4.find_all('tr',class_=''):
       colm7 = item4.find('td', class_='block-lable')
       rt = soup1.find('bids').find('okpd2idname').text
       if colm7 is None :
           continue
       if e==14 :
           if rt!='':
              colm8 = mass5[14]    
              print('        {}   [{}]'.format(colm7.text,colm8))
              print('                                                                               {}'.format(rt))
              info[index] = ('        {}   [{}]'.format(colm7.text,colm8))
              index+=1
              info[index] = ('                                                                               {}'.format(rt))
           else:
             colm8 = mass5[14]  
             print('        {}   [{}]'.format(colm7.text,colm8))  
             print('                            {}'.format('Инфромация отсутствует'))
             info[index] = ('        {}   [{}]'.format(colm7.text,colm8))
             index+=1
             info[index] = ('                            {}'.format('Инфромация отсутствует'))
       else:     
         if e==15:
            colm8 = mass5[15]
            print('        {}    [{}]'.format(colm7.text,colm8))
            print('                           [   {} {}  {}  {}  {}  {}     {}     {}    {}]'.format(e_11,e_12,e_13,e_14,e_15,e_16,e_17,e_18,e_19))
            info[index] = ('        {}    [{}]'.format(colm7.text,colm8))
            index+=1
            info[index] = ('                           [   {} {}  {}  {}  {}  {}    {}    {}    {}]'.format(e_11,e_12,e_13,e_14,e_15,e_16,e_17,e_18,e_19))   
         else:
           if e==13 and colm_7!=None:
             colm8 = mass5[13]
             print('        {} [{}]'.format(colm7.text,colm8))
             info[index] = ('        {} [{}]'.format(colm7.text,colm8))
             index+=1
             for l in soup1.find('regions').find_all('region'):
                 colm_8 = l.find('regionidname').text
                 if colm_8=='':
                     print('                                    {}'.format('Инфромация отсутствует'))
                     info[index] = ('                                    {}'.format('Инфромация отсутствует'))
                     index+=1
                 else:    
                   print('                                  [{}  ]'.format(colm_8))
                   info[index] = ('                                  [{}  ]'.format(colm_8))
                   index+=1
           else:   
             colm8 = mass5[0+e]  
             print('        {}    [{}]'.format(colm7.text,colm8))
             info[index] = ('        {} [{}]'.format(colm7.text, colm8))
       e+=1
       index+=1
         
    #Получение заголовка 'Документы'
    title7 = soup.find('div', id='Docs_DocsDivDiv').find('th', class_='block-head').text
    info[index] = title7
    index+=1
    print(title7)

    n5 = soup.find('div', class_='block-div', id='Docs_DocsDivDiv').find('table',id='Docs_DocsDiv').find('tbody')


    #Получение названия поля 'Документация' из раздела'Документы'
    colm9 = n5.find('td', class_='block-lable').text
    info[index] = ('        {}'.format(colm9))
    index+=1
    print('           {}'.format(colm9))

    # цекл для получения описания поля 'Документация'
    k = 0
    for item5 in mass6:
        #Cобираем ссылки для скачивания файлов со страницы лота
        colm10 = 'http://utp.sberbank-ast.ru/VIP/File/DownloadFile?fid='+ mass6[0+k]
        print('                [{}]'.format(colm10))
        info[index] = ('                [{}]'.format(colm10))
        index+=1
        k+=1

    #Заголовки 'Дата поступления запросов','Тема запроса','Текст запроса','Дата разъяснения','Разъяснение'
    title8 = soup.find('thead',id='tblExplanationRequestshead').text
    info[index] = title8
    index+=1
    print(title8)

    #Заголовки 'Посмотреть', 'Наименование протокола', 'Дата подписания протокола на площадке', 'Статус протокола'
    title9 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolView').text
    title10 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolName').text
    title11 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolDate').text
    title12 = soup.find('thead', id='tblProtocolInfohead').find('th', id='Protocols_thProtocolStatus').text
    info[index] = ('                 {}                                {}        {} {} '.format(title9, title10, title11, title12))
    index+=1
    print('{} {} {} {} '.format(title9, title10, title11, title12))

    e12 = soup1.find('protocolinfo')
    if e12 is None:
        print('                                      {}'.format('"Информация отсутствует"'))
        e12 = 'Информация отсутствует'
        info[index] = ('                                      {}                                     '.format(e12))
        index+=1
    else:
        #Собираем ссылку(ссылки) для просмотра протокола
        href = soup1.find('protocol').find('protocoldocid').text
        link = 'http://utp.sberbank-ast.ru/VIP/Util/DocumentView/'+ href
        #Получаем значения других разделов:'Наименование протокола', 'Дата подписания протокола на площадке', 'Статус протокола'
        e_12 = soup1.find('protocolinfo').find('protocolname').text
        e_13 = soup1.find('protocolinfo').find('protocoldate').text
        e_14 = soup1.find('protocolinfo').find('protocolstatus').text
        print('[{}]  [{}]   [{}]   [{}]'.format(link,e_12,e_13,e_14))
        info[index] = ('[{}]   [{}]               [{}]              [{}]'.format(link,e_12,e_13,e_14))
        index+=1

    #Заголовки 'Дата события' , 'Событие'
    title13 = soup.find('tr',id='hTableEvents_Eventsrow').find('th',id='Events_thEventDate').text
    title14 = soup.find('tr',id='hTableEvents_Eventsrow').find('th',id='Events_thEventComment').text
    info[index] = ('{}          {} '.format(title13, title14))
    index+=1
    print('{}          {} '.format(title13, title14))

    #Цикл для получения значений полей разделов 'Дата события и 'Событие'
    for item6 in soup1.find('events'):
        colm11 = item6.find('eventdate').text
        colm12 = item6.find('eventcomment').text
        info[index] = ('[{}]     [{}]'.format(colm11,colm12))
        index+=1
        print('[{}]     [{}]'.format(colm11,colm12))

    #Запись полученных данных из всех разделов лота в файл формата 'json'
    infoArr.append(info)
    f = open('info.json', 'w',encoding='UTF-8')
    f.write(json.dumps(infoArr, sort_keys=False, indent=4,ensure_ascii = False))

def main():
    parse(get_html('http://utp.sberbank-ast.ru/VIP/NBT/PurchaseView/43/0/0/239861'))

if __name__ == '__main__':
     main()


