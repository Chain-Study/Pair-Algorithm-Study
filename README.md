# Pair-Algorithm-Study
페어로 진행하는 알고리즘 스터디

## 🏷️ 목차

- [Pair-Algorithm-Study](#pair-algorithm-study)
  - [🏷️ 목차](#️-목차)
  - [📕 문제 보관함](#-문제-보관함)
  - [📘 스터디 계획](#-스터디-계획)
  - [📊 문제 난이도](#-문제-난이도)
  - [⏰ 타임 테이블](#-타임-테이블)
  - [🧐 COC(Code of Conduct, 행동 규칙)](#-coccode-of-conduct-행동-규칙)
  - [💻 스터디 규칙](#-스터디-규칙)
  - [🍴 PR 규칙](#-pr-규칙)
  - [💻 디렉토리 및 파일 구조](#-디렉토리-및-파일-구조)
  - [💦 참고](#-참고)

## 📕 문제 보관함

[문제](https://www.notion.so/redniche/200975cde215475fa8b3f9f82242fe79?v=3f2b97428e1a4547a10ecd15d8e692d7)

## 📘 스터디 계획

- 푼 문제를 기록한다.
- GitHub Organization 기능을 활용하여 Repository를 Fork하여 PR로 기록을 남긴다.
- 풀 문제를 [문제보관함](https://www.notion.so/redniche/200975cde215475fa8b3f9f82242fe79?v=3f2b97428e1a4547a10ecd15d8e692d7)에 등록한다.    

## 📊 문제 난이도

- 백준 실버5 ~ 골드1
- 프로그래머스 레벨 1 ~ 3

## ⏰ 타임 테이블

| 시간 | 내용 |
| --- | --- |
| 자유 | 알고리즘 문제 풀이 |

## 🧐 COC(Code of Conduct, 행동 규칙)

- 먼저 나온 의견을 깊게 파서 끝을 보았을 때 다음 의견을 말한다.
- 자신을 비하하지 않고 자신감을 가진다.
- 남들이 얻을 수 있는 것을 
내가 노력해서 얻지 못하는 것은 없다고 믿는다.
- 스터디는 삶을 좀 더 풍요롭게 좀 더 지혜롭게 만들 것을 믿는다.
- 불참은 지양하고 스터디를 회사와 가족 다음으로 중요히 여긴다.

## 💻 스터디 규칙

- 스터디는 페어 코딩으로 진행된다.
- 페어코딩을 위해 Visual Studio Code라는 IDE로 풀이 도구를 통일한다.
- Live Share Extension을 활용한다.
    
    ![README_IMG_1](https://user-images.githubusercontent.com/44011226/189650785-4127dfa7-f31a-4e99-8dbe-cbd47261bd3b.png)
    
- 소통
    - Discord: 음성대화와 화면공유로 스터디를 진행하기 위해 사용한다
    - Kakaotalk: 스터디 불참, 개선의견 등의 전파를 위해 사용한다.
    - Notion: 개선의견, 기록, 문서화 등을 위해 사용한다.
- 문제 풀이
    - 문제의 풀이 중 Discord로 소통한다.
    - 문제는 둘이서 의논하며 같이 푼다.
    - 화면공유를 통해 서로의 화면을 확인하며 문제를 푼다.
    - 코드는 Live Share Extension을 통해 페어 코딩으로 진행한다.
- 코드 규칙
    - 문제의 시작은 항상 문제 링크를 주석으로 기록한다
    - 문제 해결을 코드로 시도하기 전에 의견을 모아 풀이 방식을 선정한다
    - 마지막 시간동안 문제 풀이를 본 후에 베스트 알고리즘을 적는다

```python
# https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 예상 알고리즘: BFS
# 베스트 알고리즘: BFS

''' 풀이 코드 '''
```

- 각자 이름(이니셜 ex. ksh)을 `branch`로 생성하여 파일을 commit 및 PR한다.
    - 코드 리뷰가 끝나면 `main`로 merge한다.
- 커밋 규칙
    - 일반파일
        - 모든 파일은 main 브랜치에 바로 커밋한다.
        - 커밋 구분을 위해 일반파일과 풀이는 서로 다른 커밋 규칙을 사용한다.
            - 동사로 `Add 대신 Create`를 사용한다.
            - 동사로 `Fix 대신 Update`를 사용한다.
            - 동사로 `Move 대신 Goto`를 사용한다.
            - 동사로 `Rename 대신 Change name`를 사용한다.
        - Markdown은 docs, 그 외 파일은 file이란 형식을 앞에 붙인다.
        - `docs: Create README.md`
        - `docs: Update README.md`
        - `file: Create picture.png`
        - 기타 변경사항 `chore: [내용]`
        - … 다른 요구가 발생하면 상의 하에 규칙을 추가한다.
    - 풀이
        - 모든 코드는 Pull Request 로 추가되어야 하고 코드 리뷰 이후 main branch에 Merge한다.
        - 모든 풀이 파일은 성명 경로를 제외하고 페어끼리 동일해야 한다.
        - 파일 추가
            - `add: 풀이날짜_이름_플랫폼_문제이름`
            - ex) `add: 220912_이름_pg_N개의최소공배수`
        - 파일 수정
            - `fix: 풀이날짜_이름_플랫폼_문제이름`
        - 파일명 변경, 파일 이동
            - `move: 풀이날짜_이름_플랫폼_문제이름`
        - 플랫폼 이름
            - boj ← [백준](https://www.acmicpc.net/)을 뜻한다.
            - pg ← [프로그래머스](https://programmers.co.kr/)를 뜻한다.

## 🍴 PR 규칙

- 스터디 종료 시 PR
- PR 제목 
백준 예시 ) → 220707 이름 플랫폼 문제번호 문제이름  (220707 장예찬 백준 2615 오목 풀이)
- PR 내용 → 풀이 방법에 대한 간단한 설명
- PR 승인할 때 Comment 하나씩 달아주기 (칭찬하기)

## 💻 디렉토리 및 파일 구조

`/폴더명/풀이날짜__플랫폼_문제이름.py` 

`/폴더명/성명/풀이날짜_플랫폼_문제이름.py`

ex) `/dfs/220912_장예찬_boj_DFS스페셜저지.py`   `/dfs/220912_고하람_boj_DFS스페셜저지.py`

기본적인 구조는 [Algorithm](https://github.com/redniche/Algorithm)를 따른다.

| 폴더명 | 내용 |
| --- | --- |
| base of base | 프로그래머스 level1, 백준 bronze급 |
| combination | 완전 탐색 중 조합을 이용한 풀이 |
| permutation | 완전 탐색 중 순열을 이용한 풀이 |
| hash | 해시 자료구조를 이용한 풀이 |
| linkedlist | 링크드 리스트를 이용한 풀이 |
| priorityqueue | 우선순위 큐를 이용한 풀이 |
| queue | 큐를 이용한 풀이 |
| stack | 스택을 이용한 풀이 |
| divide and conquer | 분할 정복을 이용한 풀이 |
| dynamic programming | 다이나믹 프로그래밍을 이용한 풀이 |
| bfs | 그래프의 완전탐색 중 bfs 를 사용한 풀이 |
| binary search | 이진 탐색을 이용한 풀이 |
| dfs | 그래프의 완전 탐색 중 dfs를 이용한 풀이 |
| dijkstra | 다익스트라 알고리즘을 이용한 풀이 |
| mst | 최소신장트리를 이용한 풀이 |
| prim | 프림 알고리즘을 이용한 풀이 |
| trie | 트라이 자료구조를 이용한 그래프 알고리즘 |
| union-find | 유니온 파인드 자료구조를 이용한 그래프 알고리즘 |
| greedy | 탐욕법을 이용한 풀이 |
| math | 수학식만을 이용해 푸는 풀이 |
| simulation | 따로 알고리즘이 필요하지 않고 문제에 주어진 조건을 이용해 푸는 풀이 |
| sort | 정렬이 풀이의 핵심인 풀이 |
| string | 문자열 처리가 핵심인 풀이 |

## 💦 참고

[fork해서 Pull Request 보내는 법](https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/)

[fork된 Repository 최신상태 유지하는 법](https://jybaek.tistory.com/775)
