import peewee as pw

from .db import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = pw.CharField(unique=True, null=False)


class Journal(BaseModel):
    owner = pw.ForeignKeyField(User, related_name='journals')
    version = pw.IntegerField()
    uid = pw.CharField(unique=True, null=False, index=True)
    content = pw.BlobField()
    deleted = pw.BooleanField(null=False, default=False)


class Entry(BaseModel):
    journal = pw.ForeignKeyField(Journal, related_name='entries')
    uid = pw.CharField(unique=True, null=False, index=True)
    content = pw.BlobField()

    class Meta:
        order_by = ('id', )


db.create_tables([User, Journal, Entry], safe=True)