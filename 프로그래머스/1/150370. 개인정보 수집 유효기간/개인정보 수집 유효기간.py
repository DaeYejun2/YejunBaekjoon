def solution(today, terms, privacies):
    def get_total_days(date_str):
        y,m,d = map(int, date_str.split('.'))
        return (y*12*28)+(m*28)+d
    
    today = get_total_days(today)
    
    term_dict = {}
    for term in terms:
        name, month = term.split()
        term_dict[name] = int(month)*28
        
    res = []
    for i, pri in enumerate(privacies):
        date_part, term_name = pri.split()
        start_days = get_total_days(date_part)
        
        if start_days + term_dict[term_name] <= today:
            res.append(i+1)
    return res