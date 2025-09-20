import statistics

def summarize_data(data):
    numbers = []
    

    for item in data:
        try:
            num = float(item)
            if not (num != num):
                numbers.append(num)

        except(ValueError, TypeError):
            continue

    if not numbers:
        return {'count':0,
        'mean':0.0,
        'median':0.0,
        'mode': None,
        'stdev':0.0
        }
    
    summary = {
    'count': len(numbers),
    'mean': round(statistics.mean(numbers), 2),
    'median': round(statistics.median(numbers), 2),
    'mode': statistics.mode(numbers) if len(set(numbers)) != len(numbers) else None,
    'stdev': round(statistics.stdev(numbers), 2)
    if len(numbers) > 1 else 0.0 
    }
    
    return summary
    
data = ['none', 'moon','str','-', 99, 77 ,44,12, 'NaN', [], {}]
result = summarize_data(data)
print(result)


















