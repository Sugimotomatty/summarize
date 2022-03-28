from flask import Flask, render_template, request
from wtforms import Form, FloatField, SubmitField, validators, ValidationError,StringField,TextAreaField
import numpy as np

import summarize 

app = Flask(__name__)

# Flaskとwtformsを使い、index.html側で表示させるフォームを構築する
class EnterForm(Form):
    EnterSentence = TextAreaField('要約したい文を貼り付け、または入力してください', [validators.InputRequired("この項目は入力必須です")])


    # html側で表示するsubmitボタンの表示
    submit = SubmitField("判定")

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    form = EnterForm(request.form)
    if request.method == 'POST':
        print(form.EnterSentence.data)
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:            
            EnterSentence = form.EnterSentence.data

            result = summarize.summa(EnterSentence) #ここでsummarizeファイルにおけるsumma関数を呼び出し

            result1 =""
            for fragment in result:
                result1+=fragment

            return render_template('result.html', result = result1) #resultはresult.html内でのresultに対応
                                                                    #result1はこのすぐ上のresultに対応       

    
    elif request.method == 'GET':

        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
