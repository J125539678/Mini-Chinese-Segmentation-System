import string
punctuation=[",","，","。","”","“","《","》","：","！","？","；","；","、","；","（","）","…"," ","\n","\t","——"]
punctuation.extend(string.punctuation)

def enter_file():#生成一个大的字典
    twoWord=open("字典\\hanyupinyin3_modified.txt","r")
    content1=twoWord.read()
    twoWord.close()
    content12=content1.split()
    prononciation={}
    for (i,ele) in enumerate(content12):
        if i%2==1:
            list_afdoaodf=list(ele)
            for element in list_afdoaodf:
                prononciation[element]=content12[i-1]
    dictionary={}
    list_hjahahaha=list(string.ascii_lowercase)
    list_hjahahaha.remove("i")
    list_hjahahaha.remove("u")
    list_hjahahaha.remove("v")
    for letter in list_hjahahaha:
        twoWord=open("字典\\"+letter+".txt","r")
        content1=twoWord.read()
        twoWord.close()
        content12=content1.split()
        dictionary1={}
        for i,ele in enumerate(content12):
            if i%2==0:
                dictionary1[ele]=int(content12[i+1])
        dictionary[letter]=dictionary1
    return prononciation,dictionary


def transform(string2):  #将整篇文章以标点为界，分成小段存入List中，并按顺序保留标点
    global punctuation
    string1=[]
    string1.append(string2)
    for i in punctuation:
        for ele in string1:
            if i in ele and ele not in punctuation:
                old=ele+""
                ele=ele.split(str(i))
                middle="+"+str(i)+"+"
                ele=middle.join(ele)
                ele=ele.split("+")
                index=string1.index(old)
                string1.remove(old)
                ele.reverse()
                for haha in ele:
                    string1.insert(index,haha)
    for i in string1:
        if i=="":
            string1.remove(i)
    return string1

def match(a_string_of_word,prononciation,dictionary):#这个词是否在词库中
    try:
        first=a_string_of_word[0]
        letter=prononciation[first]
        letter=letter[0]
        vocabulary=dictionary[letter]
        if a_string_of_word in vocabulary:
            return True
        else:
            return False
    except:
        return False


def slice(string_haha,prononciation,dictionary):#根据字典分词
    string_test=string_haha[:]
    new=[]
    number=['1','2','3','4','5','6','7','8','9',"0"]
    while len(string_haha)>0:
        if string_haha[0] in string.ascii_letters or string_haha[0] in number:
            a=""
            while string_haha[0] in string.ascii_letters or  string_haha[0] in number:
                a+=string_haha[0]
                if len(string_haha)==1:
                    string_haha=""
                    break
                else:
                    string_haha=string_haha[1:]
            new.append(a)
        order=list(range(min(8,len(string_haha)+1)))
        order.remove(0)
        order.reverse()
        for i in order:
            if string_haha=="":
                break
            test_part=string_haha[0:i]
            if match(test_part,prononciation,dictionary):
                new.append(test_part)
                string_haha=string_haha[i:]
                break
            elif i==1:
                string_haha=string_haha[1:]
                new.append(test_part)
                break
    new1=[]
    string_test=string_test[:]
    while len(string_test)>0:
        if string_test[-1] in string.ascii_letters or string_test[-1] in number:
            a=""
            while string_test[-1] in string.ascii_letters or  string_test[-1] in number:
                a+=string_test[-1]
                if len(string_test)==1:
                    string_test=""
                    break
                else:
                    string_test=string_test[:len(string_test)-1]
            new1.append(a)
        order=list(range(min(8,len(string_test)+1)))
        order.remove(0)
        order.reverse()
        for i in order:
            if string_test=="":
                break
            test_part=string_test[len(string_test)-i:len(string_test)]
            if match(test_part,prononciation,dictionary):
                new1.append(test_part)
                string_test=string_test[:len(string_test)-i]
                break
            elif i==1:
                string_test=string_test[:len(string_test)-1]
                new1.append(test_part)
                break
    new1.reverse()
    total1=0
    for i in new:
        try:
            first=i[0]
            letter=prononciation[first]
            letter=letter[0]
            vocabulary=dictionary[letter]
            total1+=vocabulary.get(i,0)
        except:
            continue
    total2=0
    for i in new1:
        try:
            first=i[0]
            letter=prononciation[first]
            letter=letter[0]
            vocabulary=dictionary[letter]
            total2+=vocabulary.get(i,0)
        except:
            continue
    if total1<total2:
        new=new1
    new=check1(new)
    new=check3(new)
    return new

def check1(list1):
    words=["了","着","儿","个","头","到","年","月","天","于"]
    new=[]
    for ele in list1:
        if ele in words:
            try:
                temporary=new[-1]
                word=temporary+ele
                new=new[:len(new)-1]
                new.append(word)
            except:
                new.append(ele)
        else:
            new.append(ele)
    return new

def check_2(list1):
    for ele in list1:
        if len(ele)!=1:
            return False
    return True
def check2(list1):
    first="“"
    second="”"
    newList=[]
    for (i,ele) in enumerate(list1):
        temporary=list1[i+1:]
        if ele==first:
            two=temporary.index(second)
            tem=temporary[0:two]
            new="".join(tem)
            if len(new)<=4 and check_2(tem):
                newList.append("“")
                newList.append(new)
                list1[i:i+len(new)]=[]
            else:
                newList.append("“")
        else:
            newList.append(ele)
    return newList

def check_3(a):
    try:
        float(a)
        return True
    except:
        return False
def check3(list1):
    new1=[]
    while list1!=[]:
        if check_3(list1[0]):
            if len(list1)>1:
                temporary=list1[1]
                word=list1[0]+temporary
                new1.append(word)
                list1=list1[2:]
            else:
                new1.append(list1[0])
                list1=list1[1:]
        else:
            new1.append(list1[0])
            list1=list1[1:]
    return new1

def slice_second(list1,vocabulary,dictionary):#对生成后的list其中每一个小的成分分词
    new=[]
    for i in list1:
        if i not in punctuation:
            m=slice(i,vocabulary,dictionary)
            new.extend(m)
        elif i in punctuation:
            new.append(i)
    new=check2(new)
    return new



def add_lines(whole):
    global punctuation
    new=[]
    for i in whole:
        if i not in punctuation:
            word=i+"/"
            new.append(word)
        else:
            new.append(i)
    final1="".join(new)
    final1=final1.split("//")
    final1="/".join(final1)
    final1=final1[0:len(final1)]
    temporary=[]
    temporary+=final1
    final=[]
    for (i,ele) in enumerate(final1):
        if ele not in punctuation:
            final.append(ele)
        elif final==[]:
            final.append(ele)
        elif ele  in punctuation and ele!="/":
            if final[len(final)-1]=="/":
                final=final[:len(final)-1]
                final.append(ele)
            else:
                final.append(ele)
        elif ele=="/":
            final.append("/")
    final="".join(final)
    return final

def Accurate_Seg(sentence,dictionary,dictionary1):#一为list 二为字典。
    sentence_1=transform(sentence)
    sentence_2=slice_second(sentence_1,dictionary,dictionary1)
    sentence_3=add_lines(sentence_2)
    return sentence_3

#==============================================================================
from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter.font import*
import winsound

def Init_Windows():  # 初始化界面
    global root,pronunciation,dictionary
    pronunciation,dictionary=enter_file()
    on_bgm()
    root = Tk()
    root.title("中文分词系统 V3.0  ————by 3 Idiots")
    root.geometry("900x600+350+70")
    root.resizable(0,0)
    root.iconbitmap("素材\\3 Idiots.ico")
    Background()

def Background():  # 设置背景图片
    bggif=PhotoImage(file='素材\\main.gif')
    bg=Label(root,image=bggif)
    bg.bggif=bggif
    bg.place_configure(x=0,y=0)

def on_bgm():  # 打开背景音乐
    winsound.PlaySound('素材//bgm.wav', winsound.SND_ASYNC)

def off_bgm():  # 关闭背景音乐
    winsound.PlaySound('NULL', winsound.SND_ASYNC)

def MyMenu():  # 创建菜单及子菜单
    global emenu
    menubar = Menu(root)

    fmenu = Menu(menubar,tearoff=0,font=("微软雅黑",9),bg="white")
    fmenu.add_command(label = "打开(O)    Ctrl+O", command = MyOpen)
    fmenu.add_command(label = "另存为(S)  Ctrl+S", command = SaveAs)
    fmenu.add_command(label = "退出(X)    Alt+F4", command = Quit)

    emenu = Menu(root,tearoff=0,font=("微软雅黑",9),bg="white")
    emenu.add_command(label="剪切(T)    Ctrl+X",command=cut)
    emenu.add_command(label="复制(C)    Ctrl+C",command=copy)
    emenu.add_command(label="粘贴(P)    Ctrl+V",command=paste)
    emenu.add_separator()
    emenu.add_command(label="全选(A)    Ctrl+A",command=select_all)

    lmenu = Menu(menubar,tearoff=0,font=("微软雅黑",9),bg="white")
    lmenu.add_command(label = "修改词库(M)",command = lexicon_window)

    hmenu = Menu(menubar,tearoff=0,font=("微软雅黑",9),bg="white")
    hmenu.add_command(label = "系统说明(I)", command = introduction)
    hmenu.add_command(label = "版本信息(V)", command = version_info)

    menubar.add_cascade(label = "文件(F)", menu = fmenu)
    menubar.add_cascade(label = "编辑(E)", menu = emenu)
    menubar.add_cascade(label = "词库(L)", menu = lmenu)
    menubar.add_cascade(label = "帮助(H)", menu = hmenu)

    root["menu"] = menubar

def MyEntry():  # 创建输入输出文本框
    OriginText()
    ResultText()

def OriginText():  # 创建输入文本框
    global Origin_Text
    frame_1 = Frame(root)
    label_1 = Label(root, text="分词原文",font=("华文行楷",15),fg="#2961ce")
    label_1.pack()
    Origin_Text = Text(frame_1, width=95,height=13,font=("楷体",12),bg="white")
    Origin_Text.pack(side=LEFT)

    sroll_1 = Scrollbar(frame_1)
    Origin_Text['yscrollcommand']=sroll_1.set
    sroll_1['command'] = Origin_Text.yview
    sroll_1.pack(side=RIGHT,fill=Y)
    Origin_Text.bind("<Button-3>",EditMenu)
    frame_1.pack(side=TOP,ipady=5)
    Origin_Text.focus()

def ResultText():  # 创建输出文本框
    global Result_Text
    frame_2 = Frame(root)
    label_2 = Label(root, text="分词结果",font=("华文行楷",15),fg="#2961ce")
    label_2.pack()
    Result_Text = Text(frame_2, width=95,height=13,font=("楷体",12),bg="white")
    Result_Text.pack(side=LEFT)

    sroll_2 = Scrollbar(frame_2)
    Result_Text['yscrollcommand']=sroll_2.set
    sroll_2['command'] = Result_Text.yview
    sroll_2.pack(side=RIGHT,fill=Y)
    Result_Text.bind("<Button-3>",EditMenu)
    frame_2.pack(side=TOP,ipady=5)

def Buttons():  # 创建主界面按钮
    botton_1 = Button(root,text="开始分词",font=("微软雅黑",11),bg="white",command=Operation)
    botton_1.pack(side=RIGHT,padx=75)
    botton_2 = Button(root,text="清空输出",font=("微软雅黑",11),bg="white",command=ClearOutput)
    botton_2.pack(side=RIGHT,padx=0)
    botton_3 = Button(root,text="清空输入",font=("微软雅黑",11),bg="white",command=ClearInput)
    botton_3.pack(side=RIGHT,padx=25)
    botton_4 = Button(root,text="复制结果",font=("微软雅黑",11),bg="white",command=CopyOutput)
    botton_4.pack(side=RIGHT,padx=0)
    botton_5 = Button(root,text="复制原文",font=("微软雅黑",11),bg="white",command=CopyInput)
    botton_5.pack(side=RIGHT,padx=25)

def Operation():  # 分词操作
    global result
    sentence = Origin_Text.get(1.0,END)
    result = Accurate_Seg(sentence,pronunciation,dictionary)
    Result_Text.insert(1.0,result)

def ClearInput():  # 清空输入框
    if askquestion(title='提示',message='确定要清空输入框吗？') == 'yes':
        Origin_Text.delete(1.0,END)

def ClearOutput():  # 清空输出框
    if askquestion(title='提示',message='确定要清空输出框吗？') == 'yes':
        Result_Text.delete(1.0,END)

def CopyInput():  # 复制原文
    text = Origin_Text.get(1.0,END)
    copy_to_clipboard(text)

def CopyOutput():  # 复制结果
    text = Result_Text.get(1.0,END)
    copy_to_clipboard(text)

def Quit():  # 退出程序
    if askquestion(title='提示',message='确定要退出程序吗？') == 'yes':
        root.destroy()

def MyOpen():  # 打开一个文本文件
    try:
        file_name = askopenfilename(filetypes=[("文本文档","*.txt")])
        text = open(file_name,"r")
        Origin_Text.insert(1.0,text.read())
    except:
        pass

def SaveAs():  # 保存分词结果到指定目录下
    try:
        file_name = asksaveasfilename(initialfile="未命名.txt",filetypes=[("文本文档","*.txt")])
        text = open(file_name,"w")
        text.write(result)
        text.close()
    except:
        pass

def EditMenu(event):  # 右键弹出编辑菜单
    global emenu
    emenu.post(event.x_root,event.y_root)

def copy_to_clipboard(text): # 复制文本到粘贴板
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.destroy()

def cut():
    if (root.focus_get() == Origin_Text):
        Origin_Text.event_generate("<<Cut>>")
    elif (root.focus_get() == Result_Text):
        Result_Text.event_generate("<<Cut>>")

def copy():
    if (root.focus_get() == Origin_Text):
        Origin_Text.event_generate("<<Copy>>")
    elif (root.focus_get() == Result_Text):
        Result_Text.event_generate("<<Copy>>")

def paste():
    if (root.focus_get() == Origin_Text):
        Origin_Text.event_generate("<<Paste>>")
    elif (root.focus_get() == Result_Text):
        Result_Text.event_generate("<<Paste>>")

def select_all():
    if (root.focus_get() == Origin_Text):
        Origin_Text.tag_add('sel','1.0','end')
    elif (root.focus_get() == Result_Text):
        Result_Text.tag_add('sel','1.0','end')

def lexicon_window():  # 创建词库修改窗口
    global lexicon,entry_1,entry_2,entry_3

    # 词库修改窗口初始化
    lexicon = Toplevel(root)
    lexicon.title("词库操作")
    lexicon.geometry("700x250+450+200")
    lexicon.resizable(0,0)
    lexicon.iconbitmap("素材\\3 Idiots.ico")
    bggif=PhotoImage(file='素材\\lexicon.gif')
    bg=Label(lexicon,image=bggif)
    bg.bggif=bggif
    bg.place_configure(x=0,y=0)

    # 词库修改菜单
    lexicon_menu = Menu(lexicon)
    save_menu = Menu(lexicon_menu,tearoff=0,font=("微软雅黑",9),bg="white")
    save_menu.add_command(label="保存词库(S)",command=permanently_saving)
    help_menu = Menu(lexicon_menu,tearoff=0,font=("微软雅黑",9),bg="white")
    help_menu.add_command(label="修改说明(I)",command=lexicon_help)
    lexicon_menu.add_cascade(label="保存(S)",menu=save_menu)
    lexicon_menu.add_cascade(label="帮助(H)",menu=help_menu)
    lexicon["menu"] = lexicon_menu

    # 词库修改界面部件
    label_1 = Label(lexicon, text="添加的词语:",font=("华文行楷",14),fg="#2961ce")
    label_1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    label_2 =Label(lexicon, text="添加词的词频(1~10^10):",font=("华文行楷",14),fg="#2961ce")
    label_2.grid(row=0,column=1,padx=50,pady=10,sticky=W)

    entry_1 = Entry(lexicon,width=20,font=("楷体",14),bg="white")
    entry_1.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    entry_2 = Entry(lexicon,width=20,font=("楷体",14),bg="white")
    entry_2.grid(row=1,column=1,padx=50,pady=10,sticky=W)

    button_1 = Button(lexicon,text="添加词语",font=("微软雅黑",11),bg="white",command=add_words)
    button_1.grid(row=1,column=2,padx=20,sticky=E)

    label_3 = Label(lexicon, text="删除的词语:",font=("华文行楷",14),fg="#2961ce")
    label_3.grid(row=2,column=0,padx=10,pady=20,sticky=W)

    entry_3 = Entry(lexicon,width=46,font=("楷体",14))
    entry_3.grid(row=3,column=0,columnspan=2,padx=10,sticky=W)

    button_2 = Button(lexicon,text="删除词语",font=("微软雅黑",11),bg="white",command=del_words)
    button_2.grid(row=3,column=2,padx=20,sticky=E)

    entry_1.focus()

def add_words():  # 添加词语到词库中
    global dictionary
    addword = str(entry_1.get())
    try:
        init=pronunciation[addword[0]]
        init=init[0]
        whether_in_lex = addword in dictionary[init]
        if whether_in_lex==True:
            if askquestion(title='提示',message="词库中已有该词语！是否替换其词频") == 'yes':
                try:
                    frequency=int(entry_2.get())
                    dictionary[init][addword]=frequency
                    showinfo(title="提示",message="替换词频成功！")
                    entry_1.focus()
                except(ValueError):
                    showerror(title='错误',message='请输入1~10^10的整数以确定词频！')
                    entry_2.focus()
            else:
                pass

        else:
            try:
                frequency=int(entry_2.get())
                dictionary[init][addword]=frequency
                showinfo(title="提示",message="添加成功！")
                entry_1.focus()
            except(ValueError):
                showerror(title='错误',message='请输入1~10^10的整数以确定词频！')
                entry_2.focus()
        dictionary = dictionary
    except:
        showerror(title='错误',message='请输入中文词语！\n（对英文本系统采用自然分词方法）')
        entry_1.focus()

def del_words():  # 从词库中删除词语
    global dictionary
    delword = str(entry_3.get())
    try:
        init=pronunciation[delword[0]]
        init=init[0]
        whether_in_lex= delword in dictionary[init]
        if whether_in_lex==False:
            showerror(text="错误",message="词库中没有该词语！")
            delete_words(dictionary,prononciation)
        else:
            del dictionary[init][delword]
            showinfo(title="提示",message="删除成功！")
        dictionary = dictionary
    except:
        showerror(title='错误',message='请输入中文词语！\n（对英文本系统采用自然分词方法）')
    entry_3.focus()

def permanently_saving():  # 永久保存已修改的题库
    if askquestion(title='提示',message="是否要永久保存当前词库？\n警告：一旦保存将覆盖掉原有词库") == 'yes':
        for key in dictionary:
            lexicon=open("字典\\"+key+".txt","w")
            for keys in dictionary[key]:
                lexicon.write(keys+"\t"+str(dictionary[key][keys])+"\t"+"\n")
            lexicon.close()
    entry_1.focus()

def lexicon_help():  # 词库修改帮助窗口
    help_window = Toplevel(lexicon)
    help_window.title=("词库帮助")
    help_window.geometry("600x320+505+200")
    help_window.resizable(0,0)
    help_window.iconbitmap("素材\\3 Idiots.ico")

    label_0 = Label(help_window,text="词库帮助",font=("楷体",15))
    label_0.pack()
    for i in [" 添加词语：","    输入要添加的词语及整数词频(词频范围1~10^10)",
              "    如果所添加的词语已在词库中，则会替换该词语的词频。","",
              " 删除词语：","    如果所输入词语在词库中，则会删除该词语","",
              " 注意：","    以上操作均为临时操作，重新启动本系统后无效，",
              "    欲永久保存，请点击左上角“文件(F)”菜单中的“保存词库(S)”。",""]:
                label_1 = Label(help_window,text=i,font=("仿宋",13))
                label_1.pack(anchor="nw",)
    label_2 = Label(help_window,text="中文分词系统v3.0  ——by 3 Idiots",font=("华文行楷",14))
    label_2.pack(anchor="ne",ipady=10,ipadx=10)
    help_window.focus()

def introduction():  # 系统说明窗口
    intro_window = Toplevel(root)
    intro_window.title=("系统说明")
    intro_window.geometry("600x480+500+120")
    intro_window.resizable(0,0)
    intro_window.iconbitmap("素材\\3 Idiots.ico")

    label_0 = Label(intro_window,text="系统说明",font=("楷体",15))
    label_0.pack()
    for i in [" 文件：","    打开：打开一个新的文本文档(*.txt)文件，将其内容导入分词原文。","    另存为：将分词结果以文本文档(*.txt)格式保存到指定目录下。","    退出：退出程序。","",
              " 编辑：","    剪切：将选中内容剪切到剪贴板上。","    复制：将选中内容复制到剪贴板上。","    粘贴：将剪贴板上的内容粘贴到指定位置。","    全选：全选输入框或输出框的文字（取决于光标悬停的位置）。","",
              " 词库：","    修改词库：可以进行词库的添加、替换和删除操作。" ,"",
              " 帮助：","    系统说明：可以查看本分词系统的操作说明。","    版本信息：可以查看历次版本的更新信息及版权说明。",""]:
        label_1 = Label(intro_window,text=i,font=("仿宋",13))
        label_1.pack(anchor="nw",)
    label_2 = Label(intro_window,text="中文分词系统v3.0  ——by 3 Idiots",font=("华文行楷",14))
    label_2.pack(anchor="ne",ipady=10,ipadx=10)
    intro_window.focus()

def version_info():  # 版本信息窗口
    ver_window = Toplevel(root)
    ver_window.title=("版本信息")
    ver_window.geometry("580x520+500+120")
    ver_window.resizable(0,0)
    ver_window.iconbitmap("素材\\3 Idiots.ico")

    label_1 = Label(ver_window,text="中文分词系统",font=("华文行楷",40),fg="#4F4F4F")
    label_1.pack(ipady=10)
    label_2 = Label(ver_window,text="Chinese Word Segmentating System",font=("微软雅黑",13))
    label_2.pack()
    xhx_1 = Label(ver_window,text='—————————————————————————————————————————————————',fg='#8E8E8E')
    xhx_1.pack()

    label_3 = Label(ver_window,text="版本声明：",font=("楷体",13))
    label_3.pack(anchor="nw",ipadx=5)
    for i in ["   中文分词系统 Version 3.5 适用于安装Python3.0及以上的Windows系统",
              "   ®Three Idiots 版权所有",
              "   Copyright © 2014-2015 Three Idiots.",
              "   All Rights Reserved."]:
                label_4 = Label(ver_window,text=i,font=("仿宋",12))
                label_4.pack(anchor="nw")
    xhx_2 = Label(ver_window,text='—————————————————————————————————————————————————',fg='#8E8E8E')
    xhx_2.pack()

    label_5 = Label(ver_window,text="版本更新历史：",font=("楷体",13))
    label_5.pack(anchor="nw",ipadx=5)
    for i in ["   —v3.0：进一步完善词库，优化搜索算法，加入多种快捷键，界面最终整合。",
              "   —v2.5：增加词库修改功能，使词库个性化，更符合用户需求。",
              "   —v2.3: 解决重大分词BUG，中文分词更稳定可靠",
              "   —v2.1：分词系统加入背景和背景音乐，极大美化分词界面。",
              "   —v2.0：按首字拼音细分词库，搜索词库更快，分词速度大幅提升。",
              "   —v1.2：完善分词界面，分词界面更友好。",
              "   —v1.0：初步实现分词操作，初步生成分词界面。",""]:
                label_6 = Label(ver_window,text=i,font=("仿宋",12))
                label_6.pack(anchor="nw",)
    label_7 = Label(ver_window,text="中文分词系统v3.0  ——by 3 Idiots",font=("华文行楷",14))
    label_7.pack(anchor="ne",ipady=10,ipadx=10)
    ver_window.focus()

def shortcut_keys():  # 快捷键
    root.bind("<Control-o>",shortcut_open)
    root.bind("<Control-O>",shortcut_open)
    root.bind("<Control-s>",shortcut_saveas)
    root.bind("<Control-S>",shortcut_saveas)
    root.bind("<Control-a>",shortcut_select_all)
    root.bind("<Control-A>",shortcut_select_all)

def shortcut_operation(event):
    Operation()

def shortcut_open(event):
    MyOpen()

def shortcut_saveas(event):
    SaveAs()

def shortcut_select_all(event):
    select_all()

def User_Interface():  # 主程序
    Init_Windows()
    MyMenu()
    MyEntry()
    Buttons()
    shortcut_keys()
    root.mainloop()
    off_bgm()

User_Interface()
