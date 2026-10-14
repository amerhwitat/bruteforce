package org.chimera.crypto.research;

/** CLI for public hash vectors and bounded synthetic benchmarking only. */
public final class ResearchCli {
    private ResearchCli() {}

    public static void main(String[] args) {
        if (args.length == 0 || "--help".equals(args[0])) {
            System.out.println("Safe Crypto Research CLI\n  sha256 <text>\n  benchmark <iterations:1..1000000>");
            return;
        }
        try {
            switch (args[0]) {
                case "sha256" -> {
                    if (args.length != 2) throw new IllegalArgumentException("usage: sha256 <text>");
                    System.out.println(Hashing.sha256Hex(args[1]));
                }
                case "benchmark" -> {
                    if (args.length != 2) throw new IllegalArgumentException("usage: benchmark <iterations>");
                    SyntheticBenchmark.Result result = SyntheticBenchmark.run(Integer.parseInt(args[1]));
                    System.out.printf("iterations=%d elapsedNanos=%d finalDigest=%s%n",
                            result.iterations(), result.elapsedNanos(), result.finalDigest());
                }
                default -> throw new IllegalArgumentException("unknown command: " + args[0]);
            }
        } catch (IllegalArgumentException exception) {
            System.err.println("error: " + exception.getMessage());
            System.exit(2);
        }
    }
}