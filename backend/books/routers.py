from fastapi import APIRouter, status
from .schemas import SchemasBook
from .models import ModelBook
from decorators.dbDecorators import itemNotFound
from peewee import DoesNotExist

router_book = APIRouter(
    prefix='/books',
    tags=['Books']
)


# CREATE
@router_book.post('/', summary='Create a book', status_code=status.HTTP_201_CREATED)
async def create_book(request: SchemasBook):
    """
        To create a **book**
    """
    obj = ModelBook(**request.dict())
    obj.save()
    return obj.__data__


# LIST
@router_book.get('/', summary='List of books', status_code=status.HTTP_200_OK)
async def list_book():
    """
        To view all every single **books**
    """
    return ModelBook.select().order_by(-ModelBook.id).dicts()[::]


# RETRIEVE READ
@router_book.get('/{id}', summary='Get one book', status_code=status.HTTP_200_OK)
@itemNotFound
async def get_book(id: int):
    """
        To get one **book**
    """
    return ModelBook.get_by_id(id).__data__


# UPDATED
@router_book.put('/{id}', summary='Refresh a user', status_code=status.HTTP_202_ACCEPTED)
@itemNotFound
async def update_book(id: int, request: SchemasBook):
    """
        Updated a single **book**
    """
    fields = [element for element in request if not element[1]
              == None]  # only fields user write
    if ModelBook.update(**dict(fields)).where(ModelBook.id == id).execute():
        return {'Update': f'items: {id} successfully updated'}
    else:
        raise DoesNotExist


# DELETE
@router_book.delete('/{id}', summary='Delete a user', status_code=status.HTTP_202_ACCEPTED)
@itemNotFound
async def update_book(id: int):
    """
        Delete a single **book**
    """
    ModelBook.get_by_id(id).delete_instance()
    return {'Delete': f'items: {id} successfully delete.'}
