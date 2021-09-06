from flask_admin import expose
from flask_admin.contrib.sqla import ModelView

from app.core.security import get_password_hash


class UserView(ModelView):
    column_list = ['name', 'email']

    def create_model(self, form):
        # Hash inputed password
        form.password.data = get_password_hash(form.data['password'])
        return super().create_model(form)


class BlogView(ModelView):
    pass
