class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #storing unique elements but also associate additional inifomration with each element 
        if self.d.get(key,None):
            self.d[key].append((timestamp,value))
        else: 
            self.d[key] = [(timestamp,value)]
        print("set, key: ",key, "values", value, "timestamp", timestamp)

    def get(self, key: str, timestamp: int) -> str:
        #want to go to the timestamp, then find the key
        #because at a given timestep there could be multiple we need to search
        print("get: key", key, "timestamp", timestamp)
        ls = self.d.get(key,None)
        if ls:
            #then we know that there do exist some keys in it, then we need to binary search, but lets start with the brute force
            for i in range(len(ls)):
                print("ls at i" , ls[i], ls[i][0])
                if ls[i][0] == timestamp: 
                    return ls[i][1]
            #if the key is not in it then we want to return the most recent(time) value of k 
            #we can do this by iterating backward through the list and checking for the first timestamp that is less 
            # for i in range(len(ls)-1, -1,-1):
            #     if ls[i][0] < timestamp: 
            #         #first one that is less than timestamp
            #         return ls[i][1]
            tripped = False
            for i in range(len(ls)):
                if ls[i][0] > timestamp:
                    tripped = True
                    print("tripped")
                    break
            if not tripped:
                print("not tripped?")
                #the last value in the list 
                return ls[-1][1]
            else: # if tripped 
                print("going to return the i-1 value")
                print(ls)

                if ls[i-1] and i-1 >-1:
                    return ls[i-1][1]
                else: 
                    return "" 
            
            #if the list exists, but it is not at time stamp, and there is no time stamp that is less 
            #then we return empty 
            return ""
        return ""


                

        
