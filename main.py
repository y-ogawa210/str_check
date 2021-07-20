import PySimpleGUI as sg


#レイアウトを作成
layout = [

         [ sg.Text("本文を入力してください")],
         #sizeに第一引数は横幅,第二引数は縦幅
         [ sg.Multiline(size=(80,5),key='long_txt')],
         [ sg.Text("---------------------")],
         [ sg.Text("抽出したいキーワードの数を指定してください")],
         [ sg.Radio("1",key='radio1',group_id="radio",default=True),
             sg.Radio("2",key='radio2',group_id="radio"),
             sg.Radio("3",key='radio3',group_id="radio"),
             sg.Radio("4",key='radio4',group_id="radio"),
             sg.Radio("5",key='radio5',group_id="radio")],
         [ sg.Text("---------------------")],
         [ sg.Text("抽出したいキーワードを入力してください（左から入力してください）")],
         [ sg.InputText(size=(15,1),key='txt1'),sg.InputText(size=(15,1),key='txt2'),sg.InputText(size=(15,1),key='txt3'),sg.InputText(size=(15,1),key='txt4'),sg.InputText(size=(15,1),key='txt5')],
         [ sg.Button("抽出する", font=(50),key='btn'),sg.Button("全部消す", font=(50),key='del_btn')],
         [ sg.Text("---------------------これより下は抽出結果となります---------------------")],
         [ sg.Text("取得した文章の文字数を表示します")],
         [ sg.InputText(size=(15,1),key='all_txt')],
         [ sg.Text("---------------------")],
         [ sg.Text("キーワードの出現回数を表示します")],
         [ sg.InputText(size=(15,1),key='cp_txt1'),sg.InputText(size=(15,1),key='cp_txt2'),sg.InputText(size=(15,1),key='cp_txt3'),sg.InputText(size=(15,1),key='cp_txt4'),sg.InputText(size=(15,1),key='cp_txt5')],
         [ sg.InputText(size=(15,1),key='num1'),sg.InputText(size=(15,1),key='num2'),sg.InputText(size=(15,1),key='num3'),sg.InputText(size=(15,1),key='num4'),sg.InputText(size=(15,1),key='num5')],

    ]

#ウィンドウを作成して中にレイアウトを記載
Window = sg.Window("本文チェックツール", layout)

#ウィンドウ可視化
while True:
    event, value = Window.read()
    #Noneは×ボタン
    if event == None:
        break
   
    if event == 'btn':
        #本文（long_txt）の長さを取得してallに格納
        all = len(value['long_txt'])

    #
    #ここから抽出したいキーワードを
    #
    if event == 'btn':
        all_abcde = value['long_txt']
        count_a = value['txt1']
        result_a = (all_abcde.count(count_a))

    if event == 'btn':
        all_abcde = value['long_txt']
        count_b = value['txt2']
        result_b = (all_abcde.count(count_b))

    if event == 'btn':
        all_abcde = value['long_txt']
        count_c = value['txt3']
        result_c = (all_abcde.count(count_c))

    if event == 'btn':
        all_abcde = value['long_txt']
        count_d = value['txt4']
        result_d = (all_abcde.count(count_d))

    if event == 'btn':
        all_abcde = value['long_txt']
        count_e = value['txt5']
        result_e = (all_abcde.count(count_e))

    #
    #空のテキストに出力していく
    #

    Window['all_txt'].Update(all)

    Window['cp_txt1'].Update(count_a)
    Window['cp_txt2'].Update(count_b)
    Window['cp_txt3'].Update(count_c)
    Window['cp_txt4'].Update(count_d)
    Window['cp_txt5'].Update(count_e)

    if value["radio1"] == True:
        Window['num1'].Update(result_a)

    if value["radio2"] == True:
        Window['num1'].Update(result_a)
        Window['num2'].Update(result_b)
    
    if value["radio3"] == True:
        Window['num1'].Update(result_a)
        Window['num2'].Update(result_b)
        Window['num3'].Update(result_c)

    if value["radio4"] == True:
        Window['num1'].Update(result_a)
        Window['num2'].Update(result_b)
        Window['num3'].Update(result_c)
        Window['num4'].Update(result_d)
 
    if value["radio5"] == True:
        Window['num1'].Update(result_a)
        Window['num2'].Update(result_b)
        Window['num3'].Update(result_c)
        Window['num4'].Update(result_d)
        Window['num5'].Update(result_e)


#入力されている文字を全部消す
    if event == 'del_btn':

        Window['long_txt'].Update("")

        Window['txt1'].Update("")
        Window['txt2'].Update("")
        Window['txt3'].Update("")
        Window['txt4'].Update("")
        Window['txt5'].Update("")

        Window['all_txt'].Update("")

        Window['cp_txt1'].Update("")
        Window['cp_txt2'].Update("")
        Window['cp_txt3'].Update("")
        Window['cp_txt4'].Update("")
        Window['cp_txt5'].Update("")

        Window['num1'].Update("")
        Window['num2'].Update("")
        Window['num3'].Update("")
        Window['num4'].Update("")
        Window['num5'].Update("")



