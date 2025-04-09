from abc import ABC, abstractmethod

import math

class Publication(ABC):
    def __init__(self, name, author):
        self.__name_publication = name
        self.__author = author
    
    @abstractmethod
    def display(self) -> None: pass

    def find(self, criterion: dict) -> bool:
        is_check = False
    
        for key, value in criterion.items():
            class_name = self.__class__.__name__
            private_field_name = f"_{class_name}__{key}"
            if not hasattr(self, private_field_name):
                private_field_name = f"_Publication__{key}"

            if(hasattr(self, private_field_name)):
                print(private_field_name)
                attr_value = getattr(self, private_field_name)
                if(attr_value == value):
                    is_check = True
        return is_check
    

    def get_name_publication(self) -> str:
        return self.__name_publication

    def get_author(self) -> str:
        return self.__author


class Book(Publication):
    def __init__(self, name, author, year,publishing_name):
        super().__init__(name, author)
        self.__year_publication = year
        self.__publishing = publishing_name

    def display(self):
        print(f"Publication: {self.get_name_publication()}, Author : {self.get_author()} \nYear publication: {self.__year_publication} \nPublishing: {self.__publishing} \n") 


class ElectronicSource(Publication):
    def __init__(self, name, author, URL, annotation):
        super().__init__(name, author)
        self.__URL = URL
        self.__annotation = annotation

    def display(self):
        print(f"Publication: {self.get_name_publication()}, Author : {self.get_author()}\nURL: {self.__URL} \nAnnotation: {self.__annotation} \n") 


class Article(Publication):
    def __init__(self, name, author, number, year):
        super().__init__(name, author)
        self.__number = number
        self.__year_publication = year

    def display(self):
        print(f"Publication: {self.get_name_publication()}, Author : {self.get_author()} \nNumber publication: {self.__number},\nYear Publishing: {self.__year_publication} \n") 
    


class Catalog:
    def __init__(self):
        self.__list_publications : list[Publication] = list[Publication]()

    def print_publications(self):
        for publ in self.__list_publications:
            publ.display()
    
    def add_all_publication(self, list_publication: list[Publication]):
        self.__list_publications.extend(list_publication)

    def add_publication(self, publication: Publication):
        self.__list_publications.append(publication)

    def find_to_author(self, author) -> list[Publication]:
        temp_list = []
        for p in self.__list_publications:
            if p.find({"author": author}):
                temp_list.append(p)
        return temp_list


def main():
    catalog = Catalog()
    list_publication = [
        Article("One_Publisher", "Author_One", 1, 2014),
        Book("Two_Publish", "Author_Two", 2018, "Publish_Name_One"),
        ElectronicSource("Three_Publish", "Author_Two", "https://home/go", "Annotation_Three")
    ]

    catalog.add_all_publication(list_publication)
    # catalog.print_publications()

    author_publication = catalog.find_to_author("Author_Two")
    if author_publication:
        for p in author_publication:
            p.display()


if __name__ == "__main__":
    main()
