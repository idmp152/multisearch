from fastapi.routing import APIRouter

from models import QueryResponse  # type: ignore
from requesters import REQUESTERS, AvailableSearchEngines  # type: ignore

api_router = APIRouter()


def request_all_engines(query: str) -> list[QueryResponse]:
    """Requests all available search engines."""
    response_list = []
    for requester in REQUESTERS.values():
        response_list.extend(requester.request_query(query))
    return response_list


@api_router.get("/api/search", response_model=list[QueryResponse])
async def get_results(
    query: str, search_engine: AvailableSearchEngines = None
) -> list[QueryResponse]:
    """Gets a list of results by a search query."""
    if not search_engine:
        return request_all_engines(query)
    return REQUESTERS[search_engine].request_query(query)
