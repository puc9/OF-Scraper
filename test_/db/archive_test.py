import tempfile
from ofscraper.db.operations import *
import pytest
from  test_.test_constants import *
from ofscraper.classes.posts import Post
from ofscraper.classes.media import Media
import pathlib

def test_archive_create(mocker):
    with tempfile.NamedTemporaryFile() as p:
        try:
            a=mocker
            a.trace=None
            mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathHelper",return_value=pathlib.Path(p.name))
            mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathCopyHelper",return_value=pathlib.Path(p.name))
            mocker.patch("ofscraper.db.operations.log",new_callabe=a)              
            create_post_table("11111","test")
        except:
            raise Exception



# def test_archive_failure(mocker):
#     with tempfile.NamedTemporaryFile() as p:   
#         with pytest.raises(Exception):
#             a=mocker
#             a.trace=None
#             mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathHelper",return_value=pathlib.Path(p.name))
#             mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathCopyHelper",return_value=pathlib.Path(p.name))
#             mocker.patch("ofscraper.db.operations.log",new_callabe=a)              
#             create_post_table("11111")


def test_archive_insert(mocker):
    with tempfile.NamedTemporaryFile() as p:
        try:
            a=mocker
            a.trace=None
            mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathHelper",return_value=pathlib.Path(p.name))
            mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathCopyHelper",return_value=pathlib.Path(p.name))
            mocker.patch("ofscraper.db.operations.log",new_callabe=a)              
            create_post_table("11111","test")
            write_post_table(Post(ARCHIVED_POST_EXAMPLE,"11111","test"),"11111","test")
        except Exception as E:
            print(E)
            raise Exception
# def test_archive_insert_failure(mocker):
#     with tempfile.NamedTemporaryFile() as p:   
#         with pytest.raises(Exception):
#             a=mocker
#             a.trace=None
#             mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathHelper",return_value=pathlib.Path(p.name))
#             mocker.patch("ofscraper.classes.placeholder.Placeholders.databasePathCopyHelper",return_value=pathlib.Path(p.name))
#             mocker.patch("ofscraper.db.operations.log",new_callabe=a)              
#             create_post_table("11111","test")
#             write_post_table(Post(ARCHIVED_POST_EXAMPLE,"111","test2"))

