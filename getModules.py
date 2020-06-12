from pyquery import PyQuery as pq

class Category:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def traverse(self):
        subcategories = pq(url=self.url)('ul').filter('.auditRegistrationList')
        if len(subcategories) > 0:
            subcategories = subcategories.children()
            


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
print(cc.subcategories)