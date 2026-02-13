from utils.logger import logger

def main():
    logger.info("Zecpath AI system started")
    print("Zecpath AI system started ✅")

if __name__ == "__main__":
    main()

import os
from datetime import datetime
from parsers.extractor import extract_resume

def main():
    print("✅ Resume Text Extraction Engine Started")

    file_path = input("Enter resume file path (.pdf/.docx): ").strip().strip('"')

    try:
        text = extract_resume(file_path)

        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = os.path.join("outputs", f"resume_text_{timestamp}.txt")

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(text)

        print("✅ Extraction done!")
        print("✅ Saved to:", out_file)
        print("\n--- Preview (first 300 chars) ---\n")
        print(text[:300])

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()