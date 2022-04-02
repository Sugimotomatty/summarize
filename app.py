from flask import Flask, render_template, request
from wtforms import Form, FloatField, SubmitField, validators, ValidationError,StringField,TextAreaField, FileField
import numpy as np

import summarize 

app = Flask(__name__)

class CheckForm(object):
    def __call__(self, form, field):
        n_str = len(form['EnterSentence'].data)
        extension = request.files['upload_file'].filename.split('.')[-1]
        if n_str == 0:
            if extension == '':
                raise ValidationError('文の入力かtxtファイルのアップロードは必須です')
            elif extension != 'txt':
                raise ValidationError('.txtファイルをアップロードしてください')
        else:
            if extension != '':
                raise ValidationError('文かtxtファイルいずれか一つを入力してください')

# Flaskとwtformsを使い、index.html側で表示させるフォームを構築する
class EnterForm(Form):
    EnterSentence = TextAreaField('要約したい文を入力, もしくは.txtファイルをアップロードしてください', [CheckForm()])
    upload_file = FileField()

    # html側で表示するsubmitボタンの表示
    submit = SubmitField("要約")

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    form = EnterForm(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:            
            if len(form['EnterSentence'].data) > 0:
                sentence = form.EnterSentence.data
            else:
                sentence = request.files['upload_file'].read().decode('utf-8')

            result = summarize.summa(sentence) #ここでsummarizeファイルにおけるsumma関数を呼び出し

            result1 =""
            for fragment in result:
                result1+=fragment

            return render_template('result.html', result = result1) #resultはresult.html内でのresultに対応
                                                                    #result1はこのすぐ上のresultに対応       

    
    elif request.method == 'GET':

        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
