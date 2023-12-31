import shutil
import typing

from fastapi import APIRouter,Depends,HTTPException,UploadFile,File
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session
from functions.files import add_files
from routes.auth import get_current_active_user
from schemas.users import UserCurrent
import typing
Base.metadata.create_all(bind=engine)
from functions.products import add_products, all_products, update_products, delete_products
from schemas.products import *

router_product = APIRouter()

@router_product.post('/add')
def add_product(form:ProductCreate,file:typing.Optional[typing.List[UploadFile]] = File ( None ),db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    product_id=add_products(form=form,db=db)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
            url = str('media/' + file.filename)
            add_files(url=url,source='product',source_id=product_id,db=db)

        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_product.get('/',status_code=200)
def get_product(search:str=None,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_products(search=search,page=page,limit=limit,db=db,status=status,from_date=from_date,end_date=end_date)



@router_product.put('/update',)
def update_product(form:ProductUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_products(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_product.delete('/del',)
def delete_product(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_products(id=id,db=db)
