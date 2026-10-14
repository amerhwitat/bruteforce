package org.chimera.crypto.research;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HashingTest {
    @Test void matchesPublishedSha256EmptyInputVector() {
        assertEquals("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                Hashing.sha256Hex(new byte[0]));
    }

    @Test void matchesPublishedSha256AbcVector() {
        assertEquals("ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
                Hashing.sha256Hex("abc"));
    }

    @Test void rejectsNullInput() {
        assertThrows(IllegalArgumentException.class, () -> Hashing.sha256Hex((String) null));
    }

    @Test void benchmarkIsBoundedAndDeterministic() {
        var first = SyntheticBenchmark.run(3);
        var second = SyntheticBenchmark.run(3);
        assertEquals(first.finalDigest(), second.finalDigest());
        assertEquals(3, first.iterations());
        assertThrows(IllegalArgumentException.class, () -> SyntheticBenchmark.run(0));
        assertThrows(IllegalArgumentException.class, () -> SyntheticBenchmark.run(1_000_001));
    }
}