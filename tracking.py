from bs4 import BeautifulSoup
import requests
import mysql.connector
#connecting to the database
db=mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='Price_Tracker'
)
cursor=db.cursor()
#deleting the old data to insert the new one
cursor.execute("delete from products")
db.commit()

#getting the percentage desired
while True:
    percentage=input("What reduction percentage you want to start looking from : ")
    if percentage.isnumeric() and 0<=int(percentage)<=100:
        percentage=int(percentage)
        break
print('='*80)
print('')
#cleaning the price format
def clean(price):
    price=price.replace(",",'.')
    p=price.find('.')
    new_price=price[:p+1]
    for i in price[p:]:
        if i!=".":
            new_price+=i
    return new_price

#inserting the results found into the database
def inserting():
    count = 0
    page_number=0
    while True:#to check multiple pages
        page_number += 1
        url=f"https://www.jumia.com.tn/pc-portables/?page={page_number}"
        code=requests.get(url).content
        results=BeautifulSoup(code,'lxml')
        results = results.find_all("article", {'class': 'prd _fb col c-prd'})
        if results!=[]:
            for result in results:
                reduction=result.find("div",{'class','bdg _dsct _sm'})
                if reduction!=[] and reduction != None:
                    reduction=int(reduction.text[:-1])
                    if reduction>=percentage:
                        count += 1
                        prod_name=result.h3.text
                        prod_price=result.find('div',{"class":'prc'}).text.replace(' TND','')
                        prod_link='jumia.com.tn'+result.a['href']
                        cursor.execute("insert into products(id,name,price,reduction_percentage,link) values(%s,%s,%s,%s,%s)",(count,prod_name,float(clean(prod_price)),float(reduction),prod_link))
                        db.commit()
        else:
            break
    print(f"We have found {count} products that matches your needs")
if __name__=='__main__':
    inserting()


