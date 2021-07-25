import pandas as pd

oriData = pd.read_csv('data.csv')
name = oriData['Name'].values
school = oriData['School'].values
province = oriData['Province'].values
city = oriData['City'].values
# latitude = oriData['Latitude'].values
# longitude = oriData['Longitude'].values

# print(name, school, province, city, latitude, longitude)

# replaceGeo = ''
# for i in range(len(school)):
#     s = '"{}":[{:.2f}, {:.2f}],'.format(school[i], float(latitude), float(longitude))
#     print(s)
#     replaceGeo += s

# replaceVal = ''
# for i in range(len(school)):
#     s = '{{name:"{}", value:"{}"}},'.format(school[i], name[i])
#     print(s)
#     replaceVal += s

# with open('temp.html', 'r', encoding='utf-8') as a:
#     string = a.read()
#     string = string.replace('', )


# with open('index.html', 'w', encoding='utf-8') as b:
#     b.write(string)

replace1 = ''
for i in range(len(name)):
    s = "{{name: '{}', city: '{}', province: '{}', school: '{}'}},".format(
        name[i], city[i], province[i], school[i])
    print(s)
    replace1 += s

with open ('temp.js', 'r', encoding='utf-8') as r:
    string1 = r.read()
    string1 = string1.replace('replace1', replace1)

with open('info.js', 'w', encoding='utf-8') as w:
    w.write(string1)