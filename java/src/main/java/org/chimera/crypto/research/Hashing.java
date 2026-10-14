package org.chimera.crypto.research;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HexFormat;

/** Small deterministic hashing helpers for public vectors and synthetic research. */
public final class Hashing {
    private Hashing() {}

    public static byte[] sha256(byte[] input) {
        if (input == null) throw new IllegalArgumentException("input must not be null");
        try {
            return MessageDigest.getInstance("SHA-256").digest(input.clone());
        } catch (NoSuchAlgorithmException impossible) {
            throw new IllegalStateException("Required SHA-256 provider is unavailable", impossible);
        }
    }

    public static String sha256Hex(byte[] input) {
        return HexFormat.of().formatHex(sha256(input));
    }

    public static String sha256Hex(String input) {
        if (input == null) throw new IllegalArgumentException("input must not be null");
        return sha256Hex(input.getBytes(StandardCharsets.UTF_8));
    }
}