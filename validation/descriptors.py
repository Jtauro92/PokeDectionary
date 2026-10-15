from validation.validators import (
    validate_name, validate_number, set_type, set_ability
)
from pokedex.stats import Stats

class StatsDescriptor:
    """Descriptor to handle Stats assignment and conversion."""

    # This method is called when the descriptor is assigned to a class attribute.
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    # This method is called when the attribute is accessed. It retrieves the value from the instance's __dict__ using the private name.
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        # Automatically convert tuples/lists to Stats object
        if not isinstance(value, Stats):
            value = Stats(*value)
        setattr(instance, self.private_name, value)

class AttrDescriptor(StatsDescriptor):
    '''Descriptor to handle attribute assignment with validation.'''
    def __init__(self):
        super().__init__()

    def __set__(self, instance, value):
        '''Apply validation to the assigned value.'''
        if self.private_name == "_name": #Set the private name for the attribute
            @validate_name # Apply the name validation decorator
            def validated_setter(inst, val):
                '''Set the validated value to the instance's private attribute.
                   Args:
                    inst: The instance to set the attribute on.
                    val: The value to set.
                '''
                setattr(inst, self.private_name, val) # Set the validated value to the instance's private attribute
            validated_setter(instance, value) # Call the validated setter with the instance and value

        elif self.private_name == "_number":  # set the private name for the attribute
            @validate_number
            def validated_setter(inst, val):
                setattr(inst, self.private_name, val)
            validated_setter(instance, value)

        elif self.private_name == "_type1":   # Changed to elif
            @set_type
            def validated_setter(inst, val):
                setattr(inst, self.private_name, val)
            validated_setter(instance, value)

        elif self.private_name == "_type2":   # Changed to elif
            @set_type
            def validated_setter(inst, val):
                if not inst.type1 and val:
                    inst.type1 = val
                else:
                    setattr(inst, self.private_name, val)
            validated_setter(instance, value)

        elif self.private_name in ("_ability1", "_ability2", "_hidden_ability"): # Changed to elif
            @set_ability
            def validated_setter(inst, val):
                setattr(inst, self.private_name, val)
            validated_setter(instance, value)

        else:
            # Now this only runs if NO validation was needed
            setattr(instance, self.private_name, value)
