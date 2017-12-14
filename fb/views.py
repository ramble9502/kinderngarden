# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .fdb import fuploadclass, fdeleteclass, fuploadclastu, fdeleteclastu, fdeletebook, fdeleteannounce
from one.models import jktree, mmready, Mombaby
import datetime


@login_required
def index(request):
    if request.user.is_superuser:
        schoolclass = Schoolclass.objects.all().order_by('-id')
    else:
        schoolclass = Schoolclass.objects.filter(
            user=request.user).order_by('-id')
    user = get_object_or_404(User, username=request.user)
    extra_context = {'user': user, 'schoolclass': schoolclass}
    return render_to_response('schoolclass_index.html', extra_context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("That's not is_active.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')


@csrf_exempt
def addschoolclass(request):
    if request.method == 'POST':
        year = request.POST['year']
        schoolclass = request.POST['schoolclass']
        user = User.objects.get(email=request.POST['user'])
        contactfirebase = request.POST['user']
        fuploadclass(year, schoolclass, contactfirebase)
        Schoolclass.objects.create(year=year, schoolclass=schoolclass,
                                   user=user)
        return render(request, 'schoolclass_index.html', locals())


@csrf_exempt
def deleteschoolclass(request, id):
    obj = Schoolclass.objects.get(pk=id)
    year = obj.year
    schoolclass = obj.schoolclass
    fdeleteclass(year, schoolclass)
    obj.delete()
    return HttpResponseRedirect('/')


@login_required
def classparent(request, id):
    schoolclass = get_object_or_404(Schoolclass, id=id)
    user = get_object_or_404(User, username=request.user)
    extra_context = {'schoolclass': schoolclass, 'user': user}
    return render(request, 'studentinfo_index.html', extra_context)


@csrf_exempt
def addclassparent(request):
    if request.method == "POST":
        contact = get_object_or_404(Schoolclass, year=request.POST['contact'])
        contact2 = request.POST['contact']
        email = request.POST['email']
        name = request.POST['name']
        childName = request.POST['childname']
        phone = request.POST['phone']
        useraddress = request.POST['useraddress']
        usercontact = request.POST['usercontact']
        fuploadclastu(contact2, email, name)
        Studentinformation.objects.create(contact=contact, name=name, email=email,
                                          useraddress=useraddress, usercontact=usercontact, childName=childName, phone=phone)
        return render(request, 'schoolclass_index.html', locals())


@csrf_exempt
def deleteclasstu(request, id, vpk):
    obj = Studentinformation.objects.get(pk=id)
    name = obj.name
    classroom = obj.contact.year
    email = obj.email
    fdeleteclastu(classroom, name, email)
    obj.delete()
    return HttpResponseRedirect('/classparent/' + vpk)


@login_required
def ebook(request):
    if request.user.is_superuser:
        ebook = Ebook.objects.all().order_by('-id')
    else:
        ebook = Ebook.objects.filter(user=request.user)
    user = get_object_or_404(User, username=request.user)
    extra_context = {'user': user, 'ebook': ebook}
    return render(request, 'ebook_index.html', extra_context)


@csrf_exempt
def addebook(request):
    user = get_object_or_404(User, username=request.user)
    form = EbookCoverForm()
    if request.user.is_superuser:
        ebook = Ebook.objects.all().order_by('-id')
    else:
        ebook = Ebook.objects.filter(user=request.user).order_by('-id')
    extra_context = {'user': user, 'ebook': ebook, 'form': form}
    if request.method == 'POST':
        form = EbookCoverForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.image = request.FILES['image']
            post.title = request.POST['title']
            form.save()
            return HttpResponseRedirect('/ebook/')
    else:
        return render(request, 'ebook_index.html', extra_context)


@csrf_exempt
def deletebook(request, id):
    obj = Ebook.objects.get(pk=id)
    name = obj.title
    contact = obj.user
    fdeletebook(name)
    obj.delete()
    return HttpResponseRedirect('/ebook/')


@csrf_exempt
def addebookimage(request, id):
    ebook = get_object_or_404(Ebook, id=id)
    user = get_object_or_404(User, username=request.user)
    ebookdetail = Ebook_detail.objects.filter(
        contact=ebook).order_by('sortbynumber')

    form = EbookForm()
    extra_context = {'ebook': ebook, 'form': form,
                     'user': user, 'ebookdetail': ebookdetail}
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('image'):
                Ebook_detail.objects.create(image=f, contact=ebook)
        return render_to_response('ebookdetail_index.html', extra_context)
    else:
        return render_to_response('ebookdetail_index.html', extra_context)


@login_required
def contactindex(request):
    user = get_object_or_404(User, username=request.user)
    if request.user.is_superuser:
        schoolclass = Schoolclass.objects.all().order_by('-id')
    else:
        schoolclass = Schoolclass.objects.filter(
            user=request.user).order_by('-id')
    extra_context = {'user': user, 'schoolclass': schoolclass}
    return render_to_response('contactbook_index.html', extra_context)


@csrf_exempt
def addcontact(request, id):
    jktree1 = jktree.objects.order_by('-id')[:10]
    mmready1 = mmready.objects.order_by('-id')[:10]
    mombaby1 = Mombaby.objects.order_by('-id')[:10]
    schoolclass = get_object_or_404(Schoolclass, id=id)
    user = get_object_or_404(User, username=request.user)
    contactbook2 = Contactbook2.objects.filter(
        contact=schoolclass).order_by('-datetime')
    form = ContactbookForm()
    extra_context = {'user': user, 'schoolclass': schoolclass,
                     'contactbook': contactbook2, 'form': form, 'jktree': jktree1,
                     'mmready': mmready1, 'mombaby': mombaby1}
    if request.method == 'POST':
        form = ContactbookForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.imagecontact = request.FILES['image']
            post.datetime = datetime.datetime.now()
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.honor = request.POST['honor']
            post.contact = get_object_or_404(Schoolclass, id=id)
            form.save()
            return HttpResponseRedirect('/addcontact/' + id + '/')
    else:
        return render(request, 'contactbook_detail.html', extra_context)


def deletecontact(request, id, vpk):
    obj = Contactbook2.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/addcontact/' + vpk)


@csrf_exempt
def adddailyrecord(request):
    user = get_object_or_404(User, username=request.user)

    if request.user.is_superuser:
        record = Dailyrecord.objects.all()
    else:
        record = Dailyrecord.objects.filter(contact=user).order_by('-datetime')
    form = DailyrecordForm()
    extra_context = {'user': user, 'record': record, 'form': form}
    if request.method == 'POST':
        form = DailyrecordForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.datetime = datetime.datetime.today()
            post.contact = get_object_or_404(User, username=request.user)
            post.title = request.POST['title']
            post.studentnum = request.POST['studentnum']
            post.attend = request.POST['attend']
            post.absence = request.POST['absence']
            post.topic = request.POST['topic']
            post.content = request.POST['content']
            post.introspective = request.POST['introspective']
            post.event = request.POST['event']
            form.save()
            return HttpResponseRedirect('/adddailyrecord/')
    else:
        return render(request, 'dailyrecord_index.html', extra_context)


def deletedailyrecord(request, id):
    obj = Dailyrecord.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/adddailyrecord/')


@csrf_exempt
def addannounce(request):
    user = get_object_or_404(User, username=request.user)
    announce = Announcement.objects.all()
    form = AnnounceForm()
    extra_context = {'user': user, 'announce': announce, 'form': form}
    if request.method == 'POST':
        form = AnnounceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.datetime = request.POST['datetime']
            post.file = request.FILES['file']
            post.user = get_object_or_404(User, username=request.user)
            post.title = request.POST['title']
            post.content = request.POST['content']
            form.save()
            return HttpResponseRedirect('/addannounce/')
    else:
        return render(request, 'announcement_index.html', extra_context)


def deleteannounce(request, id):
    obj = Announcement.objects.get(pk=id)
    title = obj.title
    fdeleteannounce(title)
    obj.delete()
    return HttpResponseRedirect('/addannounce/')
