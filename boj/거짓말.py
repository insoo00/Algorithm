def find_relation_party(trust_party):
    for idx, party in enumerate(parties):
        for person in party:
            if person in trust_party:
                if not visited[idx]:
                    trust.update(party)
                    visited[idx] = True
                    find_relation_party(party)
                    break

N, M = map(int, input().split())
trust = list(map(int, input().split()))
if trust[0] == 0:
    print(M)
else:
    result = 0
    trust = set(trust[1:])
    parties = []
    for _ in range(M):
        cnt, *party = map(int, input().split())
        parties.append(party)
    visited = [False for _ in range(M)]
    for idx, party in enumerate(parties):
        for person in party:
            if person in trust:
                trust.update(party)
                visited[idx] = True
                find_relation_party(party)
                break

    for party in parties:
        last_person = party[-1]
        for person in party:
            if person in trust:
                break
            else:
                if person == last_person:
                    result += 1

    print(result)
