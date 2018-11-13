import json

from apispec import APISpec
from marshmallow import Schema, fields
from tornado.web import RequestHandler

spec = APISpec(
    title='Gist',
    version='1.0.0',
    info=dict(
        description='一个简单的gist demo api'
    ),
    basePath="/v1.0",
    tags=[
        {"name": "user", "description": "获取用户信息"}
    ],
    plugins=[
        "apispec.ext.tornado",
        "apispec.ext.marshmallow"
    ]
)

spec.definition("http400", properties={
    "status_code": {"type": "integer", "default": 400},
    "message": {"type": "string"},
    "errors": {"type": "array", "$ref": "#definitions/error"},
})

spec.definition("error", properties={
    "field": {"type": "array", "description": "出错列"},
})


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(description="用户姓名")


class UserListSchema(Schema):
    current_page = fields.Int(required=True)
    total_page = fields.Int()
    page_size = fields.Int()
    total_items = fields.Int()
    users = fields.Nested(UserSchema, many=True)


# spec.definition("user", schema=UserSchema)
spec.definition("user-list", schema=UserListSchema)


class UserHandler(RequestHandler):

    def get(self):
        """获取用户信息
        ---
        description: 获取用户信息
        tags:
            - user
        parameters:
        - name: "userid"
          in: "path"
          description: "用户id"
          required: true
          type: "integer"
        responses:
            200:
                description: 获取用信息成功
                schema:
                    $ref: '#definitions/user-list'
            400:
                description: Bad request
                schema:
                    $ref: '#definitions/http400'
        """
        self.write("User")


urlspec = (r'/hello/{userid}', UserHandler)
spec.add_path(urlspec=urlspec)
print(json.dumps(spec.to_dict(), ensure_ascii=False))
