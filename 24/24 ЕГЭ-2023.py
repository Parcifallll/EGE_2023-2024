import string
#Только заглавные буквы и цифры. Найти макс длину подстроки, в которой ни одна буквы не стоит рядос с буквой
# и ни одна цифра не стоит рядом с цифрой
f = open("../Файлы/244.txt")
a = f.readline()
p = []
cnt = 1
s = ""
for i in range(len(a) - 1):
    if (((a[i] in string.ascii_uppercase) * (a[i+1] in "0123456789")) == 1 or
            ((a[i+1] in string.ascii_uppercase) * (a[i] in "0123456789")) == 1):
        cnt += 1
        p.append(cnt)
    else:
        cnt = 1
print(max(p))
