from abc import ABC, abstractmethod\


class AbstractRepository(ABC):
    @abstractmethod
    def add_node():
        raise NotImplementedError

    @abstractmethod
    def add_rel():
        raise NotImplementedError
    
    # @abstractmethod
    # def del_node():
    #     raise NotImplementedError
    
    # @abstractmethod
    # def find_node():
    #     raise NotImplementedError



class NeoModelsRep(AbstractRepository):
    
    model = None

    def add_node(self, **kwargs):
        try:
            node = self.model(**kwargs).save()
            return node
        except Exception as e:
            print(f"Error creating node: {e}")
            return None
        
    def add_rel(self, from_node, to_node, relationship_type, **properties):
        try:
            relationship = getattr(from_node, relationship_type, None)
            if relationship:
                if properties:
                    relationship.connect(to_node, properties)
                else:
                    relationship.connect(to_node)
                return True
            return False
        except Exception as e:
            print(f"Error creating relationship: {e}")
            return False