"""
Module for managing the statistics of a Pokemon.

This module defines the Stats class and the Stat descriptor, which handles
validation and storage of individual stat values (HP, Attack, Defense, etc.).
"""
from typing import Any, Iterator, Union
from validation import set_stat


class Stat:
    """
    Descriptor for a Pokemon stat with built-in validation.

    This descriptor manages the access and assignment of stat values, ensuring
    that all assignments pass through the `set_stat` validation decorator.
    """

    def __set_name__(self, owner: Any, name: str) -> None:
        """
        Assign the private attribute name and pre-compile the validated setter.

        Args:
            owner: The class owning the descriptor.
            name: The name of the attribute in the owner class.
        """
        self.private_name = f"_{name}"

        # Pre-compile the setter with validation to avoid overhead in __set__
        # This ensures validation logic is attached once per attribute definition
        @set_stat
        def setter(instance: Any, value: int) -> None:
            '''
            Set the stat value on the instance after validation.
            
            Args:
                instance: The instance of the owner class.
                value: The value to assign to the stat.
            '''
            setattr(instance, self.private_name, value)
        
        self._setter = setter

    def __get__(self, instance: Any, owner: Any) -> Union[int, 'Stat', None]:
        """
        Retrieve the stat value from the instance.

        Args:
            instance: The instance of the owner class.
            owner: The owner class itself.

        Returns:
            The integer value of the stat, or the descriptor itself if accessed via the class.
        """
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance: Any, value: int) -> None:
        """
        Set the stat value on the instance using the validated setter.

        Args:
            instance: The instance of the owner class.
            value: The value to assign to the stat.
        """
        self._setter(instance, value)


class Stats:
    """
    Class representing the collection of stats for a Pokemon.

    Attributes:
        hp (int): Hit Points.
        atk (int): Attack stat.
        defn (int): Defense stat.
        spatk (int): Special Attack stat.
        spdef (int): Special Defense stat.
        speed (int): Speed stat.
    """

    __slots__ = ('_hp', '_atk', '_defn', '_spatk', '_spdef', '_speed')

    # Create descriptors for each stat
    hp, atk, defn, spatk, spdef, speed = (Stat() for _ in range(6))

    def __init__(
        self, 
        hp: int | None = None, 
        atk: int | None = None, 
        defn: int | None = None, 
        spatk: int | None = None, 
        spdef: int | None = None, 
        speed: int | None = None
    ) -> None:
        """
        Initialize the Stats object.

        We assign to public attributes (self.hp) to ensure the @set_stat validation
        runs immediately upon object creation.
        """
        # Triggers Stat.__set__ for validation
        self.hp, self.atk, self.defn = hp, atk, defn
        self.spatk, self.spdef, self.speed = spatk, spdef, speed

    def __iter__(self) -> Iterator[int | None]:
        """
        Iterate over the stat values.

        Yields:
            The value of each stat in the order: HP, ATK, DEF, SP.ATK, SP.DEF, SPEED.
        """
        yield from (getattr(self, attr) for attr in self.__slots__)




