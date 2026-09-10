"""Safe educational cryptography GUI.

No wallet recovery or address-targeted key search is implemented.
"""
import hashlib
import tkinter as tk
from tkinter import ttk


class CryptoResearchGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chimera Crypto Research — Safe Lab")
        self.geometry("900x520")
        self._build()

    def _build(self):
        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Cryptography Research Lab", font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        ttk.Label(frame, text="Hashing and public protocol concepts only. Private-key recovery is intentionally excluded.").pack(anchor="w", pady=(0, 16))
        row = ttk.Frame(frame)
        row.pack(fill="x")
        ttk.Label(row, text="Algorithm").pack(side="left")
        self.alg = ttk.Combobox(row, values=("sha256", "sha512", "sha3_256", "sha3_512"), state="readonly")
        self.alg.set("sha256")
        self.alg.pack(side="left", padx=8)
        self.input = ttk.Entry(row)
        self.input.pack(side="left", fill="x", expand=True, padx=8)
        ttk.Button(row, text="Hash", command=self.hash_value).pack(side="left")
        ttk.Label(frame, text="Digest").pack(anchor="w", pady=(20, 4))
        self.output = tk.Text(frame, height=5, wrap="word")
        self.output.pack(fill="x")

    def hash_value(self):
        name = self.alg.get().replace("-", "").lower()
        digest = hashlib.new(name, self.input.get().encode()).hexdigest()
        self.output.delete("1.0", "end")
        self.output.insert("1.0", digest)


if __name__ == "__main__":
    CryptoResearchGUI().mainloop()
