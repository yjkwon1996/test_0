# 2020 카카오 인턴십
# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258

# 정확성, 효율성 테스트
# 특정 범위를 모두 구매해야 함. 중간에 빠질 수 없음
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매하기
# ex) 3 4 5 6 7 에 루비 다이아 다이아 에메랄드 사파이어가 있으면, 다이아가 2번 중복되더라도 모두 구매해야 함
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems
# 모든 보석을 하나 이상 보함하는 가장 짧은 구간을 찾아서 return. [시작번호, 끝번호] 형태로 return

# gems 배열 내에서, 중복을 제외하고 모든 요소들을 한번씩은 구매해야 한다.
# 중복 제거한 set을 이용해서 구매해야 할 요소들의 목록을 만들고, 이것을 활용하여 계산


# 효율성에서 통과 실패
def solution_fail(gems):
    answer = []
    arr = list(set(gems)) # 포함되어야 하는 요소들을 저장
    arr_set = set()
    
    start = 0
    end = len(gems) - 1
    
    
    for i in range(len(gems)) : # 순회를 통해 짧은 구간을 갱신
        for j in range(i, len(gems)) :
            arr_set.add(gems[j])
            if len(arr_set) == len(set(gems)) and end - start > j - i :
                start = i
                end = j
                break
        arr_set.clear()
    answer.append(start+1)
    answer.append(end+1)

    
    return answer



# 효율성 통과를 위한 코드
# 투 포인터 알고리즘
# 리스트에 순차적으로 접근해야 할 때 두 개의 점 위치를 기록하면서 처리하는 알고리즘
# start와 end, 두개의 포인트를 사용한다.
# 찾고자 하는 구간의 조건을 만족할 때까지 끝점을 증가시키고, 그 뒤에 해당 구간을 최소화하도록 시작점을 증가시켜
# 최소 구간을 찾는 방법

# 시작점과 끝점을 0에서 시작. 끝점이 먼저 증가하여 구간을 늘리고 시작점이 증가하며 구간을 줄여나간다.
# 끝점이 증가함에 따라 해당 위치의 보석이 구간에 포함됨으로서 현재 구간이 필요한 조건을 만족하는지 확인
# 현재 구간이 조건을 만족하면 시작점을 증가시키면서 조건을 만족시키는 최단 구간을 탐색
# 기존의 최단 구간의 길이와 비교하여 새로운 최단구간의 길이가 더 짧다면 길이 갱신
# 끝 점이 gems의 마지막까지 도달하지 않았다면 다시 끝점을 늘려가며 1번부터 다시 반복


def solution(gems):
    answer = []
    shortest_section = len(gems) + 1 # 현재 최단 구간
    
    start, end = 0, 0 # 구간의 시작점, 끝점
    
    check_len = len(set(gems)) # 보석의 총 종류 수
    check = {} # 현재 구간에 포함된 보석들(종류 : 개수)
    
    while end < len(gems) : # 구간의 끝점이 gems의 길이보다 작으면 반복
        
        if gems[end] not in check : # 현재 끝점의 보석이 처음 발견된 보석의 종류라면
            check[gems[end]] = 1 # check 딕셔너리에 추가
        else : check[gems[end]] += 1 # 이미 있으면 +1
        
        end += 1 # 끝 점 증가
        
        # 현재 구간 내 보석의 종류의 갯수가 전체 보석 종류의 갯수와 같다면
        # 현재 구간 내에 모든 보석의 종류가 들어 있다면
        if len(check) == check_len : 
            while start < end : # 시작점이 끝점과 같아질 때까지 시작점을 증가시킨다.
                if check[gems[start]] > 1 : # 시작점에 해당하는 보석이 구간 내에 하나 초과로 있다면
                    check[gems[start]] -= 1 # 구간 내 보석 하나 감소
                    start += 1
                    
                elif shortest_section > end - start : # 기존의 최단거리보다 현재의 최단거리가 더 짧다면 
                    shortest_section = end - start # 최단거리 갱신
                    answer = [start + 1, end] # answer도 갱신하면서 진행
                    break
                else : break

    return answer






if __name__ == "__main__" :
    gems1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] # [3, 7]
    gems2 = ["AA", "AB", "AC", "AA", "AC"] # [1, 3]
    gems3 = ["XYZ", "XYZ", "XYZ"] # [1, 1]
    gems4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"] # [1, 5]
    
    print(solution(gems1))
    print(solution(gems2))
    print(solution(gems3))
    print(solution(gems4))
    