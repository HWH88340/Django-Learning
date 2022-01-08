from django.db import models
import re
from django.core.exceptions import ValidationError
# Create your models here.


class Hand:
    def __init__(self, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def parse_hand(hand_tring):
    """104长度的字符串，分解为4个玩家的手牌"""
    p1 = re.compile('.{26}')  # 每26个字符分割一下，每个单位就是一个玩家的手牌
    p2 = re.compile('..')  # 每2个字符分割一下，每个单位就是一张牌
    args = [p2.findall(x) for x in p1.findall(hand_tring)]
    if len(args) != 4:
        raise ValidationError('非法的手牌存档，格式不正确，无法解析！')
    return Hand(*args)


class HandField(models.Field):
    description = '一手桥牌'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    # 决定数据在数据库种以什么类型保存
    def db_type(self, connection):
        return 'char'

    # 如何将数据库种的数据转换为Python的对象
    def to_python(self, value):
        if isinstance(value, Hand):
            return value

        if value is None:
            return value

        return parse_hand(value)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return parse_hand(value)

    def get_prep_value(self, value):
        # value就是一个Hand的实例
        return ''.join([''.join(l) for l in (
            value.north, value.east, value.south, value.west)])

class HandModel(models.Model):
    hand = HandField()