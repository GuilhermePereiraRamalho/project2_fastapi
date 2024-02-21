from pydantic import BaseModel

class CustomBaseModel(BaseModel):
    def dict(self, *args, **kargs):
        d = super().dict(*args, **kargs)
        d = {k: v for k, v in d.items() if v is not None}
        return d