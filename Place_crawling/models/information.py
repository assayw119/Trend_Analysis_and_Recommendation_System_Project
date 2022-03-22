from odmantic import Model


class Information(Model):
    name: str
    sort = str
    mood: list
    menu: str
    mean_price: int
    point: int
    reviews: int

    class Config:
        collection = "restaurant_inform"
