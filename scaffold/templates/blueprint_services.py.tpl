# {{blueprint_name}} service

class HelloService:
    
    @staticmethod
    def get_hello():
        return {
            "message": "Hello from {{blueprint_name}}"
        }, 200
