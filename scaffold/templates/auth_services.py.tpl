# Auth service

class AuthService:

    @staticmethod
    def user_payload(user):
        return {
            "id": str(user.id),
            "username": user.username,
            "email": user.email
        }


    @staticmethod
    def register(data):
        return {
            "message": "User register successfully"
        }, 200


    @staticmethod
    def login(data):
        pass


    @staticmethod
    def refresh(identity):
        pass


    @staticmethod
    def logout():
        pass


    @staticmethod
    def request_reset_password(data):
        pass


    @staticmethod
    def reset_password(data):
        pass
