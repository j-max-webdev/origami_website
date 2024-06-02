from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Designer(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    first_name: so.Mapped[str] = so.mapped_column(sa.String(140))
    last_name: so.Mapped[str] = so.mapped_column(sa.String(140))
    designs: so.WriteOnlyMapped["Design"] = so.relationship(
        back_populates="model_designer"
    )

    def __repr__(self):
        return "<Designer {}>".format(self.last_name)


# one to many with designer
class Design(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title:  so.Mapped[str] = so.mapped_column(sa.String(300))
    designer_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Designer.id),
                                                   index=True)
    model_designer: so.Mapped[Designer] = so.relationship(back_populates="designs")

    def __repr__(self):
        return "<Design {}>".format(self.title)

