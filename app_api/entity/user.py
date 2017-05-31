from app_api.database import db
import uuid
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = "Users"
    Id = db.Column(db.String(32), default=uuid.uuid4().hex, primary_key=True)
    UserName = db.Column(db.String(64),unique=True)
    RoleId = db.Column(db.String(32),db.ForeignKey("Roles.Id"))
    PassWordHash = db.Column(db.String(128))

    def hash_password(self,password):
        self.PassWordHash = pwd_context.encrypt(password)

    def verify_password(self,password):
        return pwd_context.verify(password,self.PassWordHash)