from .arithmetic import arithmetic


def convert_to_4(raw_points, score_type, arith=None):
    ret = []
    if score_type == 'hundred' and arith is None:
        raise ValueError('You must specify arith in `hundred` score type')
    for raw_point in raw_points:
        target_point = -1
        found = False
        arith_data = arithmetic[score_type][arith] if score_type == 'hundred' else arithmetic[score_type]
        for rank_data in arith_data:
            rank, point = rank_data['rank'], rank_data['point']
            if score_type == 'hundred':
                if rank[0] <= raw_point <= rank[1]:
                    target_point = point
                    found = True
                    break
            elif rank == raw_point:
                target_point = point
                found = True
                break
        if not found:
            raise ValueError(
                'We cannot find appropriate 4 points GPA of score (%s) as %s in %s' % (str(raw_point), score_type, arith))
        ret.append(target_point)
    return ret
