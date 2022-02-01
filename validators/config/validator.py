class Validator:
    def isset(self, value: str)-> bool:
        if not value:
            return True
        return False
    
    def size(self, value: str, min_size, max_size=None)-> bool:
        if max_size:
            if len(value) > max_size or len(value) < min_size:
                return True
            return False

    def contain(self, value: str, contain: str)-> bool:
        if contain not in value:
            return True
        return False
    
    def only_numbers(self, number: str)-> bool:
        if not number.isdigit():
            return True
        return False

