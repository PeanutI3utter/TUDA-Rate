from pyquery import PyQuery as pq

class Course:
    def __init__(self, name, link):
        self.name = name
        self.link = 'www.tucan.tu-darmstadt.de' + link

    def getLink(self):
        return self.link

    def getName(self):
        return self.name

    def __str__(self):
        return '{\n\tCourse: ' + str(self.name) + '\n\tLink: ' + str(self.link) + '\n}'

    def __repr__(self):
        return '{\n\tCourse: ' + str(self.name) + '\n\tLink: ' + str(self.link) + '\n}'

    
d = pq(url="https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-ARykwIoAoe25QV72nKSmnPe~eIKBRCEh1ONpCunbzfygB8Slxcja9vHWtJjrgkT2M7meJQ5Hw~V~Ik1CiYMplOjb8zhzZdMDEYSL~IJ5mKiWxUFlx3tWh5gweWapt64HGfWAjElStoPfHj8ou2yypXcBe02tRfwGf5MC-X694JWcdogEXTb6yoHAk2A__")
fblist = d('ul').filter('.auditRegistrationList').children()

courseRefs = [Course(course.attr.title, course('a').attr.href) for course in  fblist.items()]


print(courseRefs)