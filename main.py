from copy import copy
import sys
import random
from typing import Any, Iterator, SupportsIndex
from colorama import init, Fore, Back, Style
import time
import os


class Debuger():
    def __init__(self) -> None:
        os.system('cls')
        self._line_ = -1
        self._file_ = None
    
    @property
    def _time_(self):
        _time = time.localtime(time.perf_counter())
        return f'{Fore.CYAN}[ {_time[3]}:{_time[4]}:{_time[5]} ]{Fore.RESET}'
        
    @property
    def _debug_(self):
        return f'{Fore.BLACK}[ DEBUG ]{Fore.RESET}{self._stroke_line_}'
    
    @property
    def _win_(self):
        return f'{Fore.MAGENTA}[ WINDOW ]{Fore.RESET}'
    
    @property
    def _list_(self):
        return f'{Fore.LIGHTYELLOW_EX}[ LIST ]{Fore.RESET}'
    
    @property
    def _list_converting_(self):
        return f'{Fore.YELLOW}[ CONVERTING ]{Fore.RESET}'
    
    @property
    def _list_mutation_(self):
        return f'{Fore.YELLOW}[ MUTATION ]{Fore.RESET}'
    
    @property
    def _list_mutation_copy_(self):
        return f'{Fore.YELLOW}[ COPY ]{Fore.RESET}'
    
    @property
    def _list_mutation_concat_(self):
        return f'{Fore.YELLOW}[ CONCATINATION ]{Fore.RESET}'
    
    @property
    def _list_mutation_dellete_(self):
        return f'{Fore.YELLOW}[ DELLETE ]{Fore.RESET}'
    
    @property
    def _list_mutation_sort_(self):
        return f'{Fore.YELLOW}[ SORT ]{Fore.RESET}'
    
    @property
    def _list_id_(self):
        return f'{Fore.LIGHTMAGENTA_EX}[ ID ]{Fore.RESET}'
    
    @property
    def _stroke_line_(self):
        if self._file_!='GL':
            stroke = self._line_
        else:
            stroke = str(self._line_) + self._not_exactly_
        
        return f'{Fore.WHITE}{Style.BRIGHT}[ stroke:{stroke} {Style.BRIGHT}{Fore.WHITE}file:{self._file_}.py ]{Fore.RESET}{Style.RESET_ALL}'
    
    @property
    def _error_(self):
        return f'{Fore.RED}[ ERROR ]{Fore.RESET}'
    
    @property
    def _not_exactly_(self):
        return f'{Fore.YELLOW}{Style.DIM}(NOT_EXACTLY){Style.RESET_ALL}{Fore.RESET}'
    
    @property
    def _setter_(self):
        return f'{Fore.LIGHTMAGENTA_EX}[ SETTER ]{Fore.RESET}'
    
    @property
    def _getter_(self):
        return f'{Fore.LIGHTMAGENTA_EX}[ GETTER ]{Fore.RESET}'
    
    @property
    def _counter_(self):
        return f'{Fore.LIGHTCYAN_EX}[ COUNTER ]{Fore.RESET}'

    
    
    
    
    @property
    def SUCCSES(self):
        return f'{self._time_}{self._debug_}{Fore.GREEN} Succes!{Fore.RESET}'
    
    # todo WIN_INIT ------------
    @property
    def WIN_SYS_INIT_START(self):
        return f'{self._time_}{self._debug_}{self._win_} Start init...'
    
    @property
    def WIN_SYS_VIDEO_DRIVER_INIT(self):
        return f'{self._time_}{self._debug_}{self._win_} Video driver init..'
    
    @property
    def WIN_SYS_ATTRS_INIT(self):
        return f'{self._time_}{self._debug_}{self._win_} Atributes setup..'
    
    def WIN_SYS_ERROR(self, log: str):
        return f'{self._time_}{self._debug_}{self._win_}{self._error_}{log}'
    # todo WIN_INIT -------------

    # todo LIST_INIT -------------
    def LIST_MODULES_INIT(self, id: Any):
        return f'{self._time_}{self._debug_}{self._list_} List {Fore.BLACK}[id:{id}]{Fore.RESET} init...'
    
    def LIST_ERROR(self, log: str):
        return f'{self._time_}{self._debug_}{self._list_}{self._error_}{log}'
    
    def LIST_CONVERTING(self,object: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_converting_}{Fore.BLACK}[ Object: {object} Type: {type(object)} ]{Fore.RESET} Object start converting...'
        
    def LIST_ADD(self, id: Any, object: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_} List {Fore.BLACK}[id:{id}]{Fore.RESET} add {Fore.BLACK}[ Object: {object} Type: {type(object)} ]{Fore.RESET}'
        
    def LIST_CLEAR(self, id: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_} List {Fore.BLACK}[id:{id}]{Fore.RESET} cleared'
    
    def LIST_POP(self, id: Any, Index: int, list):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_} List {Fore.BLACK}[id:{id}]{Fore.RESET} delete {Fore.BLACK}[ index: {Index} object: {list[Index]} ]{Fore.RESET} element.'
    
    @property
    def LIST_ID_GENERATE(self):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_id_} Generate id started...'
    
    def LIST_ID_GENERATE_FINISH(self, id: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_id_} Id {Fore.BLACK}[{id}]{Fore.RESET} generated!'
    
    def LIST_SET_ID(self, list: 'List', id: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_id_}{self._setter_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} set new {Fore.BLACK}[id:{id}]{Fore.RESET}'
    
    def LIST_SET_ID_ERROR(self, list: 'list', id: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_id_}{self._setter_}{self._error_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} dont set new {Fore.BLACK}[id:{id} type:{type(id)}]{Fore.RESET} '
    
    def LIST_COPY(self, list: 'List' ,id: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_}{self._list_mutation_copy_} List {Fore.BLACK}[id:{list.id} data:{list._list}]{Fore.RESET} copy new list {Fore.BLACK}[id:{id}]{Fore.RESET} '
    
    def LIST_COUNTER_INIT(self, list: 'List'):
        return f'{self._time_}{self._debug_}{self._list_}{self._counter_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} counter start init...'
    
    def LIST_COUNTER(self, list: 'List', count: int, object: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._counter_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} using counter {Fore.BLACK}[object:{object} count:{count}]{Fore.RESET}'
    
    def LIST_CONCAT(self, my_list: 'List', list: 'List'):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_}{self._list_mutation_concat_} List {Fore.BLACK}[id:{my_list.id}]{Fore.RESET} concat list {Fore.BLACK}[id:{list.id}]{Fore.RESET}'
    
    def LIST_CONCAT_NEW(self, my_list: 'List', list: 'List', new_list: 'List'):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_}{self._list_mutation_concat_} List {Fore.BLACK}[id:{my_list.id}]{Fore.RESET} concat list {Fore.BLACK}[id:{list.id}]{Fore.RESET} to new list {Fore.BLACK}[id:{new_list.id}]{Fore.RESET}'
    
    def LIST_INDEX(self, list: 'List', index: int, object: Any):
        return f'{self._time_}{self._debug_}{self._list_}{self._getter_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} getter use {Fore.BLACK}[object:{object} index:{index}]{Fore.RESET}'
    
    def LIST_DELETE(self, list: 'List', index: int):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_}{self._list_mutation_dellete_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} dellete [object:{list[index]} index:{index}]'
    
    def LIST_DELETE_ERROR(self, list: 'List', index: int):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_}{self._list_mutation_dellete_}{self._error_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} dellete index:{index} not found!'
    
    def LIST_SORT(self, list: 'List', key: Any, reversed: bool):
        return f'{self._time_}{self._debug_}{self._list_}{self._list_mutation_}{self._list_mutation_sort_} List {Fore.BLACK}[id:{list.id}]{Fore.RESET} sort by {Fore.BLACK}[key:{key} reversed:{reversed}]{Fore.RESET}'
    
    # todo LIST_INIT -------------
_deb_ = Debuger()
class List():
    ONE_ELEMENT = 'one'
    MANY_ELEMENT = 'many'
    
    @classmethod
    @property
    def rand_id(self) -> int:
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_ID_GENERATE)
        id = random.randint(0,9999999999999)
        print(_deb_.LIST_ID_GENERATE_FINISH(id))
        print(_deb_.SUCCSES)
        return id
    
    @property
    def id(self) -> int | str:
        return self.__id
        
    
    @classmethod
    def my_id(self, __id: int | str) -> int | str:
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_ID_GENERATE)
        id = __id
        print(_deb_.LIST_ID_GENERATE_FINISH(id))
        print(_deb_.SUCCSES)
        return id
    
    @classmethod
    def convert(self, iterable_: list | str | tuple) -> 'List':
        __list = []
        _deb_._line_ = sys._getframe(1).f_lineno
        try:
            print(_deb_.LIST_CONVERTING(iterable_))
            for _preduct in iterable_:
                try:
                    _element = iterable_[_preduct]
                    __list.append([_preduct, _element])
                except:
                    __list.append(_preduct)
        except:...
        return List(__list)
                   
    def __init__(self, iterable_: list = []) -> None:
        """Класс подобный ванильному классу list, но предоставляющий больший функционал.
        
        Args:
            iterable_ (list, optional): Список любых элеиентов. Изначально равен [].
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        _deb_._file_ = str(sys._getframe(1)).split(',')[1].split(r'\\')[-1].split('.')[0]
        self.__id = random.randint(0,9999999999999)
        print(_deb_.LIST_MODULES_INIT(self.__id))
        try:
            self._list = list(iterable_)
            print(_deb_.SUCCSES)
        except:
            print(_deb_.LIST_ERROR(f'List {self.__id}, is not init!'))
            sys.exit(0)
            
    def set_id(cls, __id) -> 'List':
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_SET_ID(cls, __id))
        if isinstance(__id, (int, str)):
            cls.__id = __id
            print(_deb_.SUCCSES)
        else:
            print(_deb_.LIST_SET_ID_ERROR(cls, __id))
        return cls
    
    def add(self, __object: Any) -> None:
        """Добавляет объект в конец массива.
        Args:
            __object (Any): любой объект
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        self._list.append(__object)
        print(_deb_.LIST_ADD(self.__id, __object))
        
    def __List_in_list__(self) -> bool:
        for elem in self._list:
            if isinstance(elem, List):
                return True
        return False
    
    def __str__(self) -> str:
        stroke = ''
        if self.__List_in_list__():
            for elem in self._list:
                if isinstance(elem, List):
                    stroke+=str( elem(full=True) )+'\n'
                else:
                    stroke+=str( elem )+'\n'
            return f'{stroke}'
        else:
            return f'{self._list}'
    
    def __len__(self) -> int:
        return len(self._list)
    
    def clear(self) -> None:
        """Очищает массив."""
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_CLEAR(self.__id))
        self._list.clear()
        
    def pop(self, __index: int) -> None:
        """Удаляет выбранный элемент из массива.
        Args:
            __index (int): индекс удаляемого элемента.
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_POP(self.__id, __index, self))
        del self._list[__index]
        
    def to_pop(self, __index: int) -> 'List':
        """Удаляет выбранный элемент из массива и возвращает новый массив.
        Args:
            __index (int): индекс удаляемого элемента.
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_POP(self.__id, __index, self))
        new_list = copy(self._list)
        del new_list[__index]
        return List(new_list)
        
    def copy(self) -> 'List':
        """Создает точную коппию массива

        Returns:
            List: Новый массив
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        new_list = List( copy( self._list ) )
        print(_deb_.LIST_COPY(self, new_list.id))
        return new_list
    
    def count(self, __element: Any) -> int:
        """Счетает количество выбранных элементов в массиве.

        Args:
            __element (Any): Любой объект.

        Returns:
            int: Количество объектов.
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_COUNTER_INIT(self))
        __count = 0
        print(_deb_.SUCCSES)
        for element in self._list:
            if element == __element: __count+=1
        print(_deb_.LIST_COUNTER(self, __count, __element))
        return __count
    
    def concat(cls, __iterable: 'List') -> None:
        """Склеивает к данному массиву другой массив.

        Args:
            __iterable (List): Массив.
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        for __index in range(len(__iterable)):
            cls._list.append(__iterable(__index))
        print(_deb_.LIST_CONCAT(cls, __iterable))
        return cls
            
    def to_concat(self, __iterable: 'List') -> 'List':
        """Склеивает к данному массиву другой массив и возращает коппию нового массива.

        Args:
            __iterable (List): _description_

        Returns:
            List: Массив
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        new_list = copy(self._list)
        for __index in range(len(__iterable)):
            new_list.append(__iterable(__index))
        
        new_list = List( new_list )
        print(_deb_.LIST_CONCAT_NEW(self, __iterable,  new_list))
        return new_list
    
    def index(self, __value: Any, reverse: bool = False) -> int:
        """Возвращает индекс первого вхождения данного элемента в список.

        Args:
            __value (Any): Значение (объект).
            reverse (bool, optional): Будет ли начинаться поиск с конца. Defaults to False.

        Returns:
            int: индекс вхождения.
        """
        _deb_._line_ = sys._getframe(1).f_lineno
        for __index in range( len( self._list ) ):
            if reverse:
                __index = len(self._list)-1-__index
            if self._list[__index] == __value:
                print(_deb_.LIST_INDEX(self, __index, __value))
                return __index
        print(_deb_.LIST_INDEX(self, _deb_._error_, __value))
        return -1
    
    def __delitem__(self, __key: SupportsIndex | slice) -> None:
        _deb_._line_ = sys._getframe(1).f_lineno
        try:
            print(_deb_.LIST_DELETE(self,__key))
            self._list.__delitem__(__key)
        except:
            print(_deb_.LIST_DELETE_ERROR(self,__key))
        
    def sort(cls, key=None, reverse: bool = False):
        """Сортирует массив по ключу.

        Args:
            key (_type_, optional): Ключ необходимый для сортировки массива. Defaults to None.
            reverse (bool, optional): Будет перевернут отсортированный список. Defaults to False.

        """
        cls._list.sort(key=key, reverse=reverse)
        
        _deb_._line_ = sys._getframe(1).f_lineno
        print(_deb_.LIST_SORT(cls, key, reverse))
        return cls
        
    def to_sort(self, key=None, reverse: bool = False) -> 'List':
        """Сортирует массив по ключу и возвращает отсортированный массив.

        Args:
            key (_type_, optional): Ключ необходимый для сортировки массива. Defaults to None.
            reverse (bool, optional): Будет перевернут отсортированный список. Defaults to False.

        Returns:
            List: Новый Массив
        """
        new_list = copy( self._list )
        new_list.sort(key=key, reverse=reverse)
        print(_deb_.LIST_SORT(self, key, reverse))
        return List( new_list )
    
    def reverse(cls) -> None:
        """Переворачивает массив.
        """
        cls._list.reverse()
        return cls
        
    def to_reverse(self) -> 'List':
        """Переворачивает массив и возвращает новый массив.

        Returns:
            List: Новый массив.
        """
        new_list = copy(self._list)
        new_list.reverse()
        return List( new_list )
    
    def __iter__(self) -> Iterator:
        return self._list.__iter__()
    
    def __instancecheck__(self, __instance: Any) -> bool:
        return self._list.__instancecheck__(__instance)
    
    def __reversed__(self) -> Iterator:
        return self._list.__reversed__()
    
    def __call__(self, _start: int = None, _stop: int or None = None, full = False) -> Any:
        if full:
            return self._list
        if _stop == None:
            return self._list[_start]
        else:
            return List(self._list[_start: _stop+1])
    
    def generate(cls, count: int = 10, start: int = 0, stop: int = 10 ):
        """Генерирует массив из чисел по заданным параметрам.

        Args:
            count (int, optional): Количество генерируемых чисел. Defaults to 10.
            start (int, optional): Начальное значение. Defaults to 0.
            stop (int, optional): Конечное значение. Defaults to 10.

        Returns:
            cls: Возвращает себя.
        """
        for i in range(count):
            cls._list.append(random.randint(start, stop+1))
        return cls
    
    def sum(self, __index: int or None = None) -> int:
        """Находит сумму всех элементов массива соответствующих данному индексу поиска.

        Args:
            __index (int or None, optional): Индекс поиска. Defaults to None.

        Returns:
            int: Сумма.
        """
        if __index == None:
            return sum(self._list)
        else:
            return sum( [elem(__index) for elem in self._list] )
        
    def map(self, __method: Any) -> None:
        """Использует данный метод к каждому элементу массива.

        Args:
            __method (Any): lambda метод.
        """
        self._list = list( map(__method, self._list) )
        
    def to_map(self, __method: Any) -> 'List':
        """Использует данный метод к каждому элементу массива и возвращает новый массив.

        Args:
            __method (Any): lambda метод.

        Returns:
            List: Новый массив.
        """
        new_list = copy(self._list)
        new_list = list( map(__method, new_list) )
        return List( new_list )
        
    def to_list(cls, __value: Any, __flags: None = None) -> None:
        """Превращает строку или число в массив.
        Args:
            __value (Any): Значение.
            __flags (None, optional): Флаг превращения. Defaults to None.

        Returns:
            cls: Возвращает себя.
        """
        if isinstance(__value, int) and __flags == cls.ONE_ELEMENT:
            cls._list = list([__value])
        elif isinstance(__value, int) and __flags == cls.MANY_ELEMENT:
            cls._list = list( map(lambda elem: int(elem) , list(str(__value)) ) )
        elif isinstance(__value, str) and __flags == cls.ONE_ELEMENT:
            cls._list = list([int(__value)])
        elif isinstance(__value, str) and __flags == cls.MANY_ELEMENT:
            cls._list = list(__value)
        return cls
    
    def to_dict(cls, __iter_object: dict) -> 'List':
        for key in __iter_object:
            cls._list.append((key, __iter_object[key])) 
        return cls
    
    def filter(self, __method: Any):
        self._list = list(filter(__method, self._list))
        
    def to_filter(self, __method: Any):
        new_list = copy(self._list)
        new_list = list(filter(__method, new_list))
        return List( new_list )
    
    def includes(self, __object: object):
        return __object in self._list
    
    def find(self, __method: Any):
        for elem in self._list:
            if list(map(__method, [elem]))[0]:
                return elem
    
    def find_index(self, __method: Any):
        for index, elem in enumerate( self._list ):
            if list(map(__method,[elem]))[0]:
                return index
    
    def some(self, __method: Any):
        for elem in self._list:
            if list(map(__method,[elem]))[0]:
                return True
        return False
    
    def every(self, __method: Any):
        __ever = 0
        for elem in self._list :
            if list(map(__method,[elem]))[0]:
                __ever += 1
            
        return __ever == len(self._list)
    
    def __eq__(self, List: 'List') -> bool:
        return self._list == List._list
    
    def __ne__(self, List: 'List') -> bool:
        return self._list != List._list
    
    def __getitem__(self, __key: SupportsIndex | slice) -> Any:
        return self._list.__getitem__(__key)
    
    def __setitem__(self, __key: SupportsIndex | slice, __value: Any) -> None:
        self._list.__setitem__(__key, __value)
         
    def range(self, _reverse: bool = False):
        for ind, elem in enumerate( self._list):
            if _reverse: ind = len(self._list) - ind - 1
            _prod = self._list[ind]
            yield (_prod, ind)
