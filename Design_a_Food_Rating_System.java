import java.util.*;
class Design_a_Food_Rating_System{
    private static class Food{
        String name;
        int rating;
        Food(String n, int r) {
            name = n; rating = r;
        }
    }

    private Map<String, String> foodCuisine;
    private Map<String, Integer> foodRating;
    private Map<String, PriorityQueue<Food>> cuisineMap; 

    public Design_a_Food_Rating_System(String[] foods, String[] cuisines, int[] ratings) {
        foodCuisine = new HashMap<>();
        foodRating = new HashMap<>();
        cuisineMap = new HashMap<>();

        for (int i = 0; i < foods.length; i++) {
            String f = foods[i], c = cuisines[i];
            int r = ratings[i];
            foodCuisine.put(f,c);
            foodRating.put(f,r);

            cuisineMap.putIfAbsent(c, new PriorityQueue<>(
                (a, b) -> a.rating == b.rating ? a.name.compareTo(b.name) : b.rating - a.rating 
            ));
            cuisineMap.get(c).offer(new Food(f, r));
        }
    }
    
    public void changeRating(String food, int newRating) {
        String c = foodCuisine.get(food);
        foodRating.put(food, newRating);
        cuisineMap.get(c).offer(new Food(food, newRating));
    }
    
    public String highestRated(String cuisine) {
        PriorityQueue<Food> pq = cuisineMap.get(cuisine);
        while (true) {
            Food top = pq.peek();
            if (foodRating.get(top.name) == top.rating) {
                return top.name;
            }
            pq.poll();
        } 
    }
}

