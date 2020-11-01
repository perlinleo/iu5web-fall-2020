def main():
    #  _____                 _        _  _   
    # |_   _|   __ _   ___  | | __   | || |  
    #   | |    / _` | / __| | |/ /   | || |_ 
    #   | |   | (_| | \__ \ |   <    |__   _|
    #   |_|    \__,_| |___/ |_|\_\      |_|  
                                        
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    
    result = sorted(data
                    ,reverse = True)
    print(result)  
    
    result_with_lambda = sorted(data,
                                key=lambda x: x,
                                reverse=True)
    
    print(result_with_lambda)
    #_______________________________________________________

if __name__ == '__main__':
    main()
