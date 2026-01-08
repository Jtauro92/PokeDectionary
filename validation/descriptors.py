from validation.validators import (
    validate_name, validate_number, set_type, set_ability, ValidatedProperty
)
from pokedex.stats import Stats

class StatsDescriptor:
    """Descriptor to handle Stats assignment and conversion."""
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

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
    def __init__(self):
        super().__init__()

    def __set__(self, instance, value):
        if self.private_name == "_name":
            # Define a temporary setter to apply the @validate_name decorator
            @validate_name
            def validated_setter(inst, val):   
                setattr(inst, self.private_name, val)
            
            # Execute the decorated setter with the provided value
            validated_setter(instance, value)

        elif self.private_name == "_number":
            # Define a temporary setter to apply the @validate_number decorator
            @validate_number
            def validated_setter(inst, val):
                setattr(inst, self.private_name, val)
            
            # Execute the decorated setter with the provided value
            validated_setter(instance, value)

        elif self.private_name == "_type1":
            # Define a temporary setter to apply the @set_type decorator
            @set_type
            def validated_setter(inst, val):
                setattr(inst, self.private_name, val)
            
            # Execute the decorated setter with the provided value
            validated_setter(instance, value)

        elif self.private_name == "_type2":
            # Define a temporary setter to apply the @set_type decorator
            @set_type
            def validated_setter(inst, val):
                if not inst.type1 and val:
                    inst.type1 = val
                else:
                    setattr(inst, self.private_name, val)
            
            # Execute the decorated setter with the provided value
            validated_setter(instance, value)

        elif self.private_name in ("_ability1", "_ability2", "_hidden_ability"):
            # Define a temporary setter to apply the @set_ability decorator
            @set_ability
            def validated_setter(inst, val):
                setattr(inst, self.private_name, val)
            
            # Execute the decorated setter with the provided value
            validated_setter(instance, value)

        else:
            setattr(instance, self.private_name, value)
