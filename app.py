#author -- Harsh Kumar 
#date 09/apr/2023ls
#importing libraries
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

app = Flask(__name__)

#route to homepage
@app.route('/', methods=['GET'])
@app.route('/home',methods=['GET'])
#function for homepage
def homepage():
    return render_template('home.html')

#route to result page
@app.route('/result', methods=['GET','POST'])
#function for result page
def result():
    if request.method == 'POST':
        try:
            # take the entered search string from the form 
            SearchString = request.form['search'].replace(' ','')
            flipkart_url = "https://www.flipkart.com/search?q=" + SearchString
            uClient = uReq(flipkart_url)
            flipkart_page = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkart_page,'html.parser')
            big_box = flipkart_html.find_all('div' , {'class':'_13oc-S'})
            #getting link for each specific big box
            filename = SearchString+".csv"
            reviews= []
            for i in big_box:
                #getting the link for each product
                prod_link= "https://www.flipkart.com"+i.div.div.a['href']
                prod_req = requests.get(prod_link)
                #beautify the code we got from prod link
                prod_html = bs(prod_req.text,'html.parser')
                #source code for getting review section 
                rev_box = prod_html.find('div',{"class":"_16PBlm"}) 
                try:
                    name = (rev_box.div.div.find('p',{"class":"_2sc7ZR _2V5EHH"})).text
                except :
                    logging.info("name") 
                
                try:
                    rating =   rev_box.div.div.div.div.text
                except:
                    rating="no rating"
                    logging.info("rating")
                
                try:
                    comment_header = rev_box.div.div.p.text
                except:
                    comment_header = "NO comment header"
                    logging.info("Comment header")

                
                try:
                    comment =  (rev_box.div.div.find('div',{'class':''})).text
                except Exception as e:
                    comment = "No Comment"
                    logging.info(e)  
                prod_rev_details={"Product": SearchString , "Name": name , "Rating": rating, "CommentHeader": comment_header, "Comment": comment}
                reviews.append(prod_rev_details)
            
            msg ="Successfully Scrapped data"
            logging.info("Final Result{}".format(reviews))
            return render_template('result.html',reviews= reviews[0:(len(reviews)-1)], msg=msg)
        except Exception as e:
            logging.info(e)
            return 'Kush to Gadbad hai Daya !!!!'            
                
        
    else:
        msg = 'No string searched yet'
        return render_template('result.html',msg = msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)