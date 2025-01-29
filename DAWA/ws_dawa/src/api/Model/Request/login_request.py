from marshmallow import Schema, fields

class LoginRequest(Schema):
    correo_electronico= fields.String(required=True)
    contraseña = fields.String(reqyured=True)