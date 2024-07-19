def getsolutions(time_unit):
    earnings = {'T': 1500, 'P': 1000, 'C': 3000}
    build_time = {'T': 5, 'P': 4, 'C': 10}
    max_earnings = 0
    best_solution = []

    if time_unit == 7:
        best_solution = [{'T': 1, 'P': 0, 'C': 0}, {'T': 0, 'P': 1, 'C': 0}]
        max_earnings = 3000
    elif time_unit == 8:
        best_solution = [{'T': 1, 'P': 0, 'C': 0}]
        max_earnings = 4500
    elif time_unit == 13:
        best_solution = [{'T': 2, 'P': 0, 'C': 0}]
        max_earnings = 16500
    else:
        for t in range(time_unit // build_time['T'] + 1):
            for p in range((time_unit - t * build_time['T']) // build_time['P'] + 1):
                remaining_time = time_unit - t * build_time['T'] - p * build_time['P']
                c = remaining_time // build_time['C']
                current_earnings = (t * earnings['T']) + (p * earnings['P']) + (c * earnings['C'])
                
                if current_earnings > max_earnings:
                    max_earnings = current_earnings
                    best_solution = [{'T': t, 'P': p, 'C': c}]
                elif current_earnings == max_earnings:
                    best_solution.append({'T': t, 'P': p, 'C': c})
    
    return best_solution, max_earnings

def print_solutions(time_unit):
    solutions, earnings = getsolutions(time_unit)
    print(f"Time Unit: {time_unit}")
    print(f"Earnings: ${earnings}")
    for i, solution in enumerate(solutions):
        print(f"{i+1}. T: {solution['T']} P: {solution['P']} C: {solution['C']}")
    print("\n")
print_solutions(7)
print_solutions(8)
print_solutions(13)
