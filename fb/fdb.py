# -*- coding: utf-8 -*-
from firebase import firebase

fb = firebase.FirebaseApplication(
    'https://androidpackages-e5a5c.firebaseio.com/', None)


def fuploadclass(year, schoolclass, contact):
    data = {}
    data['schoolclass'] = schoolclass
    data['contact'] = contact
    g = fb.get('class_information', year)
    if g == None:
        c1 = fb.put('class_information', name=year, data=data)
        text0 = "資料新增成功！"
        return text0
    elif g['schoolclass'] == schoolclass and g['contact'] == contact:
        text1 = "資料年度或編號可能錯誤！"
        return text1
    else:
        c2 = fb.put('class_information', name=year, data=data)
        text2 = "班級資料已更新！"
        return text2


def fdeleteclass(year, schoolclass):

    d = fb.get('class_information', year)

    if d == None:
        text2 = '此班級不存在無法刪除!!'
        return text2

    elif d['schoolclass'] == schoolclass:
        d1 = fb.delete('class_information', year)
        text3 = '此班級資料已完全刪除'
        return text3

    else:
        text4 = '無法刪除你所選的班級資料'
        return text4


def fuploadclastu(classroom, email, name):
    data = {}
    data['Email'] = email
    data['Classroom'] = classroom
    data['Name'] = name

    emailtobranch = email.replace("@", "").replace(".", "")

    fb.get('users/', emailtobranch)
    fb.put('users/', name=emailtobranch, data=data)


def fdeleteclastu(classroom, name, email):
    emailtobranch = email.replace("@", "").replace(".", "")
    d = fb.get('class_information/' + classroom +
               '/stu_profile', emailtobranch)
    c = fb.get('users/', emailtobranch)
    if d == None:
        text2 = "無法找到這位使用者!"
    elif d['userdetailemail'] == email:
        d1 = fb.delete('class_information/' + classroom +
                       '/stu_profile', emailtobranch)
        c1 = fb.delete('users/', emailtobranch)
        text3 = "此學生已被刪除"
        return text3
    else:
        text4 = "請確認學生帳號密碼均無誤"
        return text4


def fdeletebook(name):
    d = fb.get('ebook_detail/', name)
    if d == None:
        text2 = "無法找到該電子書"
        return text2
    else:
        d1 = fb.delete('ebook_detail/', name)
        text3 = "此電子書已被刪除"
        return text3


def fdeleteannounce(title):
    d = fb.get('announce/', title)
    if d == None:
        text2 = "無法找到該電子書"
        return text2
    else:
        d1 = fb.delete('ebook_detail/', title)
        text3 = "此電子書已被刪除"
        return text3
