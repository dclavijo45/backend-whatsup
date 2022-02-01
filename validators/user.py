from validators.config.validator import Validator

class UserValidator:
    def __init__(self, user: dict):
        self.__user = user
        self.validator = Validator()

    def validate(self)-> dict or None:
        if validate_isset :=self.__validate_isset():
            return validate_isset
        if validate_size := self.__validate_size():
            return validate_size
        if validate_contain := self.__validate_contain():
            return validate_contain

        if validate_numbers := self.__validate_numbers():
            return validate_numbers

        return None

    def __validate_size(self)-> dict or None:
        if self.validator.size(self.__user['name'], 3, 60):
            return {"message": "Invalid 'name'"}

        if self.validator.size(self.__user['number'], 5, 15):
            return {"message": "Invalid 'number'"}

        if self.validator.size(self.__user['device_id'], 5, 15):
            return {"message": "Invalid 'device_id'"}

        if self.validator.size(self.__user['birthday'], 10, 10):
            return {"message": "Invalid 'birthday'"}

        if self.validator.size(self.__user['username'], 3, 10):
            return {"message": f"Invalid 'username'"}
        
        if self.validator.size(self.__user['role'], 1, 1):
            return {"message": f"Invalid 'role'"}

        if self.validator.size(self.__user['status'], 1, 1):
            return {"message": f"Invalid 'status'"}

        if self.__user['description']:
            if self.validator.size(self.__user['description'], 0, 100):
                return {"message": "Invalid 'description'"}
        
        return None

    def __validate_isset(self)-> dict or None:
        if self.validator.isset(self.__user['name']):
            return {"message": "Invalid 'name'"}

        if self.validator.isset(self.__user['number']):
            return {"message": "Invalid 'number'"}

        if self.validator.isset(self.__user['device_id']):
            return {"message": "Invalid 'device_id'"}

        if self.validator.isset(self.__user['birthday']):
            return {"message": "Invalid 'birthday'"}

        if self.validator.isset(self.__user['username']):
            return {"message": "Invalid 'username'"}

        if self.validator.isset(self.__user['role']):
            return {"message": "Invalid 'role'"}

        if self.validator.isset(self.__user['status']):
            return {"message": "Invalid 'status'"}

        return None

    def __validate_contain(self)-> dict or None:
        if self.validator.contain(self.__user['number'], '+'):
            return {"message": f"Invalid 'number'"}
        
        return None

    def __validate_numbers(self)-> dict or None:
        if self.validator.only_numbers(self.__user['number'][1::]):
            return {"message": f"Invalid 'number'"}
        
        return None
