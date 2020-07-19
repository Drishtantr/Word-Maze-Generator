from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import string
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    wordlen=15
    return render_template('index.html', words=wordlen)

@app.route('/', methods=['POST'])
def getvalue():
    val=request.form['word']
    val=val.upper()
    word=val.split(" ")
    # word=["apple","ball","cat","dog","egg","friend", "gas", "hall", "image", "jackle","kiss","laugh","math","nose","ostrich"]
    if len(word)==15:
        B=string.ascii_uppercase
        Arr= np.full((18,18),".")
        li=random.sample(range(4,18), 14)
        for i in range(7,15):
            a=word[i]
            ale=len(a)
            dif=18-ale
            cho=random.choice(range(dif))
            temp=li[i-7]
            # nu=random.choice([1,2])
            for j in range(ale):
                Arr[j+cho][temp]=word[i][j]   

        wordd=0
        li=random.sample(range(7),7)
        maze=18
        for i in range(18):
            sam=li[wordd]
            a=word[sam]
            ale=len(a)
            count=0
            maze-=1
            put=random.choice([maze, i])
            # if i%2==0:
            #     put=maze
            # else:
            #     put=i             
            for l in range(18):
                if Arr[put][l]==".":
                    count+=1
                else:
                    break
            if count>=ale:
                wordd+=1
                dif=count-ale
                cho=random.choice(range(dif+1))  
                for j in range(ale):
                    Arr[put][j+cho]=word[sam][j]
            if wordd==7:
                break

        # for i in range(18):
        #     for j in range(18):
        #         while(Arr[i][j]=="."):
        #             Arr[i][j]=random.choice(B)
                
        df=pd.DataFrame(Arr)
    else:
        df=pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})
    # html=df.to_html()

    # return val
    return render_template('index.html', words=len(word), tables=[df.to_html(index=False,header=None, classes='table table-bordered table-warning table-sm w-auto text-center')], titles=df.columns.values)