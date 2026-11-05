import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, String> vehicles = new HashMap<>();
        vehicles.put("Toyota", "Corolla");
        vehicles.put("Honda", "Civic");

        // 1. Loop through Keys only
        for (String brand : vehicles.keySet()) {
            System.out.println("Brand: " + brand);
        }

        // 2. Loop through Values only
        for (String model : vehicles.values()) {
            System.out.println("Model: " + model);
        }

        // 3. Loop through BOTH (Key and Value)
        for (Map.Entry<String, String> entry : vehicles.entrySet()) {
            System.out.println(entry.getKey() + " makes the " + entry.getValue());
        }
    }
}
