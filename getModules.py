from pyquery import PyQuery as pq
import time
import json

class Category:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.subcategories = []
        self.modules = []

    def traverse(self):
        print(self.name)
        try:
            time.sleep(5)
            subcategories = pq(url=self.url)('ul').filter('.auditRegistrationList')
            if len(subcategories) > 0:
                subcategories = subcategories.children()
                subcategories.filter(lambda i, this: not ("Raumsperrung" in pq(this).attr.title))
                for subcategory in subcategories.items():
                    toBeAdded = Category(subcategory.attr.title, "https://www.tucan.tu-darmstadt.de" + str(subcategory('a').attr.href))
                    self.subcategories.append(toBeAdded)
                    toBeAdded.traverse()
            modules = pq("https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-A~cT0pRzARx6w5-Xn1nYR7725ig0H5Wnl0ibriku~OM7V2acDx~diJ7EgVECb0DC15ZS8te5mvROd-aEXv2qknsU~u9DXdQhilbsKx-6X-w-QimI4At6P6peRg7S6Yd3essqY1ySwGl3VxIxqCQg4~rHXJWQ151mauqz6Wet6QS80RwZwJjZm-52~OVqTb2J0xBsnvETzn-NVssA_")('tr').filter(".tbdata")
            ref = modules('a')
            for a in ref.items():
                module = Module(a.text(), a.attr.href)
                self.modules.append(module)
                module.getDescription()
                
        except:
            pass


class Module:
    def __init__(self, identifier: str, url):
        tokens = identifier.split(' ')
        self.id = tokens[0]
        self.name = ''.join(s + ' ' for s in tokens[1:])
        self.url = "https://www.tucan.tu-darmstadt.de" + url

    def getDescription(self):
        time.sleep(1)
        data = pq(url=self.url)('table').filter(lambda i, this: pq(this).attr['class'] == 'tb rw-table rw-all')
        data = data('tr').eq(1)
        data = data('td').eq(0)
        self.data = data.html()




class CourseCatalog:
    def __init__(self):
        wise, sose = getLatestSemester()
        self.subcategories = [wise, sose]

    def buildCatalog(self):
        [subcat.traverse() for subcat in self.subcategories]



def getLatestSemester():
    d = pq(url='https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000463,-Avvarchivstart%2Ehtml')
    pastsemester = d('li').filter(lambda i, this: pq(this).attr['class'] == "intern depth_3 linkItem ")


    tmp = pastsemester.eq(0)
    tmp2 = pastsemester.eq(1)

    text1 = tmp('a').text()

    if 'Winter' in text1:
        wise = tmp
        sose = tmp2
    else:
        wise = tmp2
        sose = tmp

    wiseurl = "https://www.tucan.tu-darmstadt.de" + str(pq(wise)('a').attr.href)
    soseurl = "https://www.tucan.tu-darmstadt.de" + str(pq(sose)('a').attr.href)

    wise = Category("Wintersemester", wiseurl)
    sose = Category("Sommersemester", soseurl)
    return wise, sose


cc = CourseCatalog()
cc.buildCatalog()

save = json.dumps(cc, default=lambda x: x.__dict__)

f = open('CourseCatalog.json', 'w')
f.write(save)
f.close()