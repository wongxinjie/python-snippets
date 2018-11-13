# encoding: utf-8
import yaml
from apispec import APISpec

spec = APISpec(
    title='Gisty',
    version='1.0.0',
    info=dict(
        description='一个简单的gist demo api'
    )
)

spec.definition('Gist', properties={
    "id": {"type": "integer", "format": "int64"},
    "name": {"type": "string"}
})

spec.add_path(
    path="/gist/{gist_id}",
    operations=dict(
        get=dict(
            responses={
                "200": {
                    "schema": {"$ref": "#/definations/Gist"}
                }
            }
        )
    )
)


print(spec.to_dict())
docs = yaml.dump(spec.to_dict())
print(docs)
