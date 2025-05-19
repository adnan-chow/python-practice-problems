from jsonschema import validate, ValidationError

def validate_json(json_data):
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer", "minimum": 0}
        },
        "required": ["name", "age"]
    }
    try:
        validate(instance=json_data, schema=schema)
        return True
    except ValidationError:
        return False

# Test the function
json_data = {"name": "John", "age": 30}
print(validate_json(json_data))