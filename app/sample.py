import string
from turtle import st
from typing import Awaitable, Callable, NewType, NoReturn, Protocol, TypeVar


# 型エイリアス
Vector = list[str]

Name = str

# NewType (= サブクラス)
UserId = NewType("UserId", int)


def get_user_name(userId: UserId) -> NoReturn:
    pass


T = TypeVar("T")

AsyncFun = Callable[[UserId], Awaitable[None] | None]

callableFun: AsyncFun = get_user_name


class BaseProto(Protocol):
    def hello(self, name: str) -> str:
        return f"Hello! ${name}"


class ChildProto:
    def hello(self, address: str) -> str:
        return f"I live in ${address}."


def protoFunc(f: BaseProto, str_arg: str) -> str:
    return f.hello(str_arg)


protoFunc(ChildProto())
