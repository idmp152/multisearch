from enum import Enum
import abc
import random

from frozendict import frozendict # type: ignore

from models import QueryResponse # type: ignore

class AvailableSearchEngines(str, Enum):
    """Available search engines enum."""
    GOOGLE = "google"
    YANDEX = "yandex"

class IRequester(abc.ABC):
    """Requester interface"""
    @staticmethod
    @abc.abstractmethod
    def request_query(query: str) -> list[QueryResponse]:
        """Main requester method"""


class GoogleRequester(IRequester):
    """Google requester implementation"""
    @staticmethod
    def request_query(query: str) -> list[QueryResponse]:
        responses = []
        for _ in range(random.randint(0, 10)):
            response = QueryResponse(
                title="This is a Google response",
                description=f"Lorem {query} dolor sit amet",
                url="https://www.google.com/",
                engine=AvailableSearchEngines.GOOGLE
            )
            responses.append(response)
        return responses

class YandexRequester(IRequester):
    """Yandex requester implementation"""
    @staticmethod
    def request_query(query: str) -> list[QueryResponse]:
        responses = []
        for _ in range(random.randint(0, 10)):
            response = QueryResponse(
                title="This is a Yandex response",
                description=f"Lorem {query} dolor sit amet",
                url="https://www.yandex.ru/",
                engine=AvailableSearchEngines.YANDEX
            )
            responses.append(response)
        return responses

REQUESTERS: frozendict[AvailableSearchEngines, IRequester] = frozendict({
    AvailableSearchEngines.GOOGLE: GoogleRequester,
    AvailableSearchEngines.YANDEX: YandexRequester
})
