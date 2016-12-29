#!/usr/bin/env python
#coding:utf8

import urllib
import urllib2
import re

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n  ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

class BDTB(object):
    #seeLZ: 0:查看所有回复 1:只看楼主回复
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()

    #获取帖子页面数内容  
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            #print response.read()
            html = response.read().decode('utf-8')
            return html

        except urllib2.URLError,e:
            if hasattr(e, 'reason'):
                print u'连接百度贴吧失效，错误原因:', e.reason
                return None
    #获取帖子标题
    def getTitle(self, pageNum):
        page = self.getPage(pageNum)
        pat1 = re.compile(r'<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pat1, page)
        if result:
            print result.group(1)
        else:
            return None
    #获取帖子回复页数
    def getPageNum(self, pageNum):
        page = self.getPage(pageNum)
        pat1 = re.compile(r'<li class="l_reply_num".*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pat1, page)
        if result:
            print result.group(1)
            return int(result.group(1))
        else:
            return None
    #获取帖子回复内容
    def getContent(self, pageNum):
        page = self.getPage(pageNum)
        pat1 = re.compile(r'<div id="post_content.*?>(.*?)</div>', re.S)
        items = re.findall(pat1, page)
        # for item in items:
        #     print item
        floor = 1
        for item in items:
            print ''
            print '第%s页的帖子内容:' %pageNum
            print floor,u'楼-----------------------'
            print self.tool.replace(item)
            floor += 1


#调用执行主函数
if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseURL,0)
    bdtb.getTitle(1)
    page_num = bdtb.getPageNum(1)
    for i in xrange(page_num):
        bdtb.getContent(i+1)