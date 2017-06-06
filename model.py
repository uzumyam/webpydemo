import web, datetime

db = web.database(dbn='mysql', db='mytest', user='testadmin',
                  host='localhost',port=3306,pw='123')

def get_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id',vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    db.insert('entries',title=title,content=text,posted_on=datetime.datetime.utcnow())

def del_post(id):
    db.delete('entries', where='id=$id', vars=locals())

def update_post(id, title, text):
    db.update('entries', where='id=$id', vars=locals(),
              title=title, content=text)

if __name__ == '__main__':
    new_post("hello", 'this is my first post')