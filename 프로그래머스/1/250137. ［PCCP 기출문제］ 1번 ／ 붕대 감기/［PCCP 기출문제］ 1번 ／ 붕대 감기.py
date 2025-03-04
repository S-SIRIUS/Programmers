def recovery_check(health, recovery, limit):
    if health+recovery <= limit:
        return health+recovery
    else:
        return limit

def solution(bandage, health, attacks):
    answer = 0
    connect_time=0
    attack_index=0
    limit = health
    for time in range(0, attacks[-1][0]+1):
        if time == attacks[attack_index][0]:
            health-=attacks[attack_index][1]
            if health <=0:
                health=-1
                break
            connect_time=0
            attack_index+=1
        else:
            connect_time+=1
            health = recovery_check(health, bandage[1], limit)
            
            if connect_time==bandage[0]:
                health = recovery_check(health, bandage[2], limit)
                connect_time=0
        print(time, health)
    return health