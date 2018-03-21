 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse,JsonResponse

def index(request):

    return render(request,'login.html')

def regist(request):

    sign_id = request.GET.get('sign_id')
    sign_pw = request.GET.get('sign_pw')
    sign_name = request.GET.get('sign_name')
    sign_birth = request.GET.get('sign_birth')

    lock = 0
    print sign_id
    print sign_pw
    print sign_name
    print sign_birth

    with connections['default'].cursor() as cur:
            query = '''
                select id from user
                where id = '{id}'
            '''.format(id=sign_id)
            cur.execute(query)
            rows = cur.fetchall()

    if len(rows) != 0:

        lock = 1
        return JsonResponse({'return':'fail'})

    with connections['default'].cursor() as cur:
            query = '''
                insert into user(id, password, name,birth)
                values('{id}',MD5('{password}'),'{name}','{birth}')
            '''.format(id=sign_id,password=sign_pw,name=sign_name,birth=sign_birth)
            cur.execute(query)

            print query

    return JsonResponse({'return':'success', 'id':sign_id, 'password':sign_pw,'name':sign_name,'birth':sign_birth})

def Home(request):

    #print request.session.get('user_id')

    if 'user_id' not in request.session:  #id 를 생성해서 들어간 페이지가 아닐경우 session 존재하지 않으니 return

        return render (request ,'error.html')  # Sesseion 없어서 return 된 경우   ->error.html

    return render (request ,'Home.html')

def log_out(request):

    del request.session['user_id']

    return JsonResponse({'return':'success'})

def log_in(request):
    login_id = request.GET.get('login_id')
    login_pw = request.GET.get('login_pw')




    print login_id
    print login_pw

    with connections['default'].cursor() as cur:
            query = '''
                select id ,password, no
                from user
                where id = '{id}'and password = MD5('{password}')
            '''.format(id=login_id,password=login_pw)
            print query

            cur.execute(query)

            rows = cur.fetchall()

    if len(rows) == 1:
        request.session['user_id'] = rows[0][2]    #ID 생성과 함께 Session 생성
        return JsonResponse({'return':'success'})

    elif len(rows) != 1:
        return JsonResponse({'return':'fail'})



