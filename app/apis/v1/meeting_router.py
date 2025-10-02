from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.services.meeting_service_mysql import service_create_meeting_mysql

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 DB 를 쓰는지 URL 에 적을 필요 없습니다!
# 강의에서만 이렇게 합니다!
# 실전에서는 db 이름을 url 에 넣지 마세요


@mysql_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)
