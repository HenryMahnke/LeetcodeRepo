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
            #if the list exists we want to binary search the list
            #need to binary search along them 
            l = 0 
            r = len(ls)-1
            while l <= r: 
                m = (r+l)//2
                if ls[m][0] == timestamp:
                    return ls[m][1]
                elif ls[m][0] <timestamp: 
                    l = m+1
                else: 
                    r = m-1
            print(ls[m], m)
            #if they are going to be equal and it's not there 
            #1,2,4,6 target 5 
            #  L M R
            if ls[l-1] and ls[l-1][0] < timestamp: 
                return ls[l-1][1]
            else: 
                return ""


            
        return ""


                

        
