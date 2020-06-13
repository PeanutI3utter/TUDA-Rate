from pyquery import PyQuery as pq
from urllib.parse import unquote
import time
import json
import sys
import os


wise = [
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-A3Stya1ZqOhD7glG11H5NFIzuUJEgGfqsnVyXGszxADTWMAOAEO0HufUHzqLlXznlQd~sgIAmOZVNhGmGUcKw6lpHI0oG34STpdUWLEzvswi29QWfZa0mWfY2ByYxS4Qf4wuq0F3juu3vMigDy-LGclFtOBwhKetaie~Lv41x0bZ40o8u88nM6ljutf~g9kr4Hun5rS5ZnB-Pyb4_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-ASEfoAdp-pG4gLG80djNr4ulmQy94ZVjWjmk1anKYfjzf42jGtI5i1RzVfSwtrSRhIFBIZJkct63lD4AG8RZPwexu1Zlu1xjIhBXW0rslZCtxMkabJx5sVLhzI1Urp65OPLnVUuyQP7SH0OiBytSNFG~d8Lgf12n6bdduMmsgw6138Ao315zMYXUqjtV-5pByCr86kWgNvVJYYdM_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-ASSkUvQOt~tWbFCxYXXjpJx8a793kt2RGf6asLeI0fJIz4PpOcI6w7Q2RU5PSHguq3-WVm4ubdqZWWIc00d4TI2P~HRxbmI8XsAUsDvN5ebKjmnzxwADjba-Uw7A-kfM8zgl2k56-qaSu6EHmqNTN55HmOUaVxAgShunkVf7UZQYOw9W9umoQdZaRg9kfSfygARAXDknkLARPAfk_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AJtX~sE9QXsaCGtE2x8P3Fa0HhCCBea6VxHHCqkXgR0NEjr4b4yG~iLVjkeOLHVW99p3kKk8hHrDcVLF6LDQicLsn9~1snXkClV21Jp4JzTcVW2ZYXHTEQLmI9XUnQ0mJdPGZlbzfwiUUZVGOXt1TRJLj8LfC0amqqcFrMe4S7szTJYxz2dC-fUirZsVPhXtmjRqbvtwKLHtkdEM_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AV-RpTDxS~s0g6uuxrv2q7ZVxd~M1o59TDdIvkEq5OOoc1iWdDVoW1Dvi~rJ8KZu6aeU8Fge9CJQQ3Q-1QBIJYiYJC6gS-0aAIhvoNpgmSHguXjvj3XZQEa1pZ3VS4225l~slvSso76-H~pRuZ1R-2KdgJtnm0wZfaGnU93zTy4eoSAec7OSrpyFzZb~K4IRnh9s013cOkaFTrOk_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AP9o-TInGf7~kMofEU-quxUzyJD4C9zmjwmaf18bi3yfsG6lA6DVBAN9Mmf1R93t-Dlb5DjOjb8czTjUMxvNVFeSoISgIzIQMK0kJrMHGiIi0AoECpoCSlfNt1iHged-wfgZztAhdcOOl3x9ERSwps91w-183guN7K3tZtF33xzZh~kdbz-UCMWApNexwYw26te-2ZWm4zxKLWdA_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-ACfuEce4ldg289Cp6GqX0OEXni8Dp3eW6swlNpzv55UPfOa1HUwtR7W7o-j0rsStmwJZ8wpaSSyHD7cpp5-IAoQzZF7nAAwslfYu3LtVkUC~125GFwmPY5V~pW7t57vms6CJVQ6bKgyzHaMEDr3g8woUEcHIf3O3zwRVLw34jNhbvdWsYv-SGZHixxq~gtT2olY16P~4kvoJGcEI_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AopbN-BzeCPTxVLAHk15inkDh1oA~AxrPou0jnKtoFCnkszkWI-T9rhatdX0NyjehvFJ27fTwTNXbOwcPJgn5upig52pcsnQ8DUuNuzHUszH5I6r39hsnGCmmMo7usRO1dJkMuW6p1GsfjxNRkuzMi13oVnaCrs71P4QYHYeM6FXA~AJ4rzKIOBSCm9cErd5TS5q1O8xdlQt2N8o_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-A3vhEG6QzhMyFJkBPshPe6rtazHjY3hSsRNQV~T0-7zmIdEJsJSBSy3fMtcgjyJvYaXWkeFDEc10foFf86WXMLnUcw~eZMOFYS9Ms6KNLJMGYu448C1jMQyzV5a-kOmeq9abZit7c0IyfngOOsa03O7HPUEw3TvEXY1LYyZaaAbwHz-9s4C-Lr78mwsyqOGL-yeblV3DJ--DdR3s_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-Ay8yxPlh5zmi-xNSw2HNqU~8fvqQWmoL6aFLFVXt7DKTk8HDUAbt~YjaGKv3mF4RBCMUtm5FpgA9BzzAzITdajZ~Jcb1GBs~wcFI8vTI7qzk-8gbGOOsKr55GtJ5urZt8PGq9kGA1eIgfXysTpfvGfvJ1Ovnnq8fiCEUhmvS4NDN9v2foYWf4xaW6keqM5TfaISD23kHHtocc9qc_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AEaSvd8W2rPkugWYT8UQDSo0TIR2QOovAsWjPwkRMfagj6HMo3M-eFFOjntd4caS-899TU7S4iMMQOwcriyW-2tj3ZfW9vWdlZvqXOA-bCXCvanRpvvkEsuYVcOGuI8cD2i0BB8K7KMlPqyaenhEcH0WaJep3KntWfoYyJvmEUHctJRFaJyoKtymENypM87SMnejCEUO9P3xJPxc_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AZ9JV-Uvd~9C9zkVy0bTIpBErsexjL~ptJzV0k4i-hibqmhBIKbfyeH3HdHbSP5Eev-5~3fH8XUdIRfA5Q5QIhcBEINStqUUDJJWIicxM1LKson5W55xVQviDNa-U6wdPlcrejB66RTcId5NlmJ8nNjavLX1sgs~tgfG--qfyXIaoQ9uT-JuZf5-F4NUjV83JTrC0BbdvX2NUGxE_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AmIIGXG1OsL7i7OJJlS6yvpggoXczMo7RbVWi42k3DBcVoWLfCzlVLsIPlSuC0kbcjuw~A26Fd8neOUzSbVcfptWYJCD1pLH47G2juM9R4-mNw~p5Wc4PbcfYQlB5H4pz9PY1MNPcrefqUZw2~~X4h1aY~PeE0~TcLNkX1bOotlFOGFJ92PDeBl~qU3DBouyRU3JBI-8SzAOrUSw_"
]

sose = [
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AKRmR7IsHm92bbQo6cZY8B2XbtcvU2e7zbnJmZSqzWyeqZUN4hvG2nr05HXo~dpZmAkNJDNJb4kaw-ZAujE-e6zm389ZHXRt2GmStNhOZLMHqYHaa8jv1LJPHAsXBj9M8l7KaNHMM4AsUUXKuSDx74IpMk4bWs6S~zCJHlhL7kB6-LVIi8dITdjtw7245hXz-RbnHgXlexjUw0Yw_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AT~vEbNS2CDlH4~Ocd5rFaq5CJb3mp1-~k6chnKMXHDWNtJy8bcXj~GSqSI7gYGv6WJici7GbYjrUtxov1qbS8HYvvKt8~pmTen22mwXX3ipBWN9KgUKDfQDcqHLFRDh94nUFuyNvPl3s5RJZpy9ANC8aqGL4sEJDFFVUO5SIkGw2UvyfBFVZ2uqc8dpZ5oRwOiEGy1SdeDAqQNw_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AyZUfWoaFBhtA0srCreiR4P2owrcjH4QT63rhPEK8tWPCk-Sr6h84nxvVMvOdL3NMnUgxO1XHHEF39Q0~riFLVIc4HxS8GjrO~kLYQMA7Iv-fvsO~EIZKKjge0CKEiW7-e95diE6W0AaNUfNKCs~9x4Z4HAxI-lJfN1Zd3td5j1990cd639E-2BrNW~hTyy4oWfOv8y0aRvzyYhE_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AhyvVaaVemf3555MXCUfI1lUMn3oZhSE3zpLR4LeUxNByTigx7kSV7-SKgxPQZmWAq1vAN3a4KWIfvvVfJC~nuu0jVWAWvqT4pgRELQBRDZnkdpa6dAy3LnBQ9EFDKIdAHhaK-RkqZNs2JN5MZ0Ccdc97MEtYunJDURauhegKw5UUHXXijvkAhA-y7IvVoGGmlwkLu~fJfFbGjFI_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AbOw1qYvjV73MnizGGY121o8ioqQ42hO08ebkuZ4BX9TWAjiJEXlMpWcbLqi8iOoWExdpiPHcljNK1TNkuQPieHq4IuSzsl8G7H5t2V5YMyQcBDLKsILxyb-qAagU0jj3AX6rDlEmLWKpKbe0-UOaAq5cRiyRafEw3CBqy79DBZ013DacNNn1LOHPvJMz6FfFykxrBYxi9u76kio_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-A3~TZPQKNPqysi2AADtzK2R-9tNl36OJVzxT1~oa6bKmRgJ8OX0iV0mLr45oXhvZoT6OrxLO97qN95Vwd6jUrBFgX5KcjE3UQuOCC3BEsfkrY4h7beMD5Umtw~bvHZgPoMj-AHApD7Sp6PazgOQL1oOJuKQoqFRBX6LEiFdEa3JJYmp41-Jdwlcj6h7e3aqczHNzCk8lCbe2sDEo_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-Aot3vWmOBs71FLO31cHmkXXHHsHKReMs~4L0QxroYtqdeTE28DETxtOdlr3lEmMY6KQbYF3dVrOIyE9yuSCGqqQUk2MXxxGG2J3tdizD87RmGDyfgwnZmf1qGBo6i4sQOzthpVzRunTE72nYhzP56XBLwDzqTAZZOZcuFeal2ifhh0D0tEZdRPxEbk2722iZDpgngeog26vnEIsI_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AY1B6NJhaQUxHjddCCehYPzYeZ6IAafsL0vheHKbUwyMM9LAebFuNhYMI~m8033EiRGbwNJTcoOoy3yPpYPlt-7T5eFsWPuq7AWyX1pZWGCknZ-Xg4H5DleSb1aG-rRIoNmlGZrcolo9Fkt9z9ZdJmBJbdLNGwg0YNT4L~FqlRr1iIq7WV-1aAJCqfTrY5DRkoZHIWWxdOcpFrVk_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AhyHv-8g2b3k1ILm11vXfqX0mMSWKz8fSn7bDeG2bbpZg5kFSlMAS0FB-93~HP9Am6hpC2m-3gFEyhpcfozBExzg3vYg~uifpKkuzUAMNbSIVM9NvjNuyCyhmyGDyoTRO87WgdD7e9fCHWd2WlaEUAjWVVGJkzEsGWEZZLLcy2gDBL8bI-MA34SYiumEjwkthfu5jlvJ5Qt0-IJE_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AZ4s0pheISj89wuRuZtIC-2vyK9MYlvcAN1X4gaoTuwWRfKamm51eK5JvRTaQ8edGsFhDmHf07H25u3PSDfToaE8tehBOIe3XLCS2HhUEHb1nn1B6Ea16WsM2slp7~h6KNlJU0NXJWQ2rj2XzgdflgLA-x9yGkvX0UOPlBUwFcI1DBr6Uc7-hHTjP9c~mn2bomtCl5PeOP3qjFAk_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AW02IPa5PLBYfjxWTFzC9627P5ELb45O8pOB22sgmMLt2gaTQX78t6bIFsxf~k~7V2~cRB1PopSgNgVwd-bjDNsOPt68CIaH4a~8Nf7qnyZHEkJ5Uyw2Xov69jT~ptVRKn~T9IwHYPEOmkCFAznrUjco0hFenokU9GuCq4uhgt2LDWiERnso6X9GmczGAgpIm6cTLwAcpDDedz~E_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-AF8m7nzkYXGBpy8cbPf~ogpXd5wz0LaSJ460hi67KxFJG4ivlBIrZ29cdxUBTaVNHmDOxG4EjzHVjqBpp9fJ3Y9kJtF3Bn2kSeAC75V2dA1YPZTKHZK9trn1xkr7koXeGGS0G7B~WY2F8VU7nC1j92xy5rBMB4ZrYe6ZafjsUm1mH-d8AWDR8yxpeZFg6VWy9UPICgG5Yz1Qvswo_",
    "https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-ASHkKWh9eZWLR85MlydPGRs8ECuuv25Y7RDeA~ITvtRmnMP7T84equ35PGPURzu6KBcnbgq9TccSYOTfhXoRwKy87scl7p2AilP3qIRZOdCqKDQQ70uSXTpXyy8xP-OmhpzN8Gd335KsmJBW~dsQw1RfXV5x~UbXMA9gNFzhCIXx7rWuN0gcg~R4L9~MeEHP6kSSbWfiVOssFXKU_"
]


WAIT_INTERVAL = 1 # in seconds
RESET_INTERVAL = 15

wis = open("WiSe.xml", "w")
sos = open("SoSe.xml", "w")


class Category:
    def __init__(self, name, url, file, depth = 0):
        self.name = name
        self.url = url
        self.subcategories = list(pq(url=self.url, encoding='utf-8')('ul').filter('.auditRegistrationList').children())
        time.sleep(0.5)
        mods = pq(url=self.url, encoding='utf-8')('tr').filter(".tbdata")
        mods = mods('a')
        self.modules = list(mods.items())
        self.traverseBegun = False
        self.file = file
        self.depth = depth

    def traverse(self):
        try:
            if not self.traverseBegun:
                print(((self.depth-1) * "|   ") + "|___" + self.name)
                self.file.write((self.depth * "\t") + "<Category name='" + self.name.strip().replace("'", "") + "' url='" + self.url + "' >\n")
                self.traverseBegun = True
            time.sleep(WAIT_INTERVAL)
            while len(self.subcategories) > 0:
                subcategory = self.subcategories[0]
                title = str(pq(subcategory)('a').text())
                if title == 'None':
                    raise Exception('title is None.')
                if ("Raumsperrung" in title) or ("Alle Orientierungs- und Einführungsveranstaltungen" in title) or ("Courses held in English" in title):
                    del self.subcategories[0]
                    continue
                subsubcat = Category(title, "https://www.tucan.tu-darmstadt.de" + str(pq(subcategory)('a').attr.href), self.file, self.depth+1)
                subsubcat.traverse()
                del self.subcategories[0]
            while len(self.modules) > 0:
                a = self.modules[0]
                module = Module(a.text(), "https://www.tucan.tu-darmstadt.de" + str(a.attr.href), self.file, self.depth)
                module.getDescription()
                del self.modules[0]
            self.file.write((self.depth * "\t") + "</Category>\n")
        except:
            t, value, traceback = sys.exc_info()
            print(t)
            time.sleep(RESET_INTERVAL)
            self.traverse()


class Module:
    def __init__(self, identifier: str, url, file, depth):
        tokens = identifier.split(' ')
        self.id = tokens[0]
        self.name = ''.join(s + ' ' for s in tokens[1:])
        self.url = url
        self.file = file
        self.depth = depth


    def getDescription(self):
        """
        time.sleep(WAIT_INTERVAL)
        data = pq(url=self.url, encoding='utf-8')('table').filter(lambda i, this: pq(this).attr['class'] == 'tb rw-table rw-all')
        data = data('tr').eq(1)
        data = data('td').eq(0)
        """
        print(((self.depth) * "|   ") + "|" + "___<M> " + self.name)
        self.file.write(((self.depth + 1) * "\t") + "<Module id='" + self.id + "' url='" + self.url + "'>" + self.name.strip() + "</Module>\n")




class CourseCatalog:
    def __init__(self):
        wise, sose = getLatestSemester()
        self.subcategories = [wise, sose]

    def buildCatalog(self):
        for subcat in self.subcategories:
            subcat.traverse() 



def getLatestSemester():
    d = pq(url='https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000463,-Avvarchivstart%2Ehtml', encoding='utf-8')
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

    wise = Category("Wintersemester", wiseurl, wis)
    sose = Category("Sommersemester", soseurl, sos)
    return wise, sose


cc = CourseCatalog()
cc.buildCatalog()


wis.close()
sos.close()