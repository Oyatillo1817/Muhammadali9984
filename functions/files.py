import datetime
from models.files import Files
def add_files(url, source,source_id,db):

    new_files=Files(
                   file=url,
                   source=source,
                   source_id=source_id,
                   date=datetime.datetime.today()

                   )
    db.add(new_files)
    db.commit()
    db.refresh(new_files)
    balance_adding(type=form.type,money=form.money,db=db)
    return{"data" : "User add base"}
