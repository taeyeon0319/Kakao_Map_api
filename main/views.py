from django.shortcuts import render

f = open("C:\\Users\\태연\\OneDrive\\바탕 화면\\test_playground\\test\\testmap\\static\\서울특별시 용산구_어린이보호구역현황_20210915.csv", 'r')
l = []
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()

data = l[1:11]
# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'data':data})

