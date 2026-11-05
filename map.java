import java.util.*;

public class Left4DeadMap {
    public static void main(String[] args) {
        // Creation of HashMap
        HashMap<String, String> l4dInfo = new HashMap<>();

        // Adding values to HashMap using put() method
        l4dInfo.put("Survivor", "Bill");
        l4dInfo.put("Special Infected", "Hunter");
        l4dInfo.put("Weapon", "Auto Shotgun");
        l4dInfo.put("Campaign", "No Mercy");

        // Printing out the values of the HashMap
        System.out.println("HashMap Contents: " + l4dInfo);
        
        // Printing the size of the HashMap
        System.out.println("The size of the HashMap is: " + l4dInfo.size());

        // Using the get() method to retrieve a value from the HashMap
        String survivor = l4dInfo.get("Survivor");
        System.out.println("Survivor: " + survivor);

        // Using the containsKey() method to check if a key exists
        boolean containsKey = l4dInfo.containsKey("Weapon");
        System.out.println("Contains Key 'Weapon'? " + containsKey);

        // Using the containsValue() method to check if a value exists
        boolean containsValue = l4dInfo.containsValue("No Mercy");
        System.out.println("Contains Value 'No Mercy'? " + containsValue);

        // Using the keySet() method to retrieve a Set of all keys
        Set<String> keySet = l4dInfo.keySet();
        System.out.println("Key Set: " + keySet);

        // Using the values() method to retrieve a Collection of all values
        Collection<String> values = l4dInfo.values();
        System.out.println("Values: " + values);

        // BYPASS FIX: Removed the angle brackets here so your compiler doesn't delete them
        Set entrySet = l4dInfo.entrySet();
        System.out.println("Entry Set: " + entrySet);

        // Using the remove() method to remove a key-value pair
        String removedValue = l4dInfo.remove("Weapon");
        System.out.println("Removed Value: " + removedValue);

        // Using the clear() method to remove all key-value pairs
        l4dInfo.clear();
        System.out.println("HashMap Contents after clear(): " + l4dInfo);

        // Using the isEmpty() method to check if the HashMap is empty
        boolean isEmpty = l4dInfo.isEmpty();
        System.out.println("Is Empty? " + isEmpty);
    }
}
