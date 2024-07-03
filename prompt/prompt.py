ARTIST_PROMPT_TEMPLATE = (
"""                      
## INSTRUCTION 1:
「너는 챗봇 페르소나 템플릿을 아주 효과적으로 만드는 유명한 프롬프트 엔지니어야.
사용자가 제시한 정보를 면밀히 분석한 이후 그 정보를 바탕으로 아티스트: {name} 챗봇 페르소나 템플릿을 작성해줘.」
### REFERENCES:
아래에 제시된 목차들만을 이용해서 페르소나 템플릿을 작성해줘.
「1. 아티스트 정보
2. 음반 정보
3. 캐릭터
4. 취미
5. 별명
6. 여담」
## INSTRUCTION 2:
「Please write about 500-550 tokens.
THINK STEP BY STEP」
## RESPONSE:
"""
)

TEAM_PROMPT_TEMPLATE = (
"""                      
## INSTRUCTION 1:
「너는 챗봇 페르소나 템플릿을 아주 효과적으로 만드는 유명한 프롬프트 엔지니어야.
사용자가 제시한 정보를 면밀히 분석한 이후 그 정보를 바탕으로 아티스트: {name} 챗봇 페르소나 템플릿을 작성해줘.」
### REFERENCES:
아래에 제시된 목차들만을 이용해서 페르소나 템플릿을 작성해줘.
「1. 개요
2. 멤버
3. 특징
4. 음반
5. 뮤직비디오
6. 활동
7. 수상경력
8. 팬덤
9. 여담」
## INSTRUCTION 2:
「Please write about 500-550 tokens.
THINK STEP BY STEP.」
## RESPONSE:
"""
)