class DataProcessor:
    def __init__(self, processor_id):
        self.processor_id = processor_id
        print(f"Data Processor {self.processor_id} siap.")

    def process(self, *args, **kwargs):
        print(f"\n--- {self.processor_id} Memproses Data ---")

        if args:
            print("Argumen Posisi Diterima:")
            for i, arg in enumerate(args):
                print(f"  args[{i}]: {arg} (tipe: {type(arg).__name__})")
        else:
            print("Tidak ada argumen posisi.")

        if kwargs:
            print("Argumen Kata Kunci Diterima:")
            for kunci, nilai in kwargs.items():
                print(f"  {kunci}: {nilai} (tipe: {type(nilai).__name__})")
        else:
            print("Tidak ada argumen kata kunci.")
        print("---------------------------------")

if __name__ == "__main__":
    processor1 = DataProcessor("DP-001")

    print("\nPanggilan 1: Tanpa argumen tambahan")
    processor1.process()

    print("\nPanggilan 2: Hanya argumen posisi")
    processor1.process(100, "Status OK", 99.9, False)

    print("\nPanggilan 3: Hanya argumen kata kunci")
    processor1.process(user="admin", level=5, mode="verbose")

    print("\nPanggilan 4: Kombinasi argumen posisi dan kata kunci")
    processor1.process("Task-A", "Task-B", status="Running", priority="High", thread_id=54321)