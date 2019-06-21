from pybloods.model.orm import NoteGroup


def search():
    return ApiApp.db().query(NoteGroup)
