import tkinter as tk
import sqlite3
import os
import io
import requests
import webbrowser
import PIL
import tempfile, base64, zlib
from PIL import Image,ImageTk


window = tk.Tk()



ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


window.geometry('1060x600')
window.title('khonello')
window.resizable(width= False, height= False)
window.iconbitmap(default=ICON_PATH)
 

def create():

    database = 'Database'

    try:
        
        mkdir = os.mkdir(database)
    except FileExistsError:
        pass


    dir = os.getcwd() + '\\' + database
    chdir = os.chdir(dir)

    
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS characters(
        id INTEGER PRIMARY KEY,
        Hulk BLOB,
        HulkDescrip TEXT,
        IronMan BLOB,
        IronManDescrip TEXT,
        CaptainAmerica BLOB,
        CaptainAmericaDescrip TEXT,
        Thor BLOB,
        ThorDescrip TEXT,
        Thumbnail BLOB,
        Favicon BLOB,
        Font BLOB,
        God INTEGER
    )""")

    try:
        cursor.execute("INSERT INTO characters VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ",(1,b'','',b'','',b'','',b'','',b'',b'',b'',1))
        cursor.execute("INSERT INTO characters VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ",(2,b'','',b'','',b'','',b'','',b'',b'',b'',1))
        cursor.execute("INSERT INTO characters VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ",(3,b'','',b'','',b'','',b'','',b'',b'',b'',1))
        cursor.execute("INSERT INTO characters VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ",(4,b'','',b'','',b'','',b'','',b'',b'',b'',1))

        connection.commit()
        
    except sqlite3.IntegrityError:
        connection.commit()



def getfiles():
    
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    try:
        resp = requests.get('https://www.google.com/')
    except requests.exceptions.ConnectionError:
        return
    

    def hulk():


        hulk1 = requests.get('https://i.ibb.co/rsG9qmP/Hulk-1.png').content
        hulk2 = requests.get('https://i.ibb.co/Wnscwws/Hulk-2.png').content
        hulk3 = requests.get('https://i.ibb.co/wy1FxQf/Hulk-3.png').content
        hulk4 = requests.get('https://i.ibb.co/gwtc2NR/Hulk-4.png').content

        cursor.execute("UPDATE characters SET Hulk= ? WHERE id= 1", (hulk1,))
        cursor.execute("UPDATE characters SET Hulk= ? WHERE id= 2", (hulk2,))
        cursor.execute("UPDATE characters SET Hulk= ? WHERE id= 3", (hulk3,))
        cursor.execute("UPDATE characters SET Hulk= ? WHERE id= 4", (hulk4,))

        connection.commit()


    def iron_man():


        ironMan1 = requests.get('https://i.ibb.co/M9PrY4K/Iron-Man-1.png').content
        ironMan2 = requests.get('https://i.ibb.co/zXcD7bY/Iron-Man-2.png').content
        ironMan3 = requests.get('https://i.ibb.co/SfsC5DT/Iron-Man-3.png').content
        ironMan4 = requests.get('https://i.ibb.co/1KQZmnx/Iron-Man-4.png').content

        cursor.execute("UPDATE characters SET IronMan= ? WHERE id= 1", (ironMan1,))
        cursor.execute("UPDATE characters SET IronMan= ? WHERE id= 2", (ironMan2,))
        cursor.execute("UPDATE characters SET IronMan= ? WHERE id= 3", (ironMan3,))
        cursor.execute("UPDATE characters SET IronMan= ? WHERE id= 4", (ironMan4,))

        connection.commit()        

    def captain():

        captainAmerica1 = requests.get('https://i.ibb.co/6RmDZ5D/Captain-America-1.png').content
        captainAmerica2 = requests.get('https://i.ibb.co/9yzY1Cv/Captain-America-2.png').content
        captainAmerica3 = requests.get('https://i.ibb.co/cDyXBb5/Captain-America-3.png').content
        captainAmerica4 = requests.get('https://i.ibb.co/1smjg9s/Captain-America-4.png').content

        cursor.execute("UPDATE characters SET CaptainAmerica= ? WHERE id= 1", (captainAmerica1,))
        cursor.execute("UPDATE characters SET CaptainAmerica= ? WHERE id= 2", (captainAmerica2,))
        cursor.execute("UPDATE characters SET CaptainAmerica= ? WHERE id= 3", (captainAmerica3,))
        cursor.execute("UPDATE characters SET CaptainAmerica= ? WHERE id= 4", (captainAmerica4,))

        connection.commit()    

    def thor():

        thor1 = requests.get('https://i.ibb.co/0BqDCgQ/Thor-1.png').content
        thor2 = requests.get('https://i.ibb.co/kczJKdH/Thor-2.png').content
        thor3 = requests.get('https://i.ibb.co/5kVNQVY/Thor-3.png').content
        thor4 = requests.get('https://i.ibb.co/r7KybhC/Thor-4.png').content

        cursor.execute("UPDATE characters SET Thor= ? WHERE id =1", (thor1,))
        cursor.execute("UPDATE characters SET Thor= ? WHERE id =2", (thor2,))
        cursor.execute("UPDATE characters SET Thor= ? WHERE id =3", (thor3,))
        cursor.execute("UPDATE characters SET Thor= ? WHERE id =4", (thor4,))

        connection.commit()


    def thumbnail():

        hulkThumbnail = requests.get('https://i.ibb.co/MM8dyqR/Hulk.png').content
        ironManThumbnail = requests.get('https://i.ibb.co/Sc5xXZD/Iron-Man-head.png').content
        captainAmericaThumbnail = requests.get('https://i.ibb.co/QvTHq1T/Captain-America.png').content
        thorThumbnail = requests.get('https://i.ibb.co/Rjtccm3/Thor.png').content

        cursor.execute("UPDATE characters SET Thumbnail= ? WHERE id =1", (hulkThumbnail,))
        cursor.execute("UPDATE characters SET Thumbnail= ? WHERE id =2", (ironManThumbnail,))
        cursor.execute("UPDATE characters SET Thumbnail= ? WHERE id =3", (captainAmericaThumbnail,))
        cursor.execute("UPDATE characters SET Thumbnail= ? WHERE id =4", (thorThumbnail,))

        connection.commit()
    
    def favicon():

        ico = requests.get(url= 'https://s48.freeconvert.com/task/619d34c56c63e400112e3a90/Avengers%20RGB.ico').content

        cursor.execute("UPDATE characters SET Favicon= ? WHERE id =1", (ico,))
        connection.commit()

    def title_font():

        font = requests.get(url= 'https://filedropper.com/d/s/download/sv61y229mBKyQrzSnFIxXolWr0B82Z').content

        cursor.execute("UPDATE characters SET Font= ? WHERE id =1", (font,))
        connection.commit()

    hulk()
    iron_man()
    captain()
    thor()

    thumbnail()
    favicon()
    title_font()


def makeAPICalls():
    
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    try:
        resp = requests.get('https://www.google.com/')
    except requests.exceptions.ConnectionError:
        return

    l = 'https://gateway.marvel.com:443/v1/public/characters?ts=1&apikey=40532d3ffb1fcb60512c237ea0c6877d&hash=80de58e26c030f7f543053dc00408972'

    hulk = requests.get(url= l, params= {'name' : 'Hulk'})
    iron_man = requests.get(url= l, params= {'name' : 'Iron Man'})
    captain_america = requests.get(url= l, params= {'name' : 'Captain America'})
    thor = requests.get(url= l, params= {'name' : 'Thor'})

    hulkJsn = hulk.json()
    hulkDone = hulkJsn['data']['results'][0]['description']

    iron_manJsn = iron_man.json()
    iron_manDone = iron_manJsn['data']['results'][0]['description']

    captain_americaJsn = captain_america.json()
    captain_americaDone = captain_americaJsn['data']['results'][0]['description']

    thorJsn = thor.json()
    thorDone = thorJsn['data']['results'][0]['description']
        

    cursor.execute("UPDATE characters SET HulkDescrip= ?,IronManDescrip= ?,CaptainAmericaDescrip= ?,ThorDescrip= ? WHERE id= 1", (hulkDone,iron_manDone,captain_americaDone,thorDone))
    connection.commit()



def chk_God():
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT God FROM characters WHERE id= 1")
    result = cursor.fetchone()


    if result[0] == 1:

        cursor.execute("UPDATE characters SET God= 0 WHERE id= 1")
        connection.commit()

        makeAPICalls()
        getfiles()


    else:
        connection.commit()


def charac(*arg):

    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()


    hulkCursor = cursor.execute("SELECT Hulk FROM characters")
    hulkResult = cursor.fetchall()

    ironManCursor = cursor.execute("SELECT IronMan FROM characters")
    ironManResult = cursor.fetchall()

    captainAmericaCursor = cursor.execute("SELECT CaptainAmerica FROM characters")
    captainAmericaResult = cursor.fetchall()

    thorCursor = cursor.execute("SELECT Thor FROM characters")
    thorResult = cursor.fetchall()



    im1 = hulkResult[1][0]
    im2 = ironManResult[1][0]
    im3 = captainAmericaResult[1][0]
    im4 = thorResult[1][0]

    im1byte = io.BytesIO(im1)
    im2byte = io.BytesIO(im2)
    im3byte = io.BytesIO(im3)
    im4byte = io.BytesIO(im4)

    imgg1 = ImageTk.PhotoImage(Image.open(im1byte).resize((250,170)))
    imgg2 = ImageTk.PhotoImage(Image.open(im2byte).resize((200,170)))
    imgg3 = ImageTk.PhotoImage(Image.open(im3byte).resize((200,170)))
    imgg4 = ImageTk.PhotoImage(Image.open(im4byte).resize((250,170)))


    images = {
        'firstImage' : imgg1,
        'secondImage' : imgg2,
        'thirdImage' : imgg3,
        'fourthImage' : imgg4
    }
    
    return images


create()
chk_God()

pf_width = 1080
pf_height = 400

tf_width = 750
tf_height = 170

bf_width = 1050
bf_height = 290

ff_width = 890
ff_height = 200

ff_Children_width = 100
ff_Children_height = 70

af_width = 220
af_height = 70

bg_color1 = 'black'
bg_color2 = 'white'


def thumbnail():

    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT Thumbnail FROM characters")
    result = cursor.fetchall()

    try:
        hulkThumbnail = Image.open(io.BytesIO( result[0][0] ))
        ironManThumbnail = Image.open(io.BytesIO( result[1][0] ))
        captainAmericaThumbnail = Image.open(io.BytesIO( result[2][0] ))
        thorThumbnail = Image.open(io.BytesIO( result[3][0] ))
    except PIL.UnidentifiedImageError:
        pass

    thumbnails = {
        'thumbnail1' : hulkThumbnail,
        'thumbnail2' : ironManThumbnail,
        'thumbnail3' : captainAmericaThumbnail,
        'thumbnail4' : thorThumbnail
    }
    
    return thumbnails


parentFrame1 = tk.Frame(master= window, width= pf_width, height= pf_height, background= bg_color1,padx= 20, pady= 10)
parentFrame1.grid(column= 0, row= 0)

parentFrame2 = tk.Frame(master= window, width= 1060, height= 220, background= bg_color2, padx= 0, pady= 0)
parentFrame2.grid(column= 0, row= 1)

titleFrame = tk.Frame(master= parentFrame1, width= tf_width, height= tf_height, background= bg_color1, padx= 20, pady= 20)
titleFrame.grid(column= 0, row= 0)

bodyFrame = tk.Frame(master= parentFrame1, width= bf_width, height= bf_height, background= bg_color1, padx= 25, pady= 7)
bodyFrame.grid(column= 0, row= 1)

footerFrame = tk.Frame(master= parentFrame1, width= ff_width ,height= ff_height, background= bg_color1, padx= 20,pady= 2)
footerFrame.grid(column= 0, row= 2)

footerInnerFrame1 = tk.Frame(master= footerFrame, width= ff_Children_width, height= ff_Children_height, background= bg_color1, padx= 7, pady= 0)
footerInnerFrame1.grid(column= 0, row= 0)

footerInnerFrame2 = tk.Frame(master= footerFrame, width= ff_Children_width, height= ff_Children_height, background= bg_color1, padx= 7, pady= 0)
footerInnerFrame2.grid(column= 1, row= 0)

footerInnerFrame3 = tk.Frame(master= footerFrame, width= ff_Children_width, height= ff_Children_height, background= bg_color1, padx= 7, pady= 0)
footerInnerFrame3.grid(column= 2, row= 0)

footerInnerFrame4 = tk.Frame(master= footerFrame, width= ff_Children_width, height= ff_Children_height, background= bg_color1, padx= 7, pady= 0)
footerInnerFrame4.grid(column= 3, row= 0)


try:
    footerInnerFrame1Path =  thumbnail()['thumbnail1'].resize(size= (100,50))
    footerInnerFrame2Path =  thumbnail()['thumbnail2'].resize(size= (70,50))
    footerInnerFrame3Path =  thumbnail()['thumbnail3'].resize(size= (70,50))
    footerInnerFrame4Path =  thumbnail()['thumbnail4'].resize(size= (100,50))
except UnboundLocalError:
    pass


try:
    titleLabel = tk.Label(master= titleFrame, foreground= bg_color2, background= bg_color1,text= 'AVENGERS', font= ('BatmanForeverAlternate' ,20), justify= 'center', width= 20)
    titleLabel.grid(column= 0, row= 0)
except:
    titleLabel = tk.Label(master= titleFrame, foreground= bg_color2, background= bg_color1,text= 'AVENGERS', font= ('Arial Bold' ,20), justify= 'center', width= 20)
    titleLabel.grid(column= 0, row= 0)

try:
    bodyImage1 = charac('firstImage')['firstImage']
    bodyImage2 = charac('secondImage')['secondImage']
    bodyImage3 = charac('thirdImage')['thirdImage']
    bodyImage4 = charac('fourthImage')['fourthImage']
except PIL.UnidentifiedImageError:
    pass

try:
    footerInnerFrame1Image = ImageTk.PhotoImage(footerInnerFrame1Path)
    footerInnerFrame2Image = ImageTk.PhotoImage(footerInnerFrame2Path)
    footerInnerFrame3Image = ImageTk.PhotoImage(footerInnerFrame3Path)
    footerInnerFrame4Image = ImageTk.PhotoImage(footerInnerFrame4Path)
except:
    pass

try:
    bodyLabelImage1 = tk.Label(master= bodyFrame, width= 250, height= 170, image= bodyImage1)
    bodyLabelImage2 = tk.Label(master= bodyFrame, width= 200, height= 170, image= bodyImage2)
    bodyLabelImage3 = tk.Label(master= bodyFrame, width= 200, height= 170, image= bodyImage3)
    bodyLabelImage4 = tk.Label(master= bodyFrame, width= 250, height= 170, image= bodyImage4)
except:
    pass


def img1(*args):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT Hulk FROM characters")
    characResult = cursor.fetchall()

    im1 = characResult[0][0]
    im1byte = io.BytesIO(im1)

    img1Image = Image.open(im1byte).show('Marvel')




def img2(*args):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT IronMan FROM characters")
    characResult = cursor.fetchall()

    im2 = characResult[0][0]
    im2byte = io.BytesIO(im2)

    img2Image = Image.open(im2byte).show('Marvel')


def img3(*args):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT CaptainAmerica FROM characters")
    characResult = cursor.fetchall()    

    im3 = characResult[3][0]
    im3byte = io.BytesIO(im3)

    img3Image = Image.open(im3byte).show('Marvel')


def img4(*args):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT Thor FROM characters")
    characResult = cursor.fetchall()    

    im4 = characResult[3][0]
    im4byte = io.BytesIO(im4)

    img4Image = Image.open(im4byte).show('Marvel')


def hulk_link():

    link = 'http://marvel.com/universe/Hulk_(Bruce_Banner)?utm_campaign=apiRef&utm_source=40532d3ffb1fcb60512c237ea0c6877d'
    webbrowser.open_new(url= link )

def ironMan_link():
    link = 'http://marvel.com/universe/Iron_Man_(Anthony_Stark)?utm_campaign=apiRef&utm_source=40532d3ffb1fcb60512c237ea0c6877d'
    webbrowser.open_new(url= link)

def captain_link():
    link = 'http://marvel.com/universe/Captain_America_(Steve_Rogers)?utm_campaign=apiRef&utm_source=40532d3ffb1fcb60512c237ea0c6877d'
    webbrowser.open_new(url= link)

def thor_link():
    link = 'http://marvel.com/universe/Thor_(Thor_Odinson)?utm_campaign=apiRef&utm_source=40532d3ffb1fcb60512c237ea0c6877d'
    webbrowser.open_new(url= link)

try:
    footerInnerFrame1ImageLabel = tk.Label(master= footerInnerFrame1, background= bg_color1, width= 90, height= 70, image= footerInnerFrame1Image, borderwidth= 0)
    footerInnerFrame2ImageLabel = tk.Label(master= footerInnerFrame2, background= bg_color1, width= 90, height= 70, image= footerInnerFrame2Image, borderwidth= 0)
    footerInnerFrame3ImageLabel = tk.Label(master= footerInnerFrame3, background= bg_color1, width= 90, height= 70, image= footerInnerFrame3Image, borderwidth= 0)
    footerInnerFrame4ImageLabel = tk.Label(master= footerInnerFrame4, background= bg_color1, width= 90, height= 70, image= footerInnerFrame4Image, borderwidth= 0)
except:
    pass
try:
    bodyLabelImage1.bind('<Button-1>', img1)
    bodyLabelImage2.bind('<Button-1>', img2)
    bodyLabelImage3.bind('<Button-1>', img3)
    bodyLabelImage4.bind('<Button-1>', img4)
except :
    pass

try:
    footerInnerFrame1ImageLabel.bind('<Button-3>', func= lambda arg: hulk_link())
    footerInnerFrame2ImageLabel.bind('<Button-3>', func= lambda arg: ironMan_link())
    footerInnerFrame3ImageLabel.bind('<Button-3>', func= lambda arg: captain_link())
    footerInnerFrame4ImageLabel.bind('<Button-3>', func= lambda arg: thor_link())
except:
    pass

try:
    bodyLabelImage1.grid(column= 0,row= 0 ,padx= 7)
    bodyLabelImage2.grid(column= 1,row= 0 ,padx= 5)
    bodyLabelImage3.grid(column= 2,row= 0 ,padx= 5)
    bodyLabelImage4.grid(column= 3,row= 0 ,padx= 7)
except:
    pass

try:
    footerInnerFrame1ImageLabel.grid(column= 0, row= 0)
    footerInnerFrame2ImageLabel.grid(column= 0, row= 0)
    footerInnerFrame3ImageLabel.grid(column= 0, row= 0)
    footerInnerFrame4ImageLabel.grid(column= 0, row= 0)
except:
    pass

try:
    descriptionLabel = tk.Label(master= parentFrame2, text= 'Welcome', font= ('Comic Sans MS',10), justify= 'center', padx= 5)
    descriptionLabel.grid(column= 0, row= 0)
except:
    pass


def hulk_descrip(*arg):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT HulkDescrip FROM characters")
    result = cursor.fetchone()[0]
    description = result.replace(',','\n')

    descriptionLabel.configure(text= description, font= ('Comic Sans MS',10), justify= 'center', padx= 5)



def ironMan_descrip(*arg):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT IronManDescrip FROM characters")
    result = cursor.fetchone()[0]
    description = result.replace(',','\n')

    descriptionLabel.configure(text= description, font= ('Comic Sans MS',10), justify= 'center', padx= 5)


def captainAmerica_descrip(*arg):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT CaptainAmericaDescrip FROM characters")
    result = cursor.fetchone()[0]
    description = result.replace(',','\n')

    descriptionLabel.configure(text= description, font= ('Comic Sans MS',10), justify= 'center', padx= 5)


def thor_descrip(*arg):
    connection = sqlite3.connect('marvel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT ThorDescrip FROM characters")
    result = cursor.fetchone()[0]
    description = result.replace(',','\n')

    descriptionLabel.configure(text= description, font= ('Comic Sans MS',10), justify= 'center', padx= 5)

try:
    footerInnerFrame1ImageLabel.bind('<Button-1>', func= hulk_descrip)
    footerInnerFrame2ImageLabel.bind('<Button-1>', func= ironMan_descrip)
    footerInnerFrame3ImageLabel.bind('<Button-1>', func= captainAmerica_descrip)
    footerInnerFrame4ImageLabel.bind('<Button-1>', func= thor_descrip)
except:
    pass

window.mainloop()