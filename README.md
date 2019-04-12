# Mangoplate-Crawling
망고플레이트 서울시 인기 맛집 목록 크롤링 <br>

1. 망고플레이트에서 인기 해쉬태그 수집<br>
https://www.mangoplate.com/top_lists <br>
위의 웹 사이트(망고플레이트)에서 인기 해쉬태그를 수집<br>

2. 셀레니움으로 해쉬태그 자동 클릭(+더보기 버튼 클릭) <br>
해쉬태그 클릭 후 해당 해쉬태그에 있는 URL 모두 수집 <br>

3. 수집한 URL 속 맛집들 URL 수집<br>

4. 수집한 URL 속 맛집 정보 파싱<br>
파이썬 BeautifulSoup을 사용하여 맛집 정보 파싱 후 데이터베이스에  
