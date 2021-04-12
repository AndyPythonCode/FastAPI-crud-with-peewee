from fastapi import APIRouter, status
from .schemas import SchemasBook
from .models import ModelBook

router_book = APIRouter(
    prefix='/books',
    tags=['Books']
)


@router_book.post('/', summary='Create a book', status_code=status.HTTP_201_CREATED)
async def create_book(request: SchemasBook):
    """
        To create a **book**
    """
    obj = ModelBook(**request.dict())
    obj.save()
    return obj


@router_book.get('/', summary='List of books', status_code=status.HTTP_200_OK)
async def list_book():
    """
        To view all every single **books**
    """
    query = ModelBook.select().dicts()
    book = [element for element in query]
    return book


@router_book.get('/{id}', summary='Get one book', status_code=status.HTTP_200_OK)
async def get_book(id: int):
    """
        To get one **book**
    """
    obj = ModelBook.select().where(ModelBook.id == id).dicts().get()
    return obj


@router_book.put('/', summary='Refresh a user', status_code=status.HTTP_202_ACCEPTED)
async def update_book(id: int, request: SchemasBook):
    """
        Updated a single **book**
    """
    fields = [element for element in request if not element[1]
              == None]  # only fields user write
    obj = ModelBook.update(**dict(fields)).where(ModelBook.id == id)
    obj.execute()
    return ModelBook.select().where(ModelBook.id == id).dicts().get()


@router_book.delete('/{id}', summary='Delete a user', status_code=status.HTTP_202_ACCEPTED)
async def update_book(id: int):
    """
        Delete a single **book**
    """
    obj = ModelBook.delete().where(ModelBook.id == id).execute()
    return {'Delete': f'items: {id} successfully delete.'}
