from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import Comment
from .forms import BlogUpdate
from accounts.models import User, AdminType

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pyperclip
import time

import logging
logger=logging.getLogger(__name__)

def home(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'home.html', {'blogs':blogs,'posts':posts} )

def majorpost(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'majorpost.html', {'blogs':blogs,'posts':posts} )

def newpost(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'newpost.html', {'blogs':blogs,'posts':posts} )

def management(request):
    user = User.objects.filter(admin_type=AdminType.USER)
    return render(request, 'management.html', {'users': user})

def edit(request):
    return render(request, 'edit.html')

def edit_info(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.email=request.POST['email']
        user.dept=request.POST['dept']
        user.general=request.POST['general']
        user.school=request.POST['school']
        user.international=request.POST['international']
        user.employ=request.POST['employ']
        user.scholarship=request.POST['scholarship']
        user.save()
    return redirect('edit')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog = blog_id)
    if request.method =='POST':
        comment = Comment()
        comment.blog = blog_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
    return render(request, 'detail.html', {'blog': blog_detail, 'comments':comments})

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    try:
	    blog.image = request.FILES['image']
    except:
	    blog.image = None
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/faq/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/faq/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'update.html', {'form':form})


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def new(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )

def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "") 

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html', {'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')

def email(request):
    users = User.objects.filter(admin_type=AdminType.USER)
    user_email=[]
    user_notice=[]
    user_dept=[]
    for user in users:
        user_email.append(user.email)
        user_dept.append(user.dept)
        user_notice.append([user.general, user.school, user.international, user.employ, user.scholarship])
    logger.info('user_email = {}'.format(user_email))
    logger.info('user_dept = {}'.format(user_dept))
    logger.info('user_notice = {}'.format(user_notice))

    ############################################
    ############################################
    ############################################

    ############################# 크롤링 변수 ########################################
    
    # 일반공지 , 학사공지 , 국제교류 , 취업 , 장학 
    SEJONG_HOMEPAGE_URLS=['http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333','http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=335',
    'http://board.sejong.ac.kr/pages/notices.html','http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=337',
    'http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=338']
    # 소프트웨어 , 데이터사이언스 , 컴퓨터 공학
    DEPT_HOMEPAGE_URLS=['http://home.sejong.ac.kr/~digitdpt/6.html','http://home.sejong.ac.kr/~dsdpt/8.html','http://home.sejong.ac.kr/~cedpt/32.html']
    TODAY_DATE = input('날짜를 입력해주세요 ex) 2021.01.01   ')

    SEJONG_HOMEPAGE_URLS_titles = [ [] for row in range(len(SEJONG_HOMEPAGE_URLS))]
    SEJONG_HOMEPAGE_URLS_urls = [ [] for row in range(len(SEJONG_HOMEPAGE_URLS))]
    DEPT_HOMEPAGE_URLS_titles = [ [] for row in range(len(DEPT_HOMEPAGE_URLS))]
    DEPT_HOMEPAGE_URLS_urls=[ [] for row in range(len(DEPT_HOMEPAGE_URLS))]

    ###########################chrome 설정 #####################################
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')

    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.implicitly_wait(10)

    ############################# 홈페이지 crawling 실행 ##########################################
    for i in range(0,len(SEJONG_HOMEPAGE_URLS)):
        driver.get(SEJONG_HOMEPAGE_URLS[i])
        time.sleep(1)
        if i==2:
            driver.switch_to.frame(driver.find_element_by_xpath("//*[@id=\"iframe_main\"]"))
        tmp = driver.find_element_by_xpath('/html/body/div/table/tbody')
        tmp = tmp.find_elements_by_tag_name('tr')
        for j in range(0,len(tmp)):
            tbody = driver.find_element_by_xpath('/html/body/div/table/tbody') # 1페이지 글을 모두 가져옴
            tr_Array = tbody.find_elements_by_tag_name('tr') # 1페이지 글을 한 줄씩 쪼개서 tr_Array 담음
            tr = tr_Array[j]  # j번째 글을 tr 이라고 함
            if tr.find_element_by_xpath('/html/body/div/table/tbody/tr/td').text == '등록된 게시물 정보가 없습니다.':
                break
            if tr.find_element_by_class_name('date').text == TODAY_DATE:  # j번째 글의 날짜 == 입력 날짜
                tr.find_element_by_class_name('subject').click()  # j번째 글 클릭
                time.sleep(1)
                SEJONG_HOMEPAGE_URLS_titles[i].append(driver.find_element_by_xpath('/html/body/div/table[1]/thead/tr[1]/td').text) # 제목 추가
                SEJONG_HOMEPAGE_URLS_urls[i].append(driver.current_url) # url 추가
                driver.back()  # 뒤로가기
                if i==2:
                    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id=\"iframe_main\"]"))

    ########################### 학과 crawling 실행 ###################################################
    for i in range(0,len(DEPT_HOMEPAGE_URLS)):
        driver.get(DEPT_HOMEPAGE_URLS[i])
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id=\"iframe_main\"]"))
        tmp = driver.find_element_by_xpath('/html/body/div/table/tbody')
        tmp = tmp.find_elements_by_tag_name('tr')
        for j in range(0,len(tmp)):
            tbody = driver.find_element_by_xpath('/html/body/div/table/tbody') # 1페이지 글을 모두 가져옴
            tr_Array = tbody.find_elements_by_tag_name('tr') # 1페이지 글을 한 줄씩 쪼개서 tr_Array 담음
            tr = tr_Array[j]  # j번째 글을 tr 이라고 함
            if tr.find_element_by_class_name('date').text == TODAY_DATE:  # j번째 글의 날짜 == 입력 날짜
                tr.find_element_by_class_name('subject').click()  # j번째 글 클릭
                time.sleep(1)
                DEPT_HOMEPAGE_URLS_titles[i].append(driver.find_element_by_xpath('/html/body/div/form/table[1]/thead/tr[1]/td').text) # 제목 추가
                DEPT_HOMEPAGE_URLS_urls[i].append(driver.current_url) # url 추가
                driver.back()  # 뒤로가기
                driver.switch_to.frame(driver.find_element_by_xpath("//*[@id=\"iframe_main\"]"))


    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################

    #클립보드에 input을 복사한 뒤 해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
    def copy_input(xpath, input):
        pyperclip.copy(input)
        driver.find_element_by_xpath(xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)

    ######################################### 변수 #############################################
    ID = 'smart_notice_bot'
    PW = 'Smartnoticebot1!'
    TITLE = 'SMART.NOTICE.BOT '+ TODAY_DATE + ' 공지 사항 입니다.'
    ####################################### email 보내기 실행##############################################

    driver.get('https://nid.naver.com/nidlogin.login')
    time.sleep(1)
    copy_input('//*[@id="id"]', ID)
    time.sleep(1)
    copy_input('//*[@id="pw"]', PW)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[7]/button').click()

    for i in range(0,len(user_email)):
        SEJONG_HOMEPAGE_URLS_flag=0
        DEPT_HOMEPAGE_URLS_flag=0

        driver.get('https://mail.naver.com/#%7B%22fClass%22%3A%22write%22%2C%22oParameter%22%3A%7B%22orderType%22%3A%22new%22%2C%22sMailList%22%3A%22%22%7D%7D')
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/fieldset/div/table/tbody/tr[1]/td/div/div[2]/ul/li/div/div[1]/textarea').send_keys(user_email[i])    
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/fieldset/div/table/tbody/tr[1]/td/div/div[2]/ul/li/div/div[1]/textarea').send_keys(Keys.SPACE)
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/fieldset/div/table/tbody/tr[5]/td/div[1]/div[3]/input').send_keys(TITLE)
        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id=\"se2_iframe\"]"))

        driver.find_element_by_xpath('/html/body').send_keys('-------------------학교 공지-------------------')
        driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)

        for j in range(0,len(SEJONG_HOMEPAGE_URLS_titles)):
            if user_notice[i][j] == 'T':
                for k in range(0,len(SEJONG_HOMEPAGE_URLS_titles[j])):
                    SEJONG_HOMEPAGE_URLS_flag=1
                    driver.find_element_by_xpath('/html/body').send_keys(SEJONG_HOMEPAGE_URLS_titles[j][k])
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
                    driver.find_element_by_xpath('/html/body').send_keys(SEJONG_HOMEPAGE_URLS_urls[j][k])
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)

        if SEJONG_HOMEPAGE_URLS_flag==0:
            driver.find_element_by_xpath('/html/body').send_keys('학교 공지가 없습니다.')
            driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
        

        driver.find_element_by_xpath('/html/body').send_keys('-------------------학과 공지-------------------')
        driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)

        
        if user_dept[i] == 'Software':
            j=0
        elif user_dept[i] == 'DataScience':
            j=1
        elif user_dept[i] == 'Computer':
            j=2
        
        for k in range(0,len(DEPT_HOMEPAGE_URLS_titles[j])):
            DEPT_HOMEPAGE_URLS_flag=1
            driver.find_element_by_xpath('/html/body').send_keys(DEPT_HOMEPAGE_URLS_titles[j][k])
            driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
            driver.find_element_by_xpath('/html/body').send_keys(DEPT_HOMEPAGE_URLS_urls[j][k])
            driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
            driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)
        
        if DEPT_HOMEPAGE_URLS_flag==0:
            driver.find_element_by_xpath('/html/body').send_keys('학과 공지가 없습니다.')
            driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)

        time.sleep(1)
        driver.switch_to.default_content()

        if SEJONG_HOMEPAGE_URLS_flag==0 and DEPT_HOMEPAGE_URLS_flag==0:
            driver.get('https://mail.naver.com/#%7B%22fClass%22%3A%22write%22%2C%22oParameter%22%3A%7B%22orderType%22%3A%22new%22%2C%22sMailList%22%3A%22%22%7D%7D')
            time.sleep(1)
            tmp = driver.switch_to.alert
            tmp.accept()
            time.sleep(1)
            continue
        else:
            driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[9]/div[1]/button[1]').click()
            time.sleep(1)
            driver.get('https://mail.naver.com/#%7B%22fClass%22%3A%22write%22%2C%22oParameter%22%3A%7B%22orderType%22%3A%22new%22%2C%22sMailList%22%3A%22%22%7D%7D')
            time.sleep(1)

        time.sleep(2)

    driver.quit()
        
    return render(request, 'management.html', {'users': users, 'data': 'Success'})