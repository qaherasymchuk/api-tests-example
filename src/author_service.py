from src.entity_service import EntityService  # path may vary


class AuthorService(EntityService):
    def __init__(self):
        super().__init__("/author")
