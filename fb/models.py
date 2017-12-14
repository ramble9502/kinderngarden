# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.


class Schoolclass(models.Model):
    user = models.ForeignKey(User, related_name="schoolclass")
    schoolclass = models.CharField("班級名稱", max_length=200)
    year = models.CharField("年度與班級編號", max_length=100)

    def __unicode__(self):
        return self.schoolclass


class Studentinformation(models.Model):
    contact = models.ForeignKey(Schoolclass, related_name="studentInfor")
    email = models.EmailField("家長連絡登入帳戶")
    name = models.CharField("家長姓名", max_length=255)
    childName = models.CharField("小朋友姓名", max_length=255)
    phone = models.CharField("家長聯絡電話(手機)", max_length=10, validators=[
                             MinLengthValidator(9)])
    useraddress = models.CharField("家庭住址", max_length=255, blank=True)
    usercontact = models.CharField("家長與孩童關係", max_length=255, blank=True)

    def __unicode__(self):
        return self.childName


class Ebook(models.Model):
    user = models.ForeignKey(User, related_name="ebook")
    title = models.CharField("標題", max_length=255)
    image = models.ImageField("電子書封面", upload_to='ebookcovers/')

    def __unicode__(self):
        return self.title


class Ebook_detail(models.Model):
    contact = models.ForeignKey(Ebook, related_name="ebookdetail")
    image = models.ImageField('電子書圖片', upload_to='profiles/', blank=True)
    sortbynumber = models.AutoField(primary_key=True)

    def __unicode__(self):
        return self.contact


class Contactbook2(models.Model):
    contact = models.ForeignKey(Schoolclass, related_name="contactbook2")
    title = models.CharField("聯絡簿標題", max_length=255)
    content = models.CharField("細項內容", max_length=255)
    honor = models.CharField("表彰名單", max_length=255)
    datetime = models.DateTimeField(auto_now=True)
    imagecontact = models.ImageField(upload_to="contactbook/", blank=True)

    def __unicode__(self):
        return self.title


class Contacturl(models.Model):
    contact = models.ForeignKey(Contactbook2, related_name="contacturl")
    url = models.CharField("傳送url", max_length=255, blank=True)

    def __unicode__(self):
        return self.url


class Dailyrecord(models.Model):
    contact = models.ForeignKey(User, related_name="dailyrecord")
    datetime = models.DateField("日期", auto_now=True)
    topic = models.CharField("教學單元", max_length=255)
    studentnum = models.CharField("學生人數", max_length=255)
    attend = models.CharField("出席人數", max_length=255)
    absence = models.CharField("缺席人數", max_length=255)
    title = models.CharField("教學日誌標題", max_length=255)
    event = models.CharField("偶發事件處理事項", max_length=2550)
    content = models.TextField("教學內容", max_length=2550)
    introspective = models.TextField("教學省思", max_length=2550)
    image = models.ImageField("教學日誌圖片", upload_to="dailyrecord/", blank=True)

    def __unicode__(self):
        return self.topic


class Announcement(models.Model):
    user = models.ForeignKey(User, related_name="announce")
    datetime = models.CharField("公告時間",max_length=255)
    title = models.CharField("公告標題", max_length=255)
    content = models.CharField("公告內容", max_length=2550)
    file = models.FileField("上傳檔案", upload_to="announce/", blank=True)

    def __unicode__(self):
        return self.title
