public class Main {
    public static void main(String... args) {
        int sleepDuration = 30000;
        if (args.length > 0) {
            String passedSleepDuration = args[0];
            System.out.println("Overwriding sleep duration to %s".formatted(passedSleepDuration));
            sleepDuration = Integer.parseInt(passedSleepDuration);
        } else {
            System.out.println("No sleep duration arg passed, will sleep for %s".formatted(sleepDuration));
        }

        try {
            Thread.sleep(sleepDuration);
        } catch (Exception e) {
            System.err.println("Thread sleep was interrupted for some reason");
        }

        System.out.println("All good");
    }
}
