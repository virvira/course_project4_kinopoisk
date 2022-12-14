from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).first()
        return user

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, data):
        user = self.get_one(data.get('id'))

        if data.get('name') is not None:
            user.name = data.get('name')
        if data.get('surname') is not None:
            user.surname = data.get('surname')
        if data.get('favourite_genre_id') is not None:
            user.favourite_genre_id = data.get('favourite_genre_id')

        self.session.add(user)
        self.session.commit()

    def update_password(self, data):
        user = self.get_one(data.get('id'))
        user.password = data.get('password_2')

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
