class Difference:
    def __init__(self, a):
        self.__elements = a
        
	# Add your code here
    diffs = []
    def computeDifference(self):
        
        e = self.__elements
        for i in range(len(e)):
            for j in range(i+1, len(e)):
                abs_diff = abs(e[i] - e[j])
                self.diffs.append(abs_diff)
        #print('1 - e: ', e)
        #print('2 - diffs: ', self.diffs)
        return e
        
    def maximumDifference(self):
        #print('3 - diffs: ', self.diffs)
        max_value = max(self.diffs)
        #print(max_value)
        return max_value
    
# End of Difference class

#_ = input()
#a = [int(e) for e in input().split(' ')]

if __name__ == '__main__':

    a = [1, 2, 5]
    d = Difference(a)
    # d.computeDifference()
    print(d.computeDifference())
    print(d.maximumDifference())