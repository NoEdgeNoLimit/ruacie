package net.ttdu.questionsanswer;

import com.google.cloud.datastore.*;

public class QuickstartSample {
    public static void main(String... args) throws Exception {
        // Instantiates a client
        Datastore datastore = DatastoreOptions.getDefaultInstance().getService();

        // The kind for the new entity
        String kind = "Task";
        // The name/ID for the new entity
        String nameaa = "sampletask12";
        // The Cloud Datastore key for the new entity
        Key taskKey = datastore.newKeyFactory().setKind(kind).newKey(nameaa);
        KeyFactory keyFactory = datastore.newKeyFactory().setKind("Task");
        Key taskKey2 = datastore.allocateId(keyFactory.newKey());

        // Prepares the new entity
        Entity task = Entity.newBuilder(taskKey)
                .set("description", "Buy milkaa")
                .build();

        // Saves the entity
        datastore.put(task);

        System.out.printf("Saved %s: %s%n", task.getKey().getName(), task.getString("description"));

        //Retrieve entity
        Entity retrieved = datastore.get(taskKey);

        System.out.printf("Retrieved %s: %s%n", taskKey.getName(), retrieved.getString("description"));

    }
}