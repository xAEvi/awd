from marshmallow import Schema, fields

class CreateUserRequest(Schema):
    nombre = fields.String(required=True)
    correo_electronico = fields.String(required=True) #Cambiado a Email para validación
    contraseña = fields.String(required=True)
    rol = fields.String(required=True) #Añadido campo rol con validación