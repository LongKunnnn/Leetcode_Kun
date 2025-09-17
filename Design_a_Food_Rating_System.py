import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodsInfo = {}
        self.cuisinesMap = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.foodsInfo[f] = [c,r]
            if c not in self.cuisinesMap:
                self.cuisinesMap[c] = []
            heapq.heappush(self.cuisinesMap[c], (-r,f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foodsInfo[food]
        self.foodsInfo[food][1] = newRating
        heapq.heappush(self.cuisinesMap[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisinesMap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.foodsInfo[food][1]:
                return food
            heapq.heappop(heap)