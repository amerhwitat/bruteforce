package org.chimera.crypto.research;

import java.nio.charset.StandardCharsets;

/** Bounded synthetic SHA-256 benchmark; it never searches keys, seeds, or credentials. */
public final class SyntheticBenchmark {
    public static final int MAX_ITERATIONS = 1_000_000;
    private static final byte[] PAYLOAD = "Chimera safe synthetic crypto benchmark v1".getBytes(StandardCharsets.UTF_8);

    private SyntheticBenchmark() {}

    public record Result(int iterations, long elapsedNanos, String finalDigest) {}

    public static Result run(int iterations) {
        if (iterations < 1 || iterations > MAX_ITERATIONS) {
            throw new IllegalArgumentException("iterations must be between 1 and " + MAX_ITERATIONS);
        }
        byte[] value = PAYLOAD.clone();
        long start = System.nanoTime();
        for (int i = 0; i < iterations; i++) value = Hashing.sha256(value);
        long elapsed = System.nanoTime() - start;
        return new Result(iterations, elapsed, java.util.HexFormat.of().formatHex(value));
    }
}