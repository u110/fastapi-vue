from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Notes
from src.schemas.notes import NoteOutSchema


async def get_notes():
    return await NoteOutSchema.from_queryset(Notes.all())


async def get_note(note_id):
    return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))


async def create_note(note, current_user) -> NoteOutSchema:
    note_dict = note.dict(exclude_unset=True)
    note_dict["author_id"] = current_user.id
    note_obj = await Notes.create(**note_dict)
    return await NoteOutSchema.from_tortoise_orm(note_obj)


async def update_note(note_id, note, current_user) -> NoteOutSchema:
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Note {note_id} not found")

    if db_note.author.id == current_user.id:
        deleted_count = await Notes.filter(id=note.id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail="Note {note_id} not found")
        return "Deleted note {note_id}"

    raise HTTPException(status_code=403, detail="Not authorized to delete")
