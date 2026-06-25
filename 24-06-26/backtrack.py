def find_combo(coins,target ,curr_path,start_index):
    print(f"checking the path -> {curr_path} \t remaining target {target}")
    if target==0:
        print(f"succes !!! path-> {curr_path}")
        return
    if target<0:
        print("incorrect choice....... backttracking....")
        return
    for i in range(start_index,len(coins)):
        choice=coins[i]
        curr_path.append(choice)
        find_combo(coins,target-choice,curr_path,1)
        curr_path.pop()
currency=[2,4,5]
target=5
find_combo(currency,target,[],0)